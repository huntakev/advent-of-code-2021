"""Day 14 Advent of Code."""

from pathlib import Path

SAMPLE_INPUT_FILE = Path(r"sample_input_day_14_aoc21.txt")
PUZZLE_INPUT_FILE = Path(r"puzzle_input_day_14_aoc21.txt")

PolymerTemplate = str
InsertionRules = dict[str, str]


def load_polymer_template_and_insertion_rules(
    path: Path,
) -> tuple[PolymerTemplate, InsertionRules]:
    """Load cave connections from file."""
    with open(path, encoding="utf-8") as file:
        data = file.read().splitlines()
    polymer_template: PolymerTemplate = data[0]
    insertion_rules: InsertionRules = {}
    for row in data[2:]:
        columns = row.split(" -> ")
        insertion_rules[columns[0]] = columns[1]
    return polymer_template, insertion_rules


class PolymerizationEquipment:
    """Equipment for decoding insertion rules and generating polymers."""

    def __init__(
        self, polymer_template: PolymerTemplate, insertion_rules: InsertionRules
    ) -> None:
        """Initialize PolymerizationEquipment."""
        self._polymer_template = polymer_template
        self._insertion_rules = insertion_rules
        self.pairings_counter = self._create_pairings_counter()
        self.elements_counter = self._create_elements_counter()

    def step_polymer_n_steps(self, n_steps: int) -> None:
        """Step polymer number of times specified."""
        for _ in range(n_steps):
            self._step_polymer()

    def _step_polymer(self) -> None:
        """Step polymer once."""
        next_pairings_counter = self.pairings_counter.copy()
        for pairing, occurences in self.pairings_counter.items():
            new_element = self._insertion_rules[pairing]
            self.elements_counter[new_element] += occurences
            next_pairings_counter[f"{pairing[0]}{new_element}"] += occurences
            next_pairings_counter[f"{new_element}{pairing[1]}"] += occurences
            next_pairings_counter[pairing] -= occurences
        self.pairings_counter = next_pairings_counter

    def _create_pairings_counter(self) -> dict[str, int]:
        """Create dictionary of all permissible pairings."""
        pairings_counter: dict[str, int] = {}
        for polymer_index in range(len(self._polymer_template) - 1):
            pairing = (
                f"{self._polymer_template[polymer_index]}"
                f"{self._polymer_template[polymer_index + 1]}"
            )
            if pairing not in pairings_counter:
                pairings_counter[pairing] = 1
            else:
                pairings_counter[pairing] += 1
        for insertion_rule_key in self._insertion_rules:
            if insertion_rule_key not in pairings_counter:
                pairings_counter[insertion_rule_key] = 0
        return pairings_counter

    def _create_elements_counter(self) -> dict[str, int]:
        """Create dictionary of all permissible elements."""
        elements_counter: dict[str, int] = {}
        for element in self._polymer_template:
            if element not in elements_counter:
                elements_counter[element] = 1
            else:
                elements_counter[element] += 1
        for insection_rule_key in self._insertion_rules:
            for element in insection_rule_key:
                if element not in elements_counter:
                    elements_counter[element] = 0
        return elements_counter

    def score_polymer_after_n_steps(self, num_steps: int) -> int:
        """Score polymer after number of steps specified."""
        self.step_polymer_n_steps(num_steps)
        return self._count_most_common_element() - self._count_least_common_element()

    def _count_least_common_element(self) -> int:
        """Return count of least common element in polymer."""
        return min(self.elements_counter.values())

    def _count_most_common_element(self) -> int:
        """Return count of most common element in polymer."""
        return max(self.elements_counter.values())


def main():
    """Main."""
    polymer_template, insertion_rules = load_polymer_template_and_insertion_rules(
        PUZZLE_INPUT_FILE
    )
    polymerization_equipment = PolymerizationEquipment(
        polymer_template, insertion_rules
    )
    print(polymerization_equipment.score_polymer_after_n_steps(40))


if __name__ == "__main__":
    main()
