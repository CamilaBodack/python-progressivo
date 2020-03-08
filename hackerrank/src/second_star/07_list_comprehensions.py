x = int(input())
y = int(input())
z = int(input())
n = int(input())

def list_comprehesion(x, y, z, n):

    lista = []
    for i in range( x + 1):
        for j in range( y + 1):
            for k in range (z +1):
                if ( ( i + j + k) != n ):
                    lista.append([i,j,k]) 
    print(lista)

list_comprehesion(x, y, z, n) 