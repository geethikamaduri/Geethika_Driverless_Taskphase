class sort:
    def selection_sort (self,list):
        n = len(list)
        for i in range(n):
            min = i
            for j in range(i + 1,n):
                if list[j].lower() < list[min].lower():
                    min = j
            temp = list[i]
            list[i] = list[min]
            list[min] = temp
        return list   
    
class binarysort:
    def binarysort(self,list,target):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            if list[mid].lower() == target.lower():
               return mid
            elif list[mid].lower() < target.lower():
                low = mid + 1
            else: 
                high = mid - 1
        return None
                
n = int(input('enter n(number of strings):'))
strings = [input('enter string: ')for i in range(n)]
sorter = sort()
sortedthings = sorter.selection_sort(strings)
print(sortedthings)
target = input('\nenter string to search:')
searcher = binarysort()
result = searcher.binarysort(sortedthings,target)
print(result)         
