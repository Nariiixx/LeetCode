class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            matriz = [nums1, nums2]
            todos_elementos = [elemento for linha in matriz for elemento in linha]

            todos_elementos.sort()
            ind = len(todos_elementos)
            ind1 = ind// 2
            if ind % 2 == 1:
                return todos_elementos[ind1]
            else:
                return (todos_elementos[ind1 - 1]+ todos_elementos[ind1])/2
