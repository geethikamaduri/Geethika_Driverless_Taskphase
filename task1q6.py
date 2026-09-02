def find_index(sublist,num):
    low = 0
    high = len(sublist)
    while low < high:
        mid = (low + high) // 2
        if sublist[mid] < num:
            low = mid + 1
        else :
            high = mid
    return low

def main():
    hash_table = []
    for i in range(10):
       hash_table.append([])
    n = int(input('enter the value of n: '))
    for j in range(n):
       num = int(input('enter number: '))
       index = num % 10
       spot = find_index(hash_table[index],num)
       hash_table[index].insert(spot,num)
    for i in range(10):
       print(i ,':', hash_table[i])
if __name__ == "__main__":
    main()




            

