def  gridTab(m,n):
    gridArr=[[0]*(m+1)]*(n+1)
    gridArr[1][1]=1
    for i in range(m):
        for x in range(n):
            current=gridArr[i][x]
            if i+1 <=m:
                gridArr[(i+1)][x]+=current
            if x+1 <=n:
                gridArr[i][(x+1)]+=current
    return gridArr
print(gridTab(3,3))
