def find(i):
        if i != parent[i]:
            parent[i] = find(parent[i])
        return parent[i]

def union(a, b):
    idA = find(a)
    idB = find(b)
    if idA==idB:
        return 
    if rank[idA] > rank[idB]:
        parent[idB] = idA
        rank[idA] += rank[idB]
        rank[idB]=0
        find(b)
    else:
        parent[idA] = idB
        rank[idB] += rank[idA]
        rank[idA]=0
        find(a)

self.parent = [x for x in range(n)]
self.rank = [0]*(n)
