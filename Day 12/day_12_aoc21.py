"""Day 12 Advent of Code."""

from pathlib import Path
from typing import Callable

SIMPLE_INPUT_FILE = Path(r"simple_input_day_12_aoc21.txt")
SAMPLE_INPUT_FILE = Path(r"sample_input_day_12_aoc21.txt")
PUZZLE_INPUT_FILE = Path(r"puzzle_input_day_12_aoc21.txt")

Connection = list[str]


def load_cave_connections(path: Path) -> list[Connection]:
    """Load cave connections from file."""
    connections: list[Connection] = []
    with open(path, encoding="utf-8") as file:
        data = file.read().splitlines()
    for row in data:
        connections.append(row.split("-"))
    return connections


class Cave:
    """Subterranean cave."""

    def __init__(self, name: str, connection_names: list[str]) -> None:
        """Initialize Cave."""
        self._name = name
        self._connection_names = connection_names

    @property
    def name(self) -> str:
        """Return name of cave."""
        return self._name

    @property
    def connection_names(self) -> list[str]:
        """Return list of names of connections."""
        return self._connection_names

    @property
    def is_large(self) -> bool:
        """Return whether cave is large."""
        return self.name.isupper()


CaveMap = dict[str, Cave]
CavePath = list[Cave]


class PathPlanner:
    """Subterranean path planner."""

    _start_cave_name = "start"
    _end_cave_name = "end"

    def __init__(self, connections: list[Connection]) -> None:
        """Initialize PathPlanner."""
        self.cave_map = self._parse_connections_to_cave_map(connections)

    def find_num_paths_with_one_visit_to_small_caves(self) -> int:
        """Find number of paths that include visiting small caves no more than once."""
        start_cave = self.cave_map[self._start_cave_name]
        _, cave_paths = self._find_paths_with_visitation_rule(
            start_cave,
            [start_cave],
            [],
            self._is_cave_visitable_with_only_small_caves_once,
        )
        return len(cave_paths)

    def find_num_paths_with_one_visit_to_small_caves_and_one_double_visit(self) -> int:
        """Find number of paths that include visiting one small cave no more than
        two times, and the rest no more than once."""
        start_cave = self.cave_map[self._start_cave_name]
        _, cave_paths = self._find_paths_with_visitation_rule(
            start_cave,
            [start_cave],
            [],
            self._is_cave_visitable_with_only_small_caves_once_and_one_double_visit,
        )
        return len(cave_paths)

    def _find_paths_with_visitation_rule(
        self,
        current_cave: Cave,
        previous_cave_path: CavePath,
        all_cave_paths: list[CavePath],
        visitation_rule: Callable[[CavePath, Cave], bool],
    ) -> tuple[CavePath, list[CavePath]]:
        """Find all paths that comply with visitation rule."""
        if current_cave.name == self._end_cave_name:
            all_cave_paths.append(previous_cave_path)
            return ([], [])
        for adjacent_cave in [
            self.cave_map[adjacent_cave_name]
            for adjacent_cave_name in current_cave.connection_names
        ]:
            if visitation_rule(previous_cave_path, adjacent_cave):
                self._find_paths_with_visitation_rule(
                    adjacent_cave,
                    previous_cave_path + [adjacent_cave],
                    all_cave_paths,
                    visitation_rule,
                )
        return ([], all_cave_paths)

    def _is_cave_visitable_with_only_small_caves_once(
        self, previously_visited_caves: list[Cave], cave: Cave
    ) -> bool:
        """Return whether a cave is visitable given current path and single visitation rule."""
        if cave.is_large:
            return True
        return cave not in previously_visited_caves

    def _is_cave_visitable_with_only_small_caves_once_and_one_double_visit(
        self, previously_visited_caves: list[Cave], cave: Cave
    ) -> bool:
        """Return whether a cave is visitable given current path and single visitation rule."""
        if cave.is_large:
            return True
        small_caves = [cave for cave in previously_visited_caves if not cave.is_large]
        if len(small_caves) == len(set(small_caves)) and cave.name not in [
            self._start_cave_name,
            self._end_cave_name,
        ]:
            return True
        return cave not in previously_visited_caves

    @staticmethod
    def _parse_connections_to_cave_map(connections: list[Connection]) -> CaveMap:
        """Parse list of Connections to list of Caves."""
        cave_map: CaveMap = {}
        cave_connections: dict[str, list[str]] = {}
        for connection in connections:
            if connection[0] in cave_connections:
                if connection[1] not in cave_connections[connection[0]]:
                    cave_connections[connection[0]].append(connection[1])
            else:
                cave_connections[connection[0]] = [connection[1]]
            if connection[1] in cave_connections:
                if connection[0] not in cave_connections[connection[1]]:
                    cave_connections[connection[1]].append(connection[0])
            else:
                cave_connections[connection[1]] = [connection[0]]
        for name, connected_caves in cave_connections.items():
            cave_map[name] = Cave(name, connected_caves)
        return cave_map


def main() -> None:
    """Main."""
    connections = load_cave_connections(PUZZLE_INPUT_FILE)
    path_planner = PathPlanner(connections)
    print(
        path_planner.find_num_paths_with_one_visit_to_small_caves(),
        path_planner.find_num_paths_with_one_visit_to_small_caves_and_one_double_visit(),
    )


if __name__ == "__main__":
    main()
