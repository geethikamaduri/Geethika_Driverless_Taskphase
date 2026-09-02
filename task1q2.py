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

n = int(input('enter n(no. of strings): '))
strings = [input('enter string: ')for i in range(n)]
sorter = sort()
sortedthings = sorter.selection_sort(strings)
print(sortedthings)