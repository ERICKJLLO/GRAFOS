# BASES DE GRAFOS - Estructuras de Datos
# Clases tomadas del cuaderno EDD_2026_2_66__Grafos_ClaseBase.ipynb.
# Para practicar en casa: importarlas, no reescribirlas.


# ===== Grafo no dirigido, no ponderado (celda 1) =====
class Graph_NDNP:

  def __init__(self):
    self.__listadj = {}

  @property
  def glistadj(self):
    return self.__listadj

  def print(self):

    for vertex in self.__listadj:
      print("Vertex : ", vertex , "- Adyacentes :", self.__listadj[vertex] )

  def add_vertex(self, vertex):
    if vertex not in self.__listadj:
      self.__listadj[vertex] = []
      return True

    return False

  def add_edge(self, vertex1, vertex2):
    if vertex1 == vertex2:
      print("Una arista conecta a 2 vertices diferente")
      return False

    if vertex1 not in self.__listadj or vertex2 not in self.__listadj:
      raise ValueError("Error, los vertices deben estar creados")

    if vertex1 not in self.__listadj[vertex2]:
      self.__listadj[vertex2].append(vertex1)

    if vertex2 not in self.__listadj[vertex1]:
      self.__listadj[vertex1].append(vertex2)


  def delete_edge(self, vertex1, vertex2):
    if vertex1 == vertex2:
      print("Una arista conecta a 2 vertices diferentes")
      return False

    if vertex1 not in self.__listadj or vertex2 not in self.__listadj:
      raise ValueError("Error, los vertices no existen")

    if vertex1 in self.__listadj[vertex2]:
      self.__listadj[vertex2].remove(vertex1)

    if vertex2 in self.__listadj[vertex1]:
      self.__listadj[vertex1].remove(vertex2)


  def delete_vertex(self, vertex):
    if vertex in self.__listadj:
      del self.__listadj[vertex]

      for adjvertex in self.__listadj.values():
        if vertex in adjvertex:
          adjvertex.remove(vertex)


      return True

    raise ValueError("Error, el vertice a eliminar no existe")



# ===== Grafo dirigido, no ponderado (celda 4) =====
class Graph_DNP:

  def __init__(self):
    self.__listadj = {}

  @property
  def glistadj(self):
    return self.__listadj

  def print(self):

    for vertex in self.__listadj:
      print("Vertex : ", vertex , "- Adyacentes :", self.__listadj[vertex] )

  def add_vertex(self, vertex):
    if vertex not in self.__listadj:
      self.__listadj[vertex] = []
      return True

    return False

  def add_edge(self, source_vertex, target_vertex):
    if source_vertex == target_vertex:
      print("Una arista conecta a 2 vertices diferente")
      return False

    if source_vertex not in self.__listadj or target_vertex not in self.__listadj:
      raise ValueError("Error, los vertices deben estar creados")

    if target_vertex not in self.__listadj[source_vertex]:
      self.__listadj[source_vertex].append(target_vertex)



  def delete_edge(self, source_vertex, target_vertex):
    if source_vertex == target_vertex:
      print("Una arista conecta a 2 vertices diferentes")
      return False

    if source_vertex not in self.__listadj or target_vertex not in self.__listadj:
      raise ValueError("Error, los vertices no existen")

    if target_vertex in self.__listadj[source_vertex]:
      self.__listadj[source_vertex].remove(target_vertex)



  def delete_vertex(self, vertex):
    if vertex in self.__listadj:
      del self.__listadj[vertex]

      for adjvertex in self.__listadj.values():
        if vertex in adjvertex:
          adjvertex.remove(vertex)


      return True

    raise ValueError("Error, el vertice a eliminar no existe")



# ===== Grafo dirigido, ponderado (celda 7) =====
class Graph_DP:

  def __init__(self):
    self.__listadj = {}

  @property
  def glistadj(self):
    return self.__listadj

  def print(self):

    for vertex in self.__listadj:
      print("Vertex : ", vertex , "- Adyacentes :", self.__listadj[vertex] )

  def add_vertex(self, vertex):
    if vertex not in self.__listadj:
      self.__listadj[vertex] = {}
      return True

    return False

  def add_edge(self, source_vertex, target_vertex,w):
    if source_vertex == target_vertex:
      print("Una arista conecta a 2 vertices diferente")
      return False

    if source_vertex not in self.__listadj or target_vertex not in self.__listadj:
      raise ValueError("Error, los vertices deben estar creados")

    if target_vertex not in self.__listadj[source_vertex]:
      self.__listadj[source_vertex][target_vertex] = w



  def delete_edge(self, source_vertex, target_vertex):
    if source_vertex == target_vertex:
      print("Una arista conecta a 2 vertices diferentes")
      return False

    if source_vertex not in self.__listadj or target_vertex not in self.__listadj:
      raise ValueError("Error, los vertices no existen")

    if target_vertex in self.__listadj[source_vertex]:
       del self.__listadj[source_vertex][target_vertex]



  def delete_vertex(self, vertex):
    if vertex in self.__listadj:
      del self.__listadj[vertex]

      for adjvertex in self.__listadj.values():
        if vertex in adjvertex:
          del adjvertex[vertex]


      return True

    raise ValueError("Error, el vertice a eliminar no existe")



# ===== Node / LinkedList / Queue (celda 10) =====
import random

class Node:
  __slots__ = ('__value','__next')

  def __init__(self,value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("next debe ser un objeto tipo nodo ó None")
    self.__next = node

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self,newValue):
    if newValue is None:
      raise TypeError("el nuevo valor debe ser diferente de None")
    self.__value = newValue


class LinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Head debe ser un objeto tipo nodo ó None")
    self.__head = node

  @tail.setter
  def tail(self,node):
    if node is not None and not isinstance(node,Node):
      raise TypeError("Tail debe ser un objeto tipo nodo ó None")
    self.__tail = node

  @size.setter
  def size(self,num):
    self.__size = num

  def __str__(self):
    result = [str(nodo.value) for nodo in self]
    return ' <--> '.join(result)

  def print(self):
    for nodo in self:
      print(str(nodo.value))

  def __iter__(self):
    current = self.__head
    while current is not None:
      yield current
      current = current.next

  def append(self,value): # Adicionar al final
    newnode = Node(value)
    if self.__head is None:
      self.__head = newnode
      self.__tail = newnode
    else:
      self.__tail.next = newnode #enlazo nuevo nodo
      self.__tail = newnode
    self.__size += 1


  def popfirst(self):
    tempNode = self.__head
    if self.__head is None:
      return None
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      self.__head = self.__head.next
      self.__size -= 1

    tempNode.next = None  #limpiar la referencia al segundo nodo, ahora nueva cabeza
    return tempNode


class Queue:

  def __init__(self):
    self.__queue = LinkedList()


  def enqueue(self, e):
    self.__queue.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la cola"
    else:
      first_node = self.__queue.popfirst()
      return first_node.value

  def is_empty(self):
    return  self.__queue.size == 0

  def len(self):
    return  self.__queue.size


  def firs(self):
    return self.__queue.head.value

  def __str__(self):
    result = [str(nodo.value) for nodo in self.__queue]
    return ' -- '.join(result)



# ===== Node / slinkedlist / Stack (celda 11) =====
#Clases Base
from types import new_class
class Node:

  __slots__ = ("__value","__next")

  def __init__(self,value):
    self.__value = value
    self.__next = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next


  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise TypeError("El valor No debe ser None/Null.")
    self.__value = new_value

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,Node):
      raise TypeError("El next de un nodo, solo puede ser None ó otro Nodo")
    self.__next = new_next


  def __str__(self):
    return str(self.__value)


class slinkedlist:

  __slots__ = ("__head","__tail","__size")

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self, new_head):
    if new_head is not None and not isinstance(new_head,Node):
      raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó otro Nodo")
    self.__head = new_head

  @tail.setter
  def tail(self, new_tail):
    if new_tail is not None and not isinstance(new_tail,Node):
      raise TypeError("La cola de una lista enlazada, solo puede ser None ó otro Nodo")
    self.__tail = new_tail

  @size.setter
  def size(self, new_size):
    if not isinstance(new_size,int):
      raise TypeError("El tamaño de una lista enlazada, solo puede ser un numero entero")
    self.__size = new_size

  def __iter__(self):
    cur_node = self.__head
    while cur_node is not None:
      yield cur_node
      cur_node = cur_node.next

  def __str__(self):
     result = [str(node.value) for node in self]
     return ' --> '.join(result)


  def append(self, value):
    new_node = Node(value)

    if self.__tail is None:
      self.__head = new_node
    else:
      self.__tail.next = new_node

    self.__tail = new_node
    self.__size += 1


  def getnodebyindex(self,index):

    if not isinstance(index,int) or (index>self.__size-1) or (index <-1) :
      raise ValueError("Indice por fuera de rango ó no es tipo entero")

    if index == 0:
      return self.__head
    elif index == -1 or index == self.__size-1:
      return self.__tail
    else:
      i_temp = 0
      for cur_node in self:
        if i_temp == index:
          return cur_node
        i_temp += 1


  def pop(self):

    temp_node = self.tail

    if self.__head is None:
      raise TypeError("La lista esta vacía no hay elementos a eliminar")
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
    else:
      prev_tail = self.getnodebyindex(self.__size -2)
      #print("prev_tail",prev_tail)

      prev_tail.next =None
      self.__tail = prev_tail

    self.__size -= 1

    return temp_node.value


class Stack:

  def __init__(self):
    self.__s = slinkedlist()

  def __str__(self):
    result = [str(node.value) for node in self.__s]
    return ' || '.join(result)


  def push(self, e):
    self.__s.append(e)
    return True

  def pop(self):
    if not self.is_empty():
      e = self.__s.pop()
      return e
    else:
      raise ValueError("Error la pila esta vacia")

  def len(self):
    return self.__s.size

  def is_empty(self):
    return self.__s.size == 0

  def top(self):
    if not self.is_empty():
      return self.__s.tail.value
