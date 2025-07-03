class Solution:
    def twosoma(self, nums, target:int):
        nums= [2, 7, 11, 15]
        target = 9
        #abri um laço contando os items de nums e colocando o index no i
        for i in range(len(nums)):
            #abri outro laço colando o index no j
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:    #<--cria um if com nums[i(vai contar o numero de item/index)] + nums[j] == target
                    return [i, j]