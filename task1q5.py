hash_table = []
for i in range(10):
    hash_table.append([])
n = int(input('enter the value of n: '))
for j in range(n):
   num = int(input('enter number: '))
   index = num % 10
   hash_table[index].append(num)
for i in range(10):
   print(i ,':', hash_table[i])

