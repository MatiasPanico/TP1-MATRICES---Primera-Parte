# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:40:28 2023

@author: matia
"""
#jrr
class MyArray1:
    
    """ MyArray1 es un objeto capaz de operar con matrices. Puede crearlas,
    modificarlas y operar con ellas, además de resaltar un elemento, columna
    o fila específica"""
    
    def __init__(self, filas, columnas, elementos, by_row = bool):
        """
        La función "__init__" crea las instancias de la clase. En este caso,
        delimita el numero de filas, columnas, elementos y modo de lectura de la 
        matriz. A su vez, contiene un condicional que chequea si la cantidad de
        elementos coincide con las dimenciones de la matriz. En caso contrario, 
        se para la lectura del código imprimiendo un mensaje de error.

        """
        if len(elementos) != (filas * columnas):
            print("La cantidad de elementos debe coincidir con la cantidad de filas por cantidad de columnas.")
        else:
            self.elems = elementos
            self.r = filas
            self.c = columnas
            self.by_row = by_row

    def get_pos(self, j, k):
        """
        Esta función determina matemáticamente en qué posición (índice de la lista)
        está dicho elemento según sus coordenadas j y k, con el condicional de que
        si estos parámetros no se encuentran dentro de 0 y self.c y self.r, se para
        la lectura del código.

        """
        if 0 < k <= self.c and 0 < j <= self.r: 
            p = k + (j-1)*self.c
            #Se le resta 1 a p para poder obtener el índice 0. De esta manera, una coordenada (4, 4), si bien es el elemento numero 16 de la matriz, se marca su índice como 15. 
            return p-1
        
    def get_coords(self, p):
        """
        Por el contrario a "get_pos", "get_coords" devuelve las coordenadas de un 
        elemento segun su posición u índice a través de un cálculo matemático. Luego
        suma 1 a los parámetros j y k para que el código no devuelva coordenadas (0, 0).
        Así, una matriz 3*3 , en lugar de ir desde el (0, 0) hasta el (2, 2), va del
        (1, 1), hasta el (3, 3), como se acostumbra escribir matemáticamente.

        """
        if 0 <= p < self.r*self.c:
            j = (p // self.c)
            k = (p - j*self.c)
            j += 1
            k += 1
            return j, k

    def switch(self):
        """
       La funcion switch cambia el modo de leer la matriz. Por default se lee a la 
       matriz por filas, pero cada vez que switch sea usada se cambiara a por columna 
       o fila, según corresponda. Esto sirve para futuras funciones cuando el parámetro
       "by_row sea falso."

        """
        matriz_cambiada = []
        if self.by_row == True:
            for k in range(self.c):
                matriz_cambiada.extend([self.elems[j*self.c+k] for j in range(self.r)])
        else:
            for j in range(self.r):
                matriz_cambiada.extend(self.elems[j*self.c:(j+1)*self.c])
        return (MyArray1(self.r, self.c, matriz_cambiada, not self.by_row))   
    
    def get_row(self, j):
        """
       Esta función devuelve una nueva lista en donde estaría compuesta la fila numero
       x de la matriz. Para ello, se crea una lista vacía a la que se le agregan 
       elementos de la matriz original con la función .append(). Estos elementos
       estan delimitados por 2 variables, que sería el primer elemento de la fila
       y el último elelemto de la fila, los cuales se obtienen a través de un cálculo
       matemático.

        """
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            row = []
            row.append(self.elems[pedlf: uedlf])
            return row
        else:
            print("error")
    
    def get_col(self, k):
        """
        Esta función devuelve una lista con la columna de la matriz señalada por el
        parámetro k a través de un for loop de la cantidad de elementos sumando la i
        cada self.c cantidad de columnas, para luego ir agregando los elementos con su  
        apropiado índice a una lista vacía

        """
        if 0 < k <= self.c:   
            col = []
            for i in range(0, len(self.elems), self.c):
                col.append(self.elems[i+k-1])
            return col
   
    def get_elem(self, j, k):
        """
        La función "get_elem" devuelve el valor del número que se encuentra en las
        coordenadas marcadas por los parámetros j y k. Entonces, la función repite
        la metodología de "get_pos", pero en lugar de devolver la posición, devuelve
        el valor del elemento que se encuentra en el índice de la posición dentro de
        la lista en la que está contenida la matriz inicial.

        """
        if 0 < k <= self.c and 0 < j <= self.r: 
            p = k + (j-1)*self.c
            return self.elems[p-1]
  
    def del_row(self, j):
        """
        "del_row" utiliza las mismas cuentas de "get_row" para saber desde qué 
        elemento hasta qué elemento tiene que eliminar, y en lugar de agregarlos
        a una lista vacía, se agregan todos los demás elementos de la lista inicial
        para generar la nueva matriz sin esa fila. La función devuelve un objeto.

        """
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            matriz = self.elems[0: pedlf] + self.elems[uedlf:]
            return MyArray1(self.r, self.c, matriz, self.by_row)
  
    def del_col(self, k):  
        """
        A diferencia de "del_row", esta función utiliza un for loop para identificar
        a los elementos de una columna de parámetro k, y los saca, con el .pop(), de la nueva lista
        generada. Al igual que la función anterior, ésta también devuelve un objeto.

        """
        if 0 < k <= self.c:
            matriz = []
            r = 1
            for i in range(0, len(self.elems), self.c):
                matriz += self.elems[i: i+self.c]
                matriz.pop(i+k-r)
                r += 1
            return MyArray1(self.r, self.c, matriz, self.by_row)  

    def swap_rows(self, j, k): 
        """
        "swap_rows" devuelve un objeto en donde esta contenida la matriz de manera
        que las filas indicadas en los parámetros j y k intecrambien su posición.
        La función utiliza "get_row" para conseguir una lista de cada fila, y con 
        el .extend() agrega los elementos a una nueva matriz, y con el for loop
        detecta si a la lista vacía (variable "matriz") le debe agregar los elementos
        de qué fila, teniendo en cuenta también las filas que no se desean intercambiar, 
        a través de if, elif y else.

        """
        if 0 < j <= self.r or 0 < k <= self.r:
            fila = 1
            for i in range(1, self.r+1):
                if fila == j:
                    fj = self.get_row(i)
                if fila == k:
                    fk = self.get_row(i)
                fila += 1
            matriz = []
            fila2 = 1
            for i in range(0, len(self.elems), self.c):
                if fila2 == j:
                    for e in fk:
                        matriz.extend(e)
                elif fila2 == k:
                    for e in fj:
                        matriz.extend(e)
                else:
                    for e in self.elems[i: i+self.c]:
                        matriz.append(e)
                fila2 += 1
            return MyArray1(self.r, self.c, matriz, self.by_row)
     

    def swap_cols(self, l, m):
        """
        Esta función sigue la misma metodología y cumple la misma función que la
        anteriór, con la diferencia de que en lugar de intercambiar filas, se 
        intercambian columnas. Se llama a la función "get_col" para obtener las
        columnas, y la función devuelve un objeto.

        """
        if 0 < l <= self.c and 0 < m <= self.c:
            coll = self.get_col(l)
            colm = self.get_col(m)
            matriz = []
            contador = 1
            for i in range(0, len(self.elems), self.r):
                if contador == l:
                    matriz.extend(colm)
                elif contador == m:
                    matriz.extend(coll)
                else:
                    matriz.extend(self.elems[i: i+self.r])
                contador += 1
            return MyArray1(self.r, self.c, matriz, self.by_row)
    
    def scale_row(self, j, x):
        """
        Esta función utiliza las mismas cuentas que "get_row" para obtener el primer
        y último elemento de la fila que se desea escalar, y devuelve un objeto con
        la misma matriz, pero la fila j es multiplicada por el número x.

        """
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            fila = self.elems[pedlf:uedlf]
            fila_escalada = []
            for i in fila:
                fila_escalada.append(i*x)
            matriz = self.elems[:pedlf] + fila_escalada + self.elems[uedlf:]
        else:
            matriz = print("error")
        return MyArray1(self.r, self.c, matriz, self.by_row)
                
    def scale_col(self, k, y):
        """
        Esta función utiliza las mismas cuentas que "get_col" para obtener el primer
        y último elemento de la columna que se desea escalar, y devuelve un objeto con
        la misma matriz, pero la columna k es multiplicada por el número y.

        """
        if 0 < k <= self.c:
            columna = []
            for i in range(0, len(self.elems), self.c):
                columna.append(self.elems[i+k-1])
            columna_escalada = []
            for i in columna:
                columna_escalada.append(int(i) * y)
            contador_columna = 0
            matriz = []
            for i in range(0, len(self.elems), self.c):
                matriz += self.elems[i:i+k-1] + [columna_escalada[contador_columna]] + self.elems[i+k:i+self.c]
                contador_columna += 1
            return MyArray1(self.r, self.c, matriz, self.by_row)
        
    def transpose(self):
        """
       La función "transpose" utiliza "switch", pero no sólo cambia la lectura de
       la matriz, sino que modifica su instancia cambiando la lista de elementos
       e intercambiando el numero de filas por columnas.

        """
        self.elems = self.switch().elems
        rows, columns = self.r , self.c
        self.r, self.c = columns, rows
        actualizacion = print("Ahora se cambiaron las filas por las columnas")
        return actualizacion

    def flip_rows(self):
        """
       La función "flip_rows" invierte las filas de una matrix x*x. Por ejemplo, si
       una matriz tiene 4 filas, la primera se intercambia con la cuarte, y la
       segunda con la tercera. En caso de tener filas impares, la del medio no se
       mantinene en su lugar. Para esto la función usa un for loop que agarra 
       de a filas y llama a la función "swap_rows" para que las intercambie, y 
       repite el proceso la cantidad de veces que sea necesario según la cantidad
       de filas.

        """
        #Creo una instancia copiando los datos del __init__ para usar como parámetro en el for loop
        new_i = MyArray1(self.r, self.c, self.elems.copy(), self.by_row)
        for i in range(1, (new_i.r//2)+1):
            #Llamo a la función swap_rows con parámetros de la primera y última fila dentro de self.elems.copy() para que se intercambien
            new_i.elems = new_i.swap_rows(i, new_i.r-i+1).elems
        return new_i
    
    def flip_cols(self):
        """
        La función "flip_cols" usa la misma metodología que "flip_rows", pero llama 
        a "swap_cols", y en lugar de tomar como parámetro la cantidad de filas de 
        la clase, toma la cantidad de columnas.

        """
        new_i = MyArray1(self.r, self.c, self.elems.copy(), self.by_row)
        for i in range(1, (new_i.c//2)+1):
            new_i.elems = new_i.swap_cols(i, new_i.c-i+1).elems
        return new_i              
            
    def det(self, matriz_i = None, fila = None, columnas = None):
        """
        Esta función "det" devuelve la determinante de la matriz, con el condicional
        de que sea cuadrada, es decir, filas = columnas. Lo que hace es calcular los
        determinantes de matrices 2x2 con su fórmula, y de manera recursiva logra
        simplificar matrices 3x3 a 2x2, tomando la primera fila como multiplicadores
        de las matrices 2x2 formadas con la segunda y tercera fila. La recursión 
        permite que se repita la operación para poder realizar esto con matrices de
        x*x.
        
        """
        if matriz_i == None:
            matriz, columnas, fila = MyArray1(self.r, self.c, self.elems, self.by_row), self.c, self.r
        #Condicional
        if self.r != self.c:
            return print("error: la matriz debe ser cuadrada para calcular su determinante")
        #Caso base matriz 2x2
        if self.r == 2:
            determinante = self.elems[0] * self.elems[2] - self.elems[1] * self.elems[3]
        #Caso matrices más grandes    
        else:
            fila1 = self.get_row(1)
            determinante = 0
            contador_columna = 0
            for i in range(1, self.c+1):
                e = fila1[i-1]
                matriz = []
                for i in range(2, self.r+1):
                    fila = self.get_row(i)
                    if len(fila) > 1:
                        fila.pop(contador_columna) 
                        matriz.extend(fila)
                    elif len(fila) <= 1:
                        break
                contador_columna += 1
                #En esta línea me tira un error, de que toma los parametros fila y columna como "int" y no les puedo aplicar una resta (el -1). No se por qué pasa esto.
                determinante += e * ((-1)**(1+contador_columna)) * self.det(matriz, fila-1, columnas-1)                
        return determinante
        
if __name__ == "__main__":
       matriz = MyArray1(3, 3, [2, 4, 8, 5, 3, 1, 0, 7, 9], True)  
       #Tampoco llegué a hacer entender del todo MyArray2 como para ponerlo en esta instancia de entrega.