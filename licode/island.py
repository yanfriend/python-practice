def count_islands(matrix):
    if not matrix: return 0

    rows=len(matrix); cols=len(matrix[0]) if matrix else 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0: continue
            if i>0 and matrix[i-1][j]:
                matrix[i][j]=matrix[i-1][j]
            if j>0 and matrix[i][j-1]:
                matrix[i][j]=matrix[i][j-1] if matrix[i][j]==1 else min(matrix[i][j],matrix[i][j-1])
            if matrix[i][j]==1:
                matrix[i][j]=i*cols+j+2

        for j in range(cols-2,-1,-1):
            if matrix[i][j]==0: continue
            if matrix[i][j+1]: matrix[i][j]=min(matrix[i][j],matrix[i][j+1])

    cnt=0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==i*cols+j+2 and matrix[i][j]:
                cnt+=1
    return matrix, cnt


def transform(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def updown(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    return [[matrix[rows-1-i][cols-j-1] for i in range(rows)] for j in range(cols)]

# test below
matrix=[
    [1,0,0,1,0],
    [0,1,1,1,1],
    [1,0,0,0,1]
]
print count_islands(matrix) # 3

matrix=[
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]
print min(count_islands(matrix),count_islands(updown(matrix)))  # 1

matrix=[
[1, 0, 1, 1, 1],
[1, 0, 1, 0, 1],
[1, 1, 1, 0, 1]
]
print min(count_islands(matrix),count_islands(updown(matrix))) # 1
