###
# 딕셔너리는 연관 배열, 해시에 해당하는 자료형으로, Key와 Value형식으로 자료를 저장하고 조회할 수 있는 자료형이다. 
# 딕셔너리 자료형은 중괄호로 묶어서 표현이 가능하다. 기본적인 구조는 아래와 같다.
###

# dic={Key1:Value1, Key2:Value2, Key3:Value3, ...}

dict_zero = {}
person = {'name' : 'Michael', 'age': 10}

print(dict_zero) # {}
print(person['name']) # 'Michael'




# 값 추가하기 -  Dict_name['new_key'] = 'New Value'

person = {'name' : 'Michael', 'age': 10}
person['job'] = 'coding'
print(person['job']) # 'coding'




# 값 삭제하기 -  del Dict_name['new_key']

person = {'name' : 'Michael', 'age': 10}
del person['age']

print(person) # {'name' : 'Michael'}
print(person['age']) # KeyError: 'age'

###
# 딕셔너리 관련 함수들
###

"""
1. keys - 대상 딕셔너리의 Key만을 모아서 dict_keys 객체로 돌려준다.

dict={"Key1":"Value1", "Key2":"Value2", "Key3":"Value3"}
dict.keys() #dict_keys(['Key1', 'Key2', 'Key3']) 

* 파이선 2.7버전 까지는 dict_keys 객체 대신에 리스트로 돌려주었다. 하지만 리스트로 돌려주기 위해서는 메모리 낭비가 발생되는데,
* 이런 이슈를 해결하기 위해 파이썬 3.0 이후 버전 부터 dict_keys 객체로 돌려주게 되었다.
* dict_keys / dict_values / dict_items 등은 리스트로 굳이 반환하지 않더라도 iterable하기에 for-loop와 같은 반복구분을 실행할 수 있다.

만일 list로 반환되는 키 리스트가 필요하다면 아래와 같이 형변환을 하여 활용하면 된다.

list(dict.keys())

"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }
person.keys() # dict_keys(['name', 'age', 'address'])
print(list(person.keys())) # ['name', 'age', 'address']



"""
2. values - 대상 딕셔너리의 values만을 모아서 dict_values 객체로 돌려준다.

dict={"Key1":"Value1", "Key2":"Value2", "Key3":"Value3"}
dict.values() # dict_values(['Value1', 'Value2', 'Value3']) 
"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }
person.values() # dict_values(['kim', '30', 'seoul'])
print(list(person.keys())) # ['kim', '30', 'seoul']



"""
3. items - 대상 딕셔너리의 key와 value를 한 쌍의 튜플로 묶어서 dict_items라는 객체로 돌려준다.

dict={"Key1":"Value1", "Key2":"Value2", "Key3":"Value3"}
dict.items()
# dict_items([("Key1", "Value1"), ("Key2", "Value2"), ("Key3", "Value3")]) 
"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }
person.items() # dict_items([('name', 'kim'), ('age', 30), ('address', 'seoul')])

li = list(person.items())

print(li) # [('name', 'kim'), ('age', 30), ('address', 'seoul')]
print(li[0]) # ('name', 'kim')
print(li[0][0]) # name



"""
4. clear - 대상 딕셔너리안의 모든 요소를 삭제한다.

dict={"Key1":"Value1", "Key2":"Value2", "Key3":"Value3"}
dict.clear()
print(dict) # {} 

* 객체 자체가 메모리 상에서 사라지는 것이 아니라 객체 안의 요소들만 삭제되는 것을 기억하자. 이후 해당 객체 안에 새롭게 key-value를 넣어줄 수 있다.
"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }
person.clear()
print(person) # {}

person['name'] = 'lee'
print(person) # {'name' : 'lee'}



"""
5. get - 매개변수로 받은 key의 value를 대상 딕셔너리에서 가져온다.

dict={'Key1' : 'Value1', 'Key2' : 'Value2', 'Key3' : 'Value3'}
dict.get('Key1') # 'Value1' 
dict.get('Key2') # 'Value2'

* Notation (dict['key']) 형식으로 불러오는 것과 똑같은 기능을 하지만 주요한 차이점이 두 가지가 있다.
	- Notation은 키에 해당하는 값이 없다면 오류를 발생시키지만
	  get을 이용하였을 때 인자로 받은 키에 해당 하는 값이 없다면 None을 돌려준다.
      
dict={'Key1' : 'Value1', 'Key2' : 'Value2', 'Key3' : 'Value3'}
dict['Key4'] # KeyError 
dict.get('Key4') # None 

	- get에 두 번째 매개변수에 값을 부여하면 키에 해당하는 값이 없을 때
	  두번째 매개변수를 준다.

dict={'Key1' : 'Value1', 'Key2' : 'Value2', 'Key3' : 'Value3'}
dict.get('Key4', '존재하지 않는 키입니다.') # '존재하지 않는 키입니다.'      
"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }

person.get('name') # 'Kim'
person.get('phone') # None
person.get('phone', '***-****-****') # '***-****-****'

person['phone'] = 01099999999 # 값을 추가하고 get을 해보자
person.get('phone', '***-****-****') # 01099999999

person['name'] # 'Kim' | person.get('name') 과 같다.
person['married'] # KeyError 



"""
6. in - 해당 key가 대상 딕셔너리에 있는지 조사한다.

dict={'Key1' : 'Value1', 'Key2' : 'Value2', 'Key3' : 'Value3'}
'Key1' in dict # True 
'Key53' in dict # False
"""

person = {'name' : 'kim', 'age' : 30, 'address' : 'seoul' }
'name' in person # True
'home' in person # False