import numpy as np

if __name__ == '__main__':

    f=open("Task17.txt","r")
    lines=f.readlines()
    theInput = []

    for i in lines:
        i = i.rstrip()
        theInput.append(i)
    f.close()

    grid = np.zeros((len(theInput),len(theInput[0]),1,1))

    for i in range(len(theInput)):
        for j in range(len(theInput[0])):
            if theInput[i][j] == "#":
                grid[i][j][0][0] = 1

    grid=np.pad(grid, ((2,2), (2,2), (2, 2), (2,2)))

    for iteration in range(6):

        newGrid = np.zeros_like(grid)

        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                for k in range(1,len(grid[0][0])-1):
                    for l in range(1,len(grid[0][0][0])-1):

                        neighbours = 0

                        for v in range(i-1,i+2):
                            for u in range(j-1,j+2):
                                for w in range(k-1,k+2):
                                    for y in range(l-1,l+2):
                                    
                                        if v == i and u == j and w == k and y == l:
                                            continue

                                        if grid[v][u][w][y] == 1:
                                            neighbours += 1

                        if grid[i][j][k][l] == 1:
                            if 2 <= neighbours <= 3:
                                newGrid[i][j][k][l] = 1
                        else:
                            if neighbours == 3:
                                newGrid[i][j][k][l] = 1 

        grid = newGrid.copy()
        grid=np.pad(grid, ((1,1), (1,1), (1, 1), (1,1)), 'constant')

    print("Done")
    print(np.count_nonzero(grid == 1))
