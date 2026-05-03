from collections import deque

with open("input.txt", "r") as f:
    mas=f.readlines()
graphs=int(mas[0])
if graphs<=0:
    print("неположительное кол-во графов")
    exit()

def topolog(g, n):
    '''
    в данной функции определяется наличие цикла в графе. 
    функция получает граф (его список смежности) и количество вершин в графе.
    если цикл есть, то функция возвращает True, иначе False.
    '''
    countt=[0]*n
    for u in range(n):
        for v in g[u]:
            countt[v]+=1
    queue=deque() 
    udalen=0
    for i in range(n):
        if countt[i]==0:
            queue.append(i)
    while queue:
        u=queue.popleft()
        udalen+=1
        for v in g[u]:
            countt[v]-=1
            if countt[v]==0:
                queue.append(v)
    if udalen==n:
        return False
    else:
        return True

count=0
num=1
for i in range(graphs):
    n,k=map(int, mas[num].split())
    if n<0 or k<0:
        print("отрицательное кол-во вершин или ребер")
        exit()
    num+=1
    g=[[] for j in range(n)]
    for j in range(k):
        a,b=map(int,mas[num].split())
        g[a].append(b)
        num+=1
    if topolog(g, n):
        count+=1
print(count)