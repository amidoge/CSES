limit = int(input('Type the amount of numbers in array: '))
nums = []
for i in range(limit - 1):
    number = int(input('Type an index:'))
    nums.append(number)

print(nums) #this is just to showcase your inputs

for j in range(1, limit + 1):
    if j not in nums:
        print(j)
        break
