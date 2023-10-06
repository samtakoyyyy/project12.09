#чтение матрицы с файла
def read_matrix(file_name:str):
    fin = open(file_name,'r')
    a=[]
    for line in fin.readlines():
        a.append( [ int (x) for x in line.split(' ') ] )
    return a