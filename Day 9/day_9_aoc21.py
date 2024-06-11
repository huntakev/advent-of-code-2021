from dataclasses import dataclass
from pathlib import Path

SAMPLE_DATA_PATH = Path(r"sample_input_day_9_aoc21.txt")
PUZZLE_DATA_PATH = Path(r"puzzle_input_day_9_aoc21.txt")

Position = tuple[int, int]
Elevation = int
HeightMap = dict[Position, Elevation]


def load_height_map(path: Path) -> HeightMap:
    """Load input data from specified path."""
    with open(path) as f:
        data = []
        rows = f.read().splitlines()
        for row in rows:
            data.append([int(num) for num in row])
        height_map: HeightMap = {}
        for row_index, row_value in enumerate(data):
            for column_index, column_value in enumerate(row_value):
                position: Position = (row_index, column_index)
                elevation: Elevation = column_value
                height_map[position] = elevation
        return height_map


@dataclass
class Node:
    """LavaCave Node."""

    position: Position
    elevation: Elevation


class LavaCave:
    """LavaCave."""

    def __init__(self, height_map: HeightMap) -> None:
        """Initialize LavaCave."""
        self.height_map = height_map
        self.x_length = max([value[0] for value in self.height_map.keys()]) + 1
        self.y_length = max([value[1] for value in self.height_map.keys()]) + 1

    def measure_risk_level(self) -> int:
        """Measure risk level of LavaCave."""
        risk_level = 0
        low_nodes = self._get_low_nodes()
        for low_node in low_nodes:
            risk_level += low_node.elevation + 1
        return risk_level

    def measure_basin_size(self) -> int:
        """Measure basin size of LavaCave."""
        basin_sizes = []
        low_nodes = self._get_low_nodes()
        for low_node in low_nodes:
            basin_sizes.append(self._recursive_basin_measurement(low_node))
        basin_sizes.sort(reverse=True)
        return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    def _get_low_nodes(self) -> list[Node]:
        """Get list of nodes representing low points."""
        low_nodes: list[Node] = []
        for node in [Node(position, elevation) for position, elevation in self.height_map.items()]:
            neighbour_nodes = self._get_neighbour_nodes(node)
            if node not in low_nodes and self._is_low_node(node, neighbour_nodes):
                low_nodes.append(node)
        return low_nodes

    def _get_neighbour_nodes(self, node: Node) -> list[Node]:
        """Get neighbour nodes surrounding input node."""
        neighbour_nodes: list[Node] = []
        relative_positions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for relative_position in relative_positions:
            position: Position = (node.position[0] + relative_position[0], node.position[1] + relative_position[1])
            if -1 < position[0] < self.x_length:
                if -1 < position[1] < self.y_length:
                    neighbour_nodes.append(Node(position, self.height_map[position]))
        return neighbour_nodes

    def _recursive_basin_measurement(
            self, node: Node, measured_nodes: list[Node] | None = None, basin_size: int = 0
    ) -> int:
        """Recursively measure basin size starting at specified node."""
        if measured_nodes is None:
            measured_nodes = []
        if node.elevation != 9 and node not in measured_nodes:
            measured_nodes.append(node)
            basin_size += 1
            for neighbour_node in self._get_neighbour_nodes(node):
                basin_size = self._recursive_basin_measurement(neighbour_node, measured_nodes, basin_size)
        return basin_size

    @staticmethod
    def _is_low_node(node: Node, neighbour_nodes: list[Node]) -> bool:
        """Return whether specified node is lowest among specified neighbour nodes."""
        return not any(node.elevation >= neighbour.elevation for neighbour in neighbour_nodes)


def main():
    height_map = load_height_map(PUZZLE_DATA_PATH)
    lava_cave = LavaCave(height_map)
    risk_level = lava_cave.measure_risk_level()
    basin_size = lava_cave.measure_basin_size()
    print(f"{risk_level=} {basin_size=}")


if __name__ == "__main__":
    main()
