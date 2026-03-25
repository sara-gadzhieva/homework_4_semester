f=open("input.txt")
mas=[]
for x in f.read().split():
    mas.append(float(x))
f.close()

print("кол-во:", len(mas))
print("сумма:", sum(mas))
print("минимум:", min(mas))
print("максимум:", max(mas))
print("ср. ар.:", sum(mas)/len(mas))
