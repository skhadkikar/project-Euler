
triangle = [] # the actual graph to traverse
with open('triangle.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        lst = line.split(' ')
        lst[-1] = lst[-1].rstrip()
        triangle.append([int(x) for x in lst])

distances = [[-1 for _ in range(i+1)] for i in range(100)] # the distance to each of the vertices
distances[0][0] = triangle[0][0] # start at source, set all other distances to MIN

# run the algo in topological order where i := depth and j:= across
for i in range(99):
    for j in range(i+1): # for every vertex in triangle (i,j)
        # consider all adjacent vertices, (i+1,j) and (i+1,j+1)
        if distances[i][j] + triangle[i+1][j] > distances[i+1][j]:
            distances[i+1][j] = distances[i][j] + triangle[i+1][j]
        if distances[i][j] + triangle[i+1][j+1] > distances[i+1][j+1]:
            distances[i+1][j+1] = distances[i][j] + triangle[i+1][j+1]

# recursive relation T[adjacent] = max{ new distance to adjacent, previous distance to adjacent
# every node will have the max distance possible to it by the time that node is considered
# because of order considered, where every node previous is considered before order next
# no cycles in graph so this holds

print(max(distances[99]))