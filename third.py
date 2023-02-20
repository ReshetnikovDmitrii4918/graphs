import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import igraph
from collections import Counter
p = []
sred = []
q = 0
p.append(0)
while q < 1:
    q = q + 0.05
    p.append(round(q,2))
# проход по всем данным
for g in p:
    list_comp = []
    for j in range(10):
        N = 100
        matrix = []
        for i in range(N): #создаем нулевую матрицу смежности
            matrix.append([1]*N)
        n_matrix = []
        for i in range(N):
            n_matrix.append(str(i))
        # заполнение матрицы смежности
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if random.random() < 1-g:
                    matrix[row][col] = 0
                    matrix[col][row] = 0
                if row == col:
                    matrix[row][col] = 0        
#пункт 3, список ребер
        global lst1
        lst1 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    lst1.append([(i, j), matrix[i][j]])
        #пункт 4, визуализация графа
        global lst
        lst = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    if n_matrix[i]!=n_matrix[j]:
                        lst.append([n_matrix[i], n_matrix[j], matrix[i][j]])
                    else:
                        lst.append([n_matrix[j], n_matrix[i], matrix[i][j]])
        '''DG = nx.Graph()  # Создание объекта пустого графа без ребер и узлов (неориентрованного графа)
        #DG = nx.dodecahedral_graph()
        DG.add_nodes_from(n_matrix)
        DG.add_weighted_edges_from(lst)  # Добавление ребер в виде списка с указанием веса
        pos = nx.random_layout(DG)  # Определение карты расположения узлов
        nx.draw(DG, pos=pos,
                node_color='lightgreen',
                with_labels=True,
                node_size=300)'''
        #plt.show()
        # Поиск спектра
        stepen = []
        v = []
        q = set()
        qw = 0
        qw1 = 0
        v_1 = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    stepen.append(sum(matrix[i]) + sum(matrix[j]))
        for i in range(len(stepen)):
            qw = len(q)
            q.add(stepen[i])
            qw1 = len(q)
            if qw != qw1:
                v.append(stepen.count(stepen[i]))
                v_1.append(stepen[i])
        '''plt.bar(v, v_1)
        plt.xlabel('Степень')
        plt.ylabel('Кол-во вершин')
        plt.grid(True)'''
        #plt.show()
        G = igraph.Graph(directed=False)  # создание ориентированного графа
        G.add_vertices(N)  # добавление вершин в граф
        G.vs["label"] = n_matrix  # подписи вершин
        G.add_edges(lst1[i][0] for i in range(len(lst1)))  # добавление ребер в граф
        # нахождение компонентов
        komp = (G.components(mode="strong"))
        # количество компонентов в графе
        komp = komp._len
        list_comp.append(komp)
    list_comp = sum(list_comp)
    sred.append(round((list_comp / 10)))
    print(p)
    print(sred)
# создание графика зависимости
plt.plot(p, sred, marker='o')
plt.xlabel('Вероятность')
plt.ylabel('Среднее значение компонентов')
plt.grid(True)
plt.show()
