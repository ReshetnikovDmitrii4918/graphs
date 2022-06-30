import matplotlib.pyplot as plt
import networkx as nx
import time
import numpy as np
from sys import getsizeof
matrix = [[0, 6, 6, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 4, 0],
   [0, 0, 0, 0, 4, 0, 0],
   [0, 10, 10, 0, 10, 10, 0],
   [0, 0, 0, 0, 0, 2, 4],
   [0, 0, 0, 0, 0, 0, 4],
   [0, 0, 0, 0, 0, 0, 0]]
n_matrix = ['Assistant',"Secretary1","Secretary2","Chief","Manager1","Manager2","Worker"]
#пункт 2, вывод матрицы смежности в явном виде
def lab1_1():
   print('Вывод матрицы в явном виде:')
   print(*n_matrix)
   tm = -1
   for i in n_matrix:
      tm += 1
      for j in matrix[tm]:
         if len(str(j))>1:
            print(str(j) ,end="        ")
         else:
            print(str(j) ,end="         ")
      print(i)
#пункт 3, список ребер
def lab1_2():
   global lst
   lst = []
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
         if matrix[i][j] != 0:
            lst += [[tuple([i, j]), matrix[i][j]]]
   print(lst)
#пункт 4, визуализация графа
def lab1_3():
   #G = nx.Graph() #Создание объекта пустого графа без ребер и узлов
   DG = nx.DiGraph(directed=True) # Создание объекта пустого ориентированного графа
   DG.add_nodes_from(['Assistant', 'Secretary1', 'Secretary2', 'Chief', 'Manager1', 'Manager2',
   'Worker'])
   DG.add_weighted_edges_from(lst) #Добавление ребер в виде списка с указанием веса
   #Построение графа
   plt.figure(figsize=(25, 25))
   pos = nx.planar_layout(DG) #Определение карты расположения узлов
   nx.draw(DG, node_size=500, pos=pos, with_labels=True, label="graf", edge_color = "r") #Создание изображения графа
   nx.draw_networkx_edge_labels(DG, pos)
   plt.show() #Отображение графа
#пункт 5, Написать подпрограмму, позволяющую представить граф в виде массива записей
def lab1_4():
   name_dict = {0:'Assistant', 1:'Secretary1', 2: 'Secretary2', 3: 'Chief', 4: 'Manager1', 5: 'Manager2', 6: 'Worker'}
   global massiv_zapisei
   massiv_zapisei = []
   count = [0 for i in range(len(matrix))]
   num = [[] for i in range(len(matrix))]
   global neigh_num
   neigh_num = [[] for i in range(len(matrix))]
   children = [[] for i in range(len(matrix))]
   global weights
   weights = [0 for i in range(len(matrix))]
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
         if matrix[i][j] != 0:
            count[i] += 1
            count[j] += 1
            weights[i] += matrix[i][j]
            weights[j] += matrix[i][j]
            num[j] += [i]
            num[i] += [j]
            children[i] += [j]
   neigh_count = [i for i in count]
   for i in range(len(neigh_num)):
      neigh_num[i] += [j for j in num[i]]
   for i in range(len(matrix)):
      massiv_zapisei += [{'Номер вершины': i, 'Имя вершины':name_dict[i],'Количество соседей': neigh_count[i],
      'Номера соседей': neigh_num[i],
      'Дети': children[i], 'Сумма веса':weights[i]}]
   print('Пункт 5')
   print(massiv_zapisei)
#пункт 6, написать подпрограммы поиска и вывода на экран
#соседи, найденные по матрице смежности
def matrix_smeznost_neighbours():
   a = int(input('Введите номер вершины для поиска соседей: '))
   start_time = time.time()
   for i in range(10 ** 6):
      neigh_count = []
      for j in range(len(matrix[a])): #цикл внутри строки матрицы, поиск соседей по горизонтали
         if matrix[a][j] != 0:
            neigh_count.append(j)
      for j in range(len(matrix)): # поиск соседей по вертикали
         if matrix[j][a] != 0:
            neigh_count.append(j)
   average_time = time.time() - start_time
   print('Соседи:', neigh_count)
   print('Время выполнения подпрограммы:', average_time)
   print('Среднее время выполнения подпрограммы:', average_time / 10 ** 6)
#соседи, найденные по списку ребер
def spisok_reber_neighbours():
   a = int(input('Введите номер вершины для поиска соседей: '))
   start_time = time.time()
   for j in range(10 ** 6):
      neigh_count = []
      for i in lst:
         if a in i[0] and a == i[0][0]: #если внутри кортежа есть номер вершины и он первый элемент, то соседом является второй элемент, его мы и добавляем в список
            neigh_count.append(i[0][1])
         elif a in i[0] and a == i[0][1]: #соответственно наоборот
            neigh_count.append(i[0][0])
   average_time = time.time() - start_time
   print('Соседи: ', neigh_count)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#соседи, найденные по массиву записей
def massiv_zapisey_neighbours(neigh_num):
   a = int(input('Введите номер вершины (данное действие происходит для поиска соседей): '))
   start_time = time.time()
   for j in range(10 ** 6):
      b = neigh_num[a] #искомое количество соседей это один из параметров массива записи
      break
   print('Соседи: ', b)
   average_time = time.time() - start_time
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#определение цепи по матрице смежности
def matrix_smeznost_tsep():
   a = input('Введите последовательность:').split()
   start_time = time.time()
   for j in range(10 ** 6):
      for i in range(len(a) - 1):
         if matrix[int(a[i])][int(a[i + 1])] != 0:
            b = 'Последовательность образует цепь'
         else:
            b = 'Последовательность не образует цепь'
            break
   average_time = time.time() - start_time
   print(b)
   print('Время выполнения подпрограммы:', average_time)
   print('Среднее время выполнения подпрограммы:', average_time / 10 ** 6)
#определение цепи по списку ребер
def spisok_reber_tsep():
   a = input('Введите последовательность:').split()
   start_time = time.time()
   for k in range(10 ** 6):
      for i in range(len(a) - 1):
         var = tuple([int(a[i]), int(a[i + 1])]) # если что tuple - кортеж
         for j in range(len(lst)):
            if var != lst[j][0]: #сравнение двух кортежей
               b = 'Последовательность образует цепь'
               break
            else:
               b = 'Последовательность не образует цепь'
               break
   average_time = time.time() - start_time
   print(b)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#определение цепи по массиву записей
def massiv_zapisey_tsep(massiv_zapisei):
   a = input('Введите последовательность:').split()
   start_time = time.time()
   for k in range(10 ** 6):
      for i in range(len(a) - 1):
         for j in massiv_zapisei: # проверка на то, есть ли вершина в списке детей, не повторяются ли вершины
            if int(j['Номер вершины']) == int(a[i]) and int(a[i + 1]) != int(a[i]) and int(a[i + 1]) in j['Дети']:
               b = 'Последовательность не образует цепь'
               break
            else:
               b = 'Последовательность образует цепь'
               break
   average_time = time.time() - start_time
   print(b)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#номеров вершин, сумма весов инцидентных ребер которых больше заданной величины по матрице смежности
def matrix_smeznost_sum_reber():
   a = int(input('Введите число, которое будет сравниваться с суммой весов инцедентных ребер: '))
   start_time = time.time()
   for k in range(10 ** 6):
      summ = [0 for i in range(len(matrix))]
      for i in range(len(matrix)): #происходит подсчет суммы для каждой вершины
         summ[i] += sum(matrix[i])
         for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
               summ[j] += matrix[i][j]
      summ = [i for i in range(len(summ)) if summ[i] > a] #выбирает только те вершины, у которых сумма больше
   average_time = time.time() - start_time
   print('Номера вершин: ', summ)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ',average_time / 10 ** 6)
#номеров вершин, сумма весов инцидентных ребер которых больше заданной величины по списку ребер
def spisok_reber_sum_reber(weights):
   a = int(input('Введите число, которое будет сравниваться с суммой весов инцедентных ребер: '))
   start_time = time.time()
   for k in range(10 ** 6):
      verts = []
      for i in lst:
         for j in i[0]:
            if j not in verts:
               verts += [j]
      verts = np.sort(verts)
      summ = [0 for i in range(len(verts))]
      for i in range(len(verts)):
         for j in lst:
            if verts[i] in j[0]:
               summ[i] += j[1]
      summ = [i for i in range(len(summ)) if summ[i] > a]
   average_time = time.time() - start_time
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#номеров вершин, сумма весов инцидентных ребер которых больше заданной величины по массиву записей
def massiv_zapisey_sum_reber(massiv_zapisei):
   a = int(input('Введите число, которое будет сравниваться с суммой весов инцедентных ребер: '))
   start_time = time.time()
   for j in range(10 ** 6):
      verts = []
      for i in massiv_zapisei: #выясняет у какой вершины сумма веса больше и добавляет эту сумму в список
         if i['Сумма веса'] > a:
            verts.append(i['Номер вершины'])
   average_time = time.time() - start_time
   print('Номера вершин: ', verts)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ',average_time / 10 ** 6)
#количества ребер в графе по матрице смежности
def matrix_smeznost_kolvo_reber():
   start_time = time.time()
   for k in range(10 ** 6):
      rebra = 0
      # проходимся по матрице, если значение не нулевое, то добавляем единичку в счетчик
      for i in range(len(matrix)):
         for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
               rebra = rebra + 1
   average_time = time.time() - start_time
   print('Количество ребер в графе:', rebra)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#количества ребер в графе по списку ребер
def spisok_reber_kolvo_reber():
   start_time = time.time()
   for j in range(10 ** 6):
      b = len(lst)
      break
   average_time = time.time() - start_time
   print('Количество ребер в графе: ', b)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#количества ребер в графе по массиву записей
def massiv_zapisey_kolvo_reber(massiv_zapisei):
   start_time = time.time()
   for j in range(10 ** 6):
      rebra = 0
      for i in massiv_zapisei:
         rebra += len(i['Дети'])
   average_time = time.time() - start_time
   print('Количество ребер в графе: ', rebra)
   print('Время выполнения подпрограммы: ', average_time)
   print('Среднее время выполнения подпрограммы: ', average_time / 10 ** 6)
#пункт 7, Для каждого из представлений вывести на экран размер содержащего их объекта в байтах
def lab1_6(massiv_zapisei, lst):
        print('Пункт 7')
        print('Размер матрицы смежности: ', getsizeof(matrix), 'байт')
        print('Размер списка ребер: ', getsizeof(lst), 'байт')
        print('Размер массива записей: ', getsizeof(massiv_zapisei), 'байт')
lab1_1()
lab1_2()
lab1_3() #график
lab1_4()
print("ПО МАТРИЦЕ СМЕЖНОСТИ")
matrix_smeznost_neighbours()
print("ПО СПИСКУ РЕБЕР")
spisok_reber_neighbours()
print("ПО МАССИВУ ЗАПИСЕЙ")
massiv_zapisey_neighbours(neigh_num)
print("ПО МАТРИЦЕ СМЕЖНОСТИ")
matrix_smeznost_tsep()
print("ПО СПИСКУ РЕБЕР")
spisok_reber_tsep()
print("ПО МАССИВУ ЗАПИСЕЙ")
massiv_zapisey_tsep(massiv_zapisei)
print("ПО МАТРИЦЕ СМЕЖНОСТИ")
matrix_smeznost_sum_reber()
print("ПО СПИСКУ РЕБЕР")
spisok_reber_sum_reber(weights)
print("ПО МАССИВУ ЗАПИСЕЙ")
massiv_zapisey_sum_reber(massiv_zapisei)
print("ПО МАТРИЦЕ СМЕЖНОСТИ")
matrix_smeznost_kolvo_reber()
print("ПО СПИСКУ РЕБЕР")
spisok_reber_kolvo_reber()
print("ПО МАССИВУ ЗАПИСЕЙ")
massiv_zapisey_kolvo_reber(massiv_zapisei)
lab1_6(massiv_zapisei, lst)
