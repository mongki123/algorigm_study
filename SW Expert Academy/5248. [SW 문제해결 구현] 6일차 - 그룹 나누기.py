def FindParent(parent, x):
    if parent[x] != x:
        parent[x] = FindParent(parent, parent[x]) # 경로 압축(Path Compression)
    return parent[x]

def Union(parent, left, right):
    parent_left = FindParent(parent, left)
    parent_right = FindParent(parent, right)
    if(parent_left != parent_right):
        parent[parent_right] = parent_left

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    Marr = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]

    for i in range(0, M * 2, 2):
        leftV = Marr[i]
        rightV = Marr[i + 1]
        Union(parent, leftV, rightV)
    
    result = set()
    for i in range(1, N + 1):
        result.add(FindParent(parent,i))
    
    print(f"#{test_case} {len(result)}")