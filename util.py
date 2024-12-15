class CharGrid:
    def __init__(self, data=None):
        self.grid = {}
        if data:
            lines = [line.strip() for line in data.splitlines() if line.strip()]

            lengths = [len(line) for line in lines]
            assert max(lengths) == min(lengths)

            for j, line in enumerate(lines):
                for i, ch in enumerate(line):
                    self.grid[complex(i, j)] = ch

    @property
    def nrows(self):
        rows = max([int(x.imag) for x in self.grid])
        return rows + 1

    @property
    def ncolumns(self):
        cols = max([int(x.real) for x in self.grid])
        return cols + 1

    def __repr__(self):
        repr_ = ""
        for j in range(self.nrows):
            for i in range(self.ncolumns):
                repr_ += self.grid[complex(i, j)]
            repr_ += "\n"
        return repr_

    def iter_window(self, column_span, row_span, join=False):
        for row_index in range(self.nrows - row_span + 1):
            for column_index in range(self.ncolumns - column_span + 1):
                start_pos = complex(column_index, row_index)
                new_grid = {}
                for j in range(row_span):
                    for i in range(column_span):
                        pos = complex(i, j)
                        new_grid[pos] = self.grid[pos+start_pos]
                cg = CharGrid()
                cg.grid = new_grid
                if join:
                    yield repr(cg).replace("\n", "")
                else:
                    yield cg

    def iter_rows(self, join=False):
        return self.iter_window(self.ncolumns, 1, join)

    def iter_columns(self, join=False):
        return self.iter_window(1, self.nrows, join)

    def charlist(self):
        return self.__repr__().replace("\n", "")

    def get_neighbors(self, pos, include_direction=False):
        neighbors = {}
        n_offset = {1: "e", -1: "w", 1j: "s", -1j: "n"}
        for offset, direction in n_offset.items():
            ch = self.grid.get(pos+offset)
            if ch:
                if include_direction:
                    neighbors[(pos+offset, direction)] = ch
                else:
                    neighbors[pos+offset] = ch
        return neighbors

    def __getitem__(self, pos):
        return self.grid[pos]

    def find(self, ch):
        positions = []
        for pos in self.grid:
            if self.grid[pos] == ch:
                positions.append(pos)
        return positions

    def get_items(self, pos, direction, length=0):
        items = []
        positions = []
        next_ = pos
        while next_ in self.grid:
            items.append(self.grid[next_])
            positions.append(next_)
            next_ += direction
            if length:
                if len(items) >= length:
                    break
        return positions, items


if __name__ == "__main__":
    data = """
    1234
    5678
    9012
    """

    grid = CharGrid(data)
    print(f"{grid}")
    print(f"{grid.charlist()}")

    for col in grid.iter_columns(True):
        print(col)

    print(grid.get_neighbors(1+1j, True))
