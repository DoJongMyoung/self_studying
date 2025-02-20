def dfs(g, i, visited):
    if (visited[i] == 1):
        return
    visited[i] = 1 # 방문하면 0에서 1로 바꿈
    print(chr(ord("A")+i),end="")
    for j in range(len(g)): # 그래프 길이 만큼 반복
        if visited[i] != 0 and g[i][j] == 1:
            dfs(g,j,visited)

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

visited = [0] * len(graph)
dfs(graph, 4, visited)