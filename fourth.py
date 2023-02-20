import random
#from progress.bar import IncrementalBar
import matplotlib.pyplot as plt
import networkx as nx

def gen_matrix(len_m):  # содание матрицы смежности
    matrix = []
    flag = False
    for i in range(len_m):
        row = []
        for j in range(len_m):
            if i == j:
                row.append(0)
                flag = True
            elif flag:
                row.append(random.randint(1, 9))
            else:
                row.append(0)

        flag = False
        matrix.append(row)
        row = []

    flag = True

    for i in range(len_m):
        for j in range(len_m):
            if i == j:
                flag = False
            if flag:
                matrix[i][j] = matrix[j][i]
        flag = True
    return matrix


def paint_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")  # вывод матрицы смежности
        print(" ")





def search_best_loop(matrix, meadian_number):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i - j == 1:
                print(j, "->", i, ":", matrix[i][j])
            elif j == 9 and i == 0:
                print(j, "->", i, ":", matrix[i][j])
    nodes = [i for i in range(len(matrix))]
    sum_vert = 0




def generate_chain(iterable, r=None):

    # generate_chain(013,3) --> 012 021 102 120 201 210...
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):

            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:

            return

def summ_loop(nums,matrix):
    # nums = 0132
    summ = 0
    for i in range(len(nums) - 1):
        x = nums[i]
        j = nums[i + 1]
        summ += matrix[x][j]
    summ += matrix[len(nums)-1][nums[0]]
    return summ


def lab2_1(matrix,n_matrix,result_nodes):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                if n_matrix[i]!=n_matrix[j]:
                    lst.append([n_matrix[i], n_matrix[j], matrix[i][j]])
                else:
                    lst.append([n_matrix[j], n_matrix[i], matrix[i][j]])
    print(len(lst))
    DG = nx.Graph() #Создание объекта пустого графа без ребер и узлов (неориентрованного графа)
    #DG = nx.DiGraph(directed=True) # Создание объекта пустого ориентированного графа
    DG.add_nodes_from(n_matrix)
    DG.add_weighted_edges_from(lst) #Добавление ребер в виде списка с указанием веса
    #Построение графа
    plt.figure(figsize=(10, 10))
    pos = nx.shell_layout(DG) #Определение карты расположения узлов
    nx.draw(DG, node_size=500, pos=pos, with_labels=True, label="graf", edge_color = 'r') #Создание изображения графа
    nx.draw_networkx_edge_labels(DG, pos)
    plt.show() #Отображение графа

def main():
    len_m = 10
    matrix = gen_matrix(len_m)
    #matrix = [
    #     [0, 7, 5, 8, 1, 2, 3, 4, 5, 2],
    #     [7, 0, 7, 5, 2, 3, 5, 7, 9, 4],
    #     [5, 7, 0, 2, 3, 6, 9, 2, 6, 6],
    #     [8, 5, 2, 0, 3, 5, 2, 1, 8, 1],
    #     [1, 2, 3, 3, 0, 5, 6, 2, 7, 9],
    #     [2, 3, 6, 5, 5, 0, 4, 4, 1, 3],
    #     [3, 5, 9, 2, 6, 4, 0, 5, 2, 6],
    #     [4, 7, 2, 1, 2, 4, 5, 0, 7, 3],
    #     [5, 9, 6, 8, 7, 1, 2, 7, 0, 1],
    #     [2, 4, 6, 1, 9, 3, 6, 3, 1, 0]
    # ]
    #paint_matrix(matrix)

    min = 100000
    result = 0
    result_nodes = ()
    for i in generate_chain([i for i in range(0, len(matrix))], len_m):

        
        result = summ_loop(i,matrix)
        if result < min:
            min = result
            result_nodes = i
        #print(i,":",result)
    print(result_nodes)
    print("")
    print(result_nodes,":",min)
    #90
    lab2_1(matrix,[ str(i) for i in range(len(matrix))],result_nodes)
main()
