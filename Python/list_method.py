
###
# list.append(x) # append x to end of list
# list.extend(iterable) # append all elements of iterable to list
# list.insert(i, x) # insert x at index i
# list.remove(x) # remove first occurance of x from list
# list.pop([i]) # pop element at index i (defaults to end of list)
# list.clear() # delete all elements from the list
# list.index(x[, start[, end]]) # return index of element x
# list.count(x) # return number of occurances of x in list
# list.reverse() # reverse elements of list in-place (no return)
# list.sort(key=None, reverse=False) # sort list in-place
# list.copy() # return a shallow copy of the list
###


***

# list.append(x) - 배열의 맨 뒤에 매개변수로 주어진 x를 요소로 추가한다.

numbers = []
numbers.append("1")
print(numbers) # ["1"]
numbers.append("2")
print(numbers) # ["1", "2"]


numbers = [1,5,32,632,3,6,12]
small_numbers = []

for num in numbers:
    if num < 10:
        small_numbers.append(num)

print(small_numbers) # [1,5,3,6]
print(sorted(small_numbers)) # [1,3,5,6]


def my_append(list, parameter):
    index = len(list)
    list[index] = parameter


***

