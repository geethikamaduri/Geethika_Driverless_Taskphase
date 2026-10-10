n = int(input('enter the value of n(number of strings): '))
strings = [input('enter string: ')for i in range(n)]
dictionary = {}
for string in strings:
    for char in string.lower():
        if char.isalpha():
            if char in dictionary:
                dictionary[char] += 1
            else: 
                dictionary[char] = 1
print (dictionary)    
