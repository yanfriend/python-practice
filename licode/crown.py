class Kingdom(object):
    def __init__(self, lands):
        self.lands = []
        for land in lands:
            self.lands.append(land.split(' '))

    def calculateScore(self):
        row = len(self.lands)
        col = len(self.lands[0])

        def helper(i, j, org):
            if not (0 <= i < row and 0 <= j < col): return 0, 0  # error 1, 0,i,len, order!!
            if self.lands[i][j] == '##' or org == '##': return 0, 0
            if self.lands[i][j][0] != org[0]: return 0, 0

            area = 1;
            crown = int(self.lands[i][j][1])
            delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
            self.lands[i][j] = '##'
            for dx, dy in delta:
                newx = i + dx;
                newy = j + dy
                newarea, newcrown = helper(newx, newy, org)
                area += newarea
                crown += newcrown
            return area, crown

        ret = 0
        for i in range(row):
            for j in range(col):
                area, crown = helper(i, j, self.lands[i][j])
                ret += area * crown
        return ret


kingdom = Kingdom([
    "G0 W1 W1 W0 P2",
    "W0 W0 F0 F0 F0",
    "W0 W1 F0 S2 S1",
    "G0 X0 G1 G0 G0",
    "S0 M2 M0 G1 F0"
]
) # 41

# kingdom=Kingdom([
#   "W1 W1",
#   "W0 F1",
# ]
# )

print kingdom.calculateScore()
