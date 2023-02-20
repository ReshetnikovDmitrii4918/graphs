import networkx as nx
from matplotlib import pyplot as plt
import random
import time
#m = int(input('Введите число: '))
t = []
f = []
for m in range(2, 10):
   matrix = []
   for i in range(m*m): #создаем нулевую матрицу
      matrix.append([0]*m*m)
   v = []
   for i in range(len(matrix)): #вершины(индексы)
         v.append(i)
   for i in range(len(v)):
      r = v[i]//m
      c = v[i]%m
      if (r%4 == 0 and c%2 == 1) or (r%4 == 2 and c%2 == 0):
         if r>0:
            matrix[v[i]][v[i]-m] = matrix[v[i]-m][v[i]] = 1
         if r<(m-1) and c<(m-1):
            matrix[v[i]][v[i]+m+1] = matrix[v[i]+m+1][v[i]] = 1
         if r<(m-1) and c>0:
            matrix[v[i]][v[i] + m - 1] = matrix[v[i] + m - 1][v[i]] = 1
   i = 0
   j = 0
   s=[]
   z = []
   matrix_new = []
   while i != ((m*m)-1): #цикл удаления не задействованных вершин
         if sum(matrix[i]) >= 2:
            matrix_new.append(matrix[i])
            z.append(i)
         else:
            s.append(i)
         i = i+1
   matrix = []
   l = []
   #print(*matrix_new, sep='\n')
   for i in range(len(matrix_new)):
      for j in range(len(matrix_new[i])):
         if j not in s:
            l.append(matrix_new[i][j])
      matrix.append(l)
      l = []
   for i in range(len(matrix)):
      for j in range(len(matrix)):
         if matrix[i][j] != 0:
            matrix[i][j] = random.randint(2,27)
   print(matrix)
   lst = []
   for i in range(len(matrix)):
      for j in range(len(matrix)):
         if matrix[i][j] != 0:
            if z[i] != z[j]:
               lst.append([z[i], z[j], matrix[i][j]])
            else:
               lst.append([z[j], z[i], matrix[i][j]])
   ################################# Старт работы алгоритма
   def alg():
      q = []
      r = []
      s = set()
      w = 0
      for i in range(len(lst)):
         q.append(lst[i][2])  # сохраняем в список только значения весов ребер
      while len(q) != 0:  # в данном цикле распологаем все ребра в порядке возрастания
         w = min(q)
         for i in range(len(lst)):
            if w == lst[i][2]:
               r.append(lst[i])
         q.remove(w)
      for i in range(len(r)):
         s.add(r[i][0])  # добавляем вершины в множество
         s.add(r[i][1])
         q.append(r[i])
         if len(s) == len(z):  # если все вершины добавлены в множество
            break
   start_time = time.time()
   for k in range(10 ** 6):
      alg()
   average_time = time.time() - start_time
   t.append(average_time / 10 ** 6)
   f.append(m)
   # Построение графа
plt.figure(figsize=(12, 5)); # если нужно задать размер картинки
plt.plot(f, t)
plt.show()
