import time
import networkx as nx
from collections import deque

with open("input.txt", "r") as f:
    mas=f.readlines()
graphs = int(mas[0])
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
graphs2=[]
for i in range(graphs):
    n,k=map(int, mas[num].split())
    if n<0 or k<0:
        print("отрицательное кол-во вершин или ребер")
        exit()
    num+=1
    g=[[] for j in range(n)]
    for j in range(k):
        a,b=map(int,mas[num].split())
        num+=1
        g[a].append(b)
    graphs2.append(g)

graphs3=[]
for g in graphs2:
    rebra=[(u, v) for u in range(len(g)) for v in g[u]]
    G=nx.DiGraph(rebra)
    G.add_nodes_from(range(len(g)))
    graphs3.append(G)

count=0
start1=time.perf_counter()
for g in graphs2:
    if topolog(g,len(g)):
        count+=1
end1=time.perf_counter()

count2=0
start2=time.perf_counter()
for G in graphs3:
    if not nx.is_directed_acyclic_graph(G):
        count2+=1
end2=time.perf_counter()

print("ответ:",count)
print("ответ существующей реализации:",count2)
print("время работы:",end1-start1)
print("время существующей реализации:",end2-start2)
