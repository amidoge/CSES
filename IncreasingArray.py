#SETUP
nums = []
length = int(input('Length of array: '))
for i in range(length):
    num = int(input('Type a number: '))
    nums.append(num)
#MAIN
count = 0
for i in range(length):
    for j in range(length):
        if j == length - 1:
            continue
        if nums[j] > nums[j + 1]:
            temp1 = nums[j]
            temp2 = nums[j + 1]
            nums[j] = temp2
            nums[j + 1] = temp1
    count += 1
print(count)