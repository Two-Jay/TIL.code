
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

# javascript의 array.prototype.map과 array.prototype.filter와 유사한 기능을 알아보자
# new_list = [<expression> for <item> in <list>]
#  - 리스트 <list>를 전체 순회하여 나오는 각각의 <item>에 대해 <expression> 으로 바꾸어 새로운 리스트을 생성한다.

# 리스트 복사하기
list = ["Apple", "Banana", "Chamwae"]

new_fruits = [x for x in list] 
print(new_fruits) # ["Apple", "Banana", "Chamwae"]
head_alphabet = [x[0] for x in list ]
print(head_alphabet) # ["A", "B", "C"]

# 만약 조건문을 붙여서 필터링을 하고 싶다면 아래와 같이 하면된다.
# new_list = [<expression> for <item> in <list> if <conditions>]
#  - 리스트 <list>를 전체 순회하여 나오는 각각의 <item>에 대해 <conditions>을 필터링하여 <expression>을 수행한 후 새로운 리스트을 생성한다.
#  - 순서상 조건문으로 먼저 필터링을 하여 <item>을 뽑아내고, 그 이후 <expression>에서 정한 작업을 수행한다.

# 숫자가 있는 리스트에 짝수로만 이루어진 리스트와 홀수로만 이루어진 리스트로 필터링을 하여보자

numbers = [1,2,3,4,5,6,7,8,9,10]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 == 1]
print(even, odd) # [2, 4, 6, 8, 10] [1, 3, 5, 7, 9]

# 모든 홀수를 찾아서 필터링 한 뒤, 1을 더하고, 새로운 리스트로 반환해보자.
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_plus = [n+1 for n in numbers if n % 2 == 1]
print(odd_plus) # [2, 4, 6, 8, 10]


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

