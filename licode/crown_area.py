def crow_area(province):
    """

    :param province: list of string
    :return: int, total area with crown
    """
    ans = 0
    province = [s.split(' ') for s in province]

    def dfs(i, j, color):
        if not (0 <= i < len(province) and 0 <= j < len(province[0])): return 0, 0
        if province[i][j] == '#' or province[i][j][0] != color: return 0, 0

        crown = int(province[i][j][1])
        area = 1
        province[i][j] = '#'
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            a1, c1 = dfs(x, y, color)
            area += a1
            crown += c1
        return area, crown

    for i in range(len(province)):
        for j in range(len(province[0])):
            if province[i][j] != '#':
                area, crown = dfs(i, j, province[i][j][0])
                ans += area * crown
    return ans


print crow_area([
    'Y0 B1 B1 B0 G2',
    'B0 B0 G0 G0 G0',
    'B0 B1 G0 R2 R1',
    'Y0 G0 Y1 Y0 Y0',
    'R0 R2 R0 Y1 G0',
])

print crow_area([
    "G0 W1 W1 W0 P2",
    "W0 W0 F0 F0 F0",
    "W0 W1 F0 S2 S1",
    "G0 X0 G1 G0 G0",
    "S0 M2 M0 G1 F0"
])  # 41
