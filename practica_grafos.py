# PRACTICA PROGRESIVA - GRAFOS
# Ejecuta: python practica_grafos.py
# Completa los TODO sin consultar soluciones primero.
from bases_grafos_profesor import Graph_DNP, Graph_NDNP, Graph_DP, Queue, Stack

def crear_grafo(aristas, vertices=None):
    g = Graph_DNP()
    for v in (vertices or []):
        g.add_vertex(v)
    for a,b in aristas:
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_edge(a,b)
    return g

g1 = crear_grafo([('A','B'),('A','C'),('B','D'),('C','E')])
g2 = crear_grafo([('A','B'),('A','C'),('B','D'),('C','D'),('B','E'),('E','D')])
g3 = crear_grafo([('A','B'),('B','C'),('C','A'),('C','D')])

# NIVEL 1: bases
def r1_vecinos(g, vertice):
    # Retorna lista de vecinos de un vertice
    return g.glistadj[vertice]

def r2_grado_salida(g, vertice):
    # Retorna numero de conexiones de salida
    return len(g.glistadj[vertice])

def r3_contar_aristas(g):
    # Cuenta aristas de un grafo dirigido
    count = 0
    for vertice in g.glistadj:
        count += len(g.glistadj[vertice])
    return count

# NIVEL 2: recorridos

def r4_bfs_lista(g, inicio):
    auxqueue = Queue()
    visitados = set()
    recorrido = []

    auxqueue.enqueue(inicio)
    visitados.add(inicio)

    while not auxqueue.is_empty():
        current_vertex = auxqueue.dequeue()
        recorrido.append(current_vertex)

        for vertice in g.glistadj[current_vertex]:
            if vertice not in visitados:
                auxqueue.enqueue(vertice)
                visitados.add(vertice)

    return recorrido

    

def r5_dfs_lista(g, inicio):
    # Retorna vertices en orden DFS iterativo. Usa Stack y set.
    auxstack = Stack()
    visitados = set()
    recorrido = []
    
    auxstack.push(inicio)
    visitados.add(inicio)
    
    while not auxstack.is_empty():
        current_vertex = auxstack.pop()
        recorrido.append(current_vertex)
        
        for vertice in g.glistadj[current_vertex]:
            if vertice not in visitados:
                auxstack.push(vertice)
                visitados.add(vertice)
            
    return recorrido

def r6_existe_ruta(g, origen, destino):
    # Retorna bool, sin modificar g.
    auxqueue = Queue()
    visitados = set()
    

    auxqueue.enqueue(origen)
    visitados.add(origen)

    while not auxqueue.is_empty():
        current_vertex = auxqueue.dequeue()
        if current_vertex == destino:
                    
            return True
        else:

            for vertice in g.glistadj[current_vertex]:
                if vertice not in visitados:
                    auxqueue.enqueue(vertice)
                    visitados.add(vertice)
    return False

    
    

# NIVEL 3: variaciones tipo examen
def r7_distancia_minima(g, origen, destino):
    # Devuelve numero de aristas de ruta mas corta, o -1 si no existe
    auxqueue = Queue()
    visitados = set()

    auxqueue.enqueue((origen, 0))
    visitados.add(origen)

    while not auxqueue.is_empty():
        current_vertex, distancia = auxqueue.dequeue()

        if current_vertex == destino:
            return distancia

        for vertice in g.glistadj[current_vertex]:
            if vertice not in visitados:
                auxqueue.enqueue((vertice, distancia + 1))
                visitados.add(vertice)

    return -1


def r8_rutas_simples(g, origen, destino):
    # Devuelve lista de rutas sin vertices repetidos
    rutas = []

    def dfs(actual, camino):

        if actual == destino:
            rutas.append(camino)
            return

        for vecino in g.glistadj[actual]:

            if vecino not in camino:
                dfs(vecino, camino + [vecino])

    if origen not in g.glistadj:
        return []

    if destino not in g.glistadj:
        return []

    dfs(origen, [origen])

    return rutas

def r9_rutas_sin_excluidos(g, origen, destino, excluidos):
    # Devuelve CANTIDAD de rutas simples que no pasen por excluidos
    def dfs(actual, camino):

        if actual == destino:
            return 1

        total = 0

        for vecino in g.glistadj[actual]:

            if vecino not in camino and vecino not in excluidos:

                total += dfs(vecino, camino + [vecino])

        return total

    if origen not in g.glistadj or destino not in g.glistadj:
        return 0

    if origen in excluidos or destino in excluidos:
        return 0

    return dfs(origen, [origen])


# NIVEL 4: estilo final 2024 (enunciados adaptados)
def r10_vertices_que_alcanzan_n(g, n):
    # Retorna origenes con algun destino a distancia MINIMA exactamente n
    resultado = []

    if n < 0:
        return resultado

    for origen in g.glistadj:

        auxqueue = Queue()
        visitados = set()

        auxqueue.enqueue((origen, 0))
        visitados.add(origen)

        while not auxqueue.is_empty():

            current_vertex, distancia = auxqueue.dequeue()

            if distancia == n:
                resultado.append(origen)
                break

            for vertice in g.glistadj[current_vertex]:

                if vertice not in visitados:
                    auxqueue.enqueue((vertice, distancia + 1))
                    visitados.add(vertice)

    return resultado


def r11_texto_a_grafo(s):
    # Grafo dirigido de caracteres consecutivos. Retorna (grafo, V, A).
    # Nota: la clase docente no admite bucles x->x.
    g = Graph_DNP()

    # Crear los vertices
    for caracter in s:
        g.add_vertex(caracter)

    # Crear las aristas
    for i in range(len(s) - 1):
        origen = s[i]
        destino = s[i + 1]

        g.add_edge(origen, destino)

    # Contar vertices
    V = len(g.glistadj)

    # Contar aristas
    A = 0

    for vertice in g.glistadj:
        A += len(g.glistadj[vertice])

    return g, V, A

if __name__ == '__main__':
    print('Grafo 1:'); g1.print()
    print('Grafo 2:'); g2.print()
    print('Grafo 3:'); g3.print()
    print('Empieza por r1_vecinos(g1, "A"). Resultado esperado: ["B", "C"]')
    print('Despues r2_grado_salida(g1, "A"). Esperado: 2')
    print('Despues r3_contar_aristas(g1). Esperado: 4')
    print('r4_bfs_lista(g1,"A") esperado: ["A","B","C","D","E"]')
    print('r5_dfs_lista(g1,"A") esperado: ["A","C","E","B","D"]')
    print('r6_existe_ruta(g1,"A","E") esperado: True')
    print('r7_distancia_minima(g1,"A","E") esperado: 2')
    print('r8_rutas_simples(g2,"A","D") esperado: 3 rutas')
    print('r9_rutas_sin_excluidos(g2,"A","D",{"B"}) esperado: 1')
    print('r10_vertices_que_alcanzan_n(g1,2) esperado: ["A"]')
    print('r11_texto_a_grafo("casa") esperado: V=3, A=3')
