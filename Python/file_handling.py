

# 파일은 다음과 같이 사용이 가능하다.

file = open("target.txt") # 파일을 열어서 file 변수에 저장한다.
content = file.read() # file 변수의 내용을 읽어들인다.
file.close() # file 변수를 없애어 메모리단에서 삭제한다.

###
# open(<file>) - 매개변수로 넣은 파일을 실행한다. 
#           - <file>을 적어 줄 때에 그 확장자까지 모두 적어야한다. (ex - text.txt)
# <file>.read() - 대상 파일의 내용을 읽어들인다.
# <file>.close() - 열었던 파일을 닫아서 메모리단에서 삭제한다.
# <file>.write(<param>) - 매개변수를 받아서 파일 내에 추가하거나 수정한다.
###

# 위의 코드는 아래의 코드로 변경이 가능하다. 위의 코드와 아래의 코드는 기능적으로 완전히 같다.
# open의 두 번째 매개변수를 주지 않을 시에는 '읽기모드' 로만 파일을 연다
with open("data.txt") as file:
    content = file.read()

# open에 두 번째 매개변수를 준다면 '읽기모드' 대신 다른 모드로 파일을 열 수 있다.
with open("data.txt", "w") as file: # 해당 파일을 '쓰기모드'로 연다.
    file.write("Hello") # 해당 파일에 "Hello"라는 내용을 추가한다.

# for-loop를 활용하여 파일을 줄단위로 쉽게 읽을 수 있다.
contents = []
with open('data.txt') as file:
    for line in file:
        contents.append(line)


    