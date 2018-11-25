data = [[1, 0, 2, 5, 8],
        [2, 3, 4, 7, 9],
        [3, 5, 7, 9, 9],
        [1, 2, 5, 5, 3],
        [3, 3, 5, 1, 0]]


def get_basin(x, y, grid, points_to_basins):
    lowest_coord = (x, y)

    if points_to_basins.get(lowest_coord) is not None:
        return points_to_basins[lowest_coord]

    for dx in range(max(x - 1, 0), min(x + 2, len(grid))):
        for dy in range(max(y - 1, 0), min(y + 2, len(grid[x]))):
            if grid[dx][dy] < grid[lowest_coord[0]][lowest_coord[1]]:
                lowest_coord = (dx, dy)

    if lowest_coord != (x, y):
        lowest_coord = get_basin(lowest_coord[0], lowest_coord[1], grid, points_to_basins)

    points_to_basins[(x, y)] = lowest_coord
    return lowest_coord


def count_basin_flows(grid):
    points_to_basins = {}
    basin_counts = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            basin = get_basin(x, y, grid, points_to_basins)
            basin_counts[basin] = basin_counts.get(basin, 0) + 1
    return basin_counts


print count_basin_flows(data)  # {(0, 1): 10, (3, 0): 7, (4, 4): 8}
