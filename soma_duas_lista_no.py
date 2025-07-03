 class Node:
     def __init__(self, valor=0, proximo=None):
         self.valor = valor
         self.proximo =None
    def  cria_lista(valores)
        if not valores:
                return None
          cabeca = Node(valores[0])
          atual = cabeca
          for valor in valores[1:]:
                  atual.proximo = Node(valor)
                  atual = atual.proximo
           return cabeca
class Solution:
    def somadoisnumero(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = Node(0)
        atual = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.valor if l1 else 0
            v2 = l2.valor if l2 else 0

            soma= v1 + v2 + carry
            carry = soma//10
            atual.proximo = Node(soma % 10)
            atual= atual.proximo
        
            if l1: l1 = l1.proximo
            if l2: l2 = l2.proximo
        return dummy.proximo


