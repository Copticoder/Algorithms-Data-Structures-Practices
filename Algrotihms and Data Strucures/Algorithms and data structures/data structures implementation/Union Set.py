class unionSet():
    def __init__(self, n):
        self.parent = [x for x in range(n+1)]
        self.parent[0] = n
        self.rank = [0]*(n+1)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        idA = self.find(a)
        idB = self.find(b)
        if self.rank[idA] > self.rank[idB]:
            self.parent[b] = self.parent[a]
        elif self.rank[idA] < self.rank[idB]:
            self.parent[a] = self.parent[b]
        else:
            self.parent[a] = self.parent[b]
            self.rank[idB] += 1


newSet = unionSet(12)
# newSet.union(0,3)
# newSet.union(3,3)
# newSet.union(2,7)
# newSet.union(7,8)
# newSet.union(7,9)
# newSet.union(1,4)
# newSet.union(4,5)
# print(newSet.rank)
# print(newSet.parent)    
# for j in range(1,31):
#     newSet.union(j,2*j)
# for x in range(1,21):
#     newSet.union(x,3*x)
# for z in range(1,13):
#     newSet.union(z,5*z)
# for p in range(1,61):
#     newSet.find(p)
# print(max(newSet.rank))
# print(newSet.rank)
# print(newSet.parent)

newSet.union(2, 10)
newSet.union(7, 5)
newSet.union(6, 1)
newSet.union(3, 4)
newSet.union(5, 11)
newSet.union(7, 8)
newSet.union(7, 3)
newSet.union(12, 2)
newSet.union(9, 6)
print(newSet.find(6))
print(newSet.find(3))
print(newSet.find(11))
print(newSet.find(9))
# print(newSet.parent)

# product=1
# for i in range(len(newSet.rank)):
#     if newSet.rank[i]:
#         product*=newSet.rank[i]
# print(product)
