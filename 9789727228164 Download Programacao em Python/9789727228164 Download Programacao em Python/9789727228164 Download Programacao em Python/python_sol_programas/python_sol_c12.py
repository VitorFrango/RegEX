"""

Soluções para o livro

Programação em Python: fundamentos e resolução de problemas
Ernesto Costa
© FCA, 2015

Comentários e sugestões devem ser dirigidas ao autor paraq o email ernesto@dei.uc.pt

Versão 0.9

"""

# Capítulo 12: Tipos e Classes

# 12.1
class Empty(Exception):
   """Tentativa de aceder a um contentor vazio..."""
   pass

class Stack:
   
   def __init__(self):
      self.stack = []
   
   def push(self,object):
      self.stack.insert(0,object)
   
   def pop(self):
      if self.is_empty():
         raise Empty('ERRO: acesso e modificação de uma pilha vazia!')
      return self.stack.pop(0)
   
   def top(self):
      if self.is_empty():
         raise Empty('ERRO: Consulta de uma pilha vazia!')
      else:
         return self.stack[0]
   
   def is_empty(self):
      return len(self.stack) == 0
   
   def len(self):
      return self.stack.__len__()
 
   def __str__(self):
      saida = ''
      for elem in self.stack[::-1]:
         saida = str(elem) + ',' + saida
      saida = saida[:-1]
      return '[<' + saida + ']'
      
      
if __name__ == '__main__':
   pil_1 = Stack()
   pil_1.push('A')
   print(pil_1.is_empty())
   print(pil_1)
   print(pil_1.top())
   pil_1.push('B')
   pil_1.push('C')
   print(pil_1)
   pil_1.pop()
   print(pil_1)




# 12.2

# 12.3

# 12.4

# 12.5

# 12.6

# 12.7

# 12.8
class Empty(Exception):
   """Tentativa de aceder a um contentor vazio..."""
   pass

class Deque:
   
   def __init__(self):
      self.deque = []
   
   def insere_frente(self,objecto):
      self.deque.insert(0,objecto)
      
   def insere_tras(self,objecto):
      self.deque.append(objecto)   
   
   def remove_frente(self):
      if self.is_empty():
         raise Empty('ERRO: acesso e modificação de uma pilha vazia!')
      return self.deque.pop(0)
   
   def remove_tras(self):
      if self.is_empty():
         raise Empty('ERRO: acesso e modificação de uma pilha vazia!')
      return self.deque.pop()   
   
   
   def is_empty(self):
      return len(self.deque) == 0
   
   def len(self):
      return self.deque.__len__()
 
   def __str__(self):
      saida = ''
      for elem in self.deque[::-1]:
         saida = str(elem) + ',' + saida
      saida = saida[:-1]
      return '[<' + saida + '>]'
      
      
if __name__ == '__main__':
   deq_1 = Deque()
   deq_1.insere_frente('A')
   print(deq_1.is_empty())
   print(deq_1)
   deq_1.insere_frente('B')
   deq_1.insere_tras('C')
   print(deq_1)
   deq_1.remove_frente()
   print(deq_1)
   

# 12.9 
def capicua(cadeia):
   if cadeia.len() <= 1:
      return True
   else:
      f = cadeia.remove_frente()
      t = cadeia.remove_tras()
      return (f == t) and capicua(cadeia)
   
   
# 12.10

# 12.11

# 12.12

# 12.13
class Array2D:
    
   def __init__(self, numbrows, numbcols):
      self._the_rows = Array(numbrows)
    
      for r in range(numbrows):
         self._the_rows[r] = Array(numbcols)
        
        
   def numb_rows(self):
      return len(self._the_rows)

   def numb_cols(self):
      return len(self._the_rows[0])

   def clear(self, value):
      for row in self._the_rows:
         row.clear(value)
        
   def __getitem__(self,index):
      assert len(index) == 2, "Número de índices inválido"
      row = index[0]
      col = index[1]
    
      assert row >= 0 and row < self.numb_rows() and \
             col >= 0 and col < self.numb_cols(), \
             "índices fora dos limites."
      array_row = self._the_rows[row]
      return array_row[col]
    

   def __setitem__(self,index, value):
      assert len(index) == 2, "Número de índices inválidos"
      row = index[0]
      col = index[1]
    
      assert row >= 0 and row < self.numb_rows() and \
           col >= 0 and col < self.numb_cols(), \
           "índices fora dos limites"
      array_row = self._the_rows[row]
      array_row[col] = value

# 12.14

# 12.15

# 12.16

# 12.17

# 12.18

# 12.19

# 12.20
    