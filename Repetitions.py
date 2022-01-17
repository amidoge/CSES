a = input('Sequence: ')
highest_count = 0
count = 0
p = ''

for i in range(len(a)):
    if a[i] != p: #if current index does not equal previous index
        p = a[i] 
        count = 1 
    elif a[i] == p: #ELSE if current index does equal previous index
        count += 1 
    if count > highest_count: 
        highest_count = count 

print(highest_count)
