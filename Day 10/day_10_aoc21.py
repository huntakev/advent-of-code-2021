from pathlib import Path

SAMPLE_DATA_PATH = Path(r"sample_input_day_10_aoc21.txt")
PUZZLE_DATA_PATH = Path(r"puzzle_input_day_10_aoc21.txt")

NavigationData = list[str]


def load_navigation_data(path: Path) -> NavigationData:
    """Load input data from specified path."""
    with open(path) as f:
        return f.read().splitlines()


class Character:
    """Navigation subsystem character."""

    PERMITTED_CHARACTERS = ["(", ")", "[", "]", "{", "}", "<", ">"]

    def __init__(self, value: str) -> None:
        if value not in Character.PERMITTED_CHARACTERS:
            raise ValueError(f"value '{value}' invalid - expected value in {Character.PERMITTED_CHARACTERS}")
        self.value = value

    @property
    def opposite_character(self) -> str:
        """Return opposite character."""
        match self.value:
            case "(":
                return ")"
            case ")":
                return "("
            case "[":
                return "]"
            case "]":
                return "["
            case "{":
                return "}"
            case "}":
                return "{"
            case "<":
                return ">"
            case ">":
                return "<"

    @property
    def error_score(self) -> int:
        """Return error score of character."""
        match self.value:
            case ")":
                return 3
            case "]":
                return 57
            case "}":
                return 1197
            case ">":
                return 25137
            case _:
                raise ValueError("invalid character for scoring")

    @property
    def autocomplete_score(self) -> int:
        """Return error score of character."""
        match self.value:
            case ")":
                return 1
            case "]":
                return 2
            case "}":
                return 3
            case ">":
                return 4
            case _:
                raise ValueError("invalid character for scoring")

    @property
    def is_open_character(self) -> bool:
        """Return whether character is an open character."""
        return self.value in ["(", "[", "{", "<"]


class Line:
    """Navigational subsystem line"""

    def __init__(self, characters: list[Character]) -> None:
        """Initialize Line."""
        self.characters = characters

    def calculate_syntax_score(self) -> int | None:
        """Calculate syntax score for line."""
        illegal_character = self._find_first_illegal_character()
        if illegal_character:
            return illegal_character.error_score
        return 0

    def _find_first_illegal_character(self) -> Character | None:
        """Find first illegal ChunkType character in line."""
        expected_characters = []
        for character in self.characters:
            if character.is_open_character:
                expected_characters.append(character)
            else:
                if character.opposite_character == expected_characters[-1].value:
                    expected_characters.pop(-1)
                else:
                    return character
        return None

    def calculate_autocomplete_score(self) -> int | None:
        """Calculate score of line autocomplete characters."""
        if autocomplete_characters := self._find_autocomplete_characters():
            score = 0
            for character in autocomplete_characters:
                score *= 5
                score += character.autocomplete_score
            return score
        return None

    def _find_autocomplete_characters(self) -> list[Character] | None:
        """Find characters required to autocomplete line."""
        if self._find_first_illegal_character() is None:
            expected_characters = []
            for character in self.characters:
                if character.is_open_character:
                    expected_characters.append(character)
                else:
                    if character.opposite_character == expected_characters[-1].value:
                        expected_characters.pop(-1)
            if expected_characters:
                return [Character(character.opposite_character) for character in reversed(expected_characters)]
        return None


class NavigationSubsystem:
    """Navigation Subsystem."""

    def __init__(self, navigation_data: NavigationData) -> None:
        self.lines = []
        for row in navigation_data:
            self.lines.append(Line([Character(value) for value in row]))

    def calculate_syntax_score(self) -> int:
        """Calculate syntax score."""
        syntax_score = 0
        for line in self.lines:
            syntax_score += line.calculate_syntax_score()
        return syntax_score

    def calculate_autocomplete_score(self) -> int:
        """Calculate autocomplete score."""
        autocomplete_scores = []
        for line in self.lines:
            if line_score := line.calculate_autocomplete_score():
                autocomplete_scores.append(line_score)
        autocomplete_scores.sort()
        return autocomplete_scores[round((len(autocomplete_scores) - 1) / 2)]


def main() -> None:
    navigation_data = load_navigation_data(PUZZLE_DATA_PATH)
    navigation_subsystem = NavigationSubsystem(navigation_data)
    syntax_score = navigation_subsystem.calculate_syntax_score()
    autocomplete_score = navigation_subsystem.calculate_autocomplete_score()
    print(f"{syntax_score=} {autocomplete_score=}")


if __name__ == "__main__":
    main()
