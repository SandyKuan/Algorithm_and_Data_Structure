numbers = [1,2,3,4.5,5]

# random indexing -->O(1) get items if we know the idex!!!

numbers[1] = 200
numbers[2] = 'Sandy'
print(numbers[0])
print(numbers[1])
print(numbers[2])

for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(numbers[i])

print(numbers[0:2])
print(numbers[:])
print(numbers[:-2])


# linear search O(N) comlexity

numbers2 = [100,200,300,400,250]
maxnum = numbers2[0]
for num in numbers2:
    if num > maxnum:
        maxnum = num
print(maxnum)