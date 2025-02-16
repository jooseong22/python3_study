'''
# 조건문 if

a = 18
b = 19
c = 20
d = 21

# ------> if 18 >= 20 ------> if False -----> 코드 실행 X
if a >= 20:
  print("a 입장")

if b >= 20:
  print("b 입장")

#  ------> if 20 >= 20 ------> if True ------> 코드 실행 O
if c >= 20:
  print("c 입장")

if d >= 20:
  print("d 입장")
'''

'''
# 문제 : 나이에 따른 올바른 말이 나오도록 해주세요.
# 재료.

age = 19

# v1
if age >= 20:
  print("성인입니다.")

if age < 20:
  print("미성년입니다.")

# v2
if age > 19:
  print("성인입니다.")

if age <= 19:
  print("미성년입니다.")

# v3
if age > 19:
  print("성인입니다.")

if age < 20:
  print("미성년입니다.")
'''

'''
if False :
  print("x")
  print("y")
print("z")

if 1 == 1 :
  print("1 yes")

if 1 != 1 :
  print("2 yes")

# ----> if True and False ----> if False
if 5 == 5 and 10 != 10:
  print("3 yes")

# ----> if True or False ----> if True
if 5 == 5 or 10 != 10:
  print("4 yes")

if 1 = 1:
  print("5 yes")

1 = 1
'''

'''
# 문제 : 나이에 따른 올바른 말이 나오도록 해주세요.
# 재료.

age = 19

# v1
if age >= 20:
  print("성인입니다.")

if age < 20:
  print("미성년입니다.")

# v2
if age > 19:
  print("성인입니다.")

if age <= 19:
  print("미성년입니다.")

# v3
if age > 19:
  print("성인입니다.")

if age < 20:
  print("미성년입니다.")
'''

'''
# 문제 : 실행되는 출력문에는 `참` 그렇지 않으면 `거짓` 이라고 적어주세요.
# 조건 : `참1`, `참2`, `거짓1` 이런 순으로 적어주세요.
# 실행 시 결과가 '참'만 나오면 성공

# 개념시작
if ( True ):
  print("참")

if ( False ):
  print("거짓")
# 개념끝

# 문제시작
a = 10

# `==` => 같다.
if ( a == 10 ):
  print("참1")

# `!=` => 같지 않다.
if ( a != 10 ):
  print("거짓1")

if ( a > 10 ):
  print("거짓2")

if ( a >= 10 ):
  print("참2")

b = 10

if ( a == b ):
  print("참3")

# c 에는 true or false 이 담긴다.
c = a != b
# c = False

if ( c ):
  print("거짓3")

if ( c == False ): # ----> False == False => True
  print("참4")

# `not` => 반전
if ( not c ): # not False -> True
  print("참5")

if ( not(not c) ): # not (not False) -> not True -> False
  print("거짓4")

d = True

if ( c != d ): # False != True ==> True
  print("참6")

if ( 10 > 5 and -6 > -10 and 10 != 10 ): # T and T and F
  print("거짓5")

if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ): # F and F and F or T
  print("참7")
# 문제끝
'''

'''
a = 10 # a 와 같은 값을 찾으시오.

if a == 5:
  print("답이야1")
elif a == 7:
  print("답이야2")
elif a == 10:
  print("답이야3")
elif a == 12:
  print("답이야4")
elif a == 10:
  print("답이야5")

'''
'''
if 10 != 10:
  print("맞아")
else :
  print("틀려")

if 10 != 10:
  print("맞아")
elif 5 == 5:
  print("맞아")
elif 2 != 2:
  print("맞아")
else :
  print("위에거 다 틀려서 이거 출력")
'''

'''
a = 30
b = 20

if a >= 20:
  print("a성인")
elif b >= 20:  # 이러면 b 체크를 못하니 적절치 않은 코드
  print("b성인")
'''

'''
# 문제 : 10대, 20대, 30대 중 나이에 맞는 변수를 출력해주세요.

age = 35 # 25로 바꿔서 실행해보세요. 15로도 바꿔서 실행해보세요.

# v1
print("v1")
if age >= 10 and age < 20: # 10 ~ 19
  print("10대")
if age >= 20 and age < 30: # 20 ~ 29
  print("20대")
if age >= 30 and age < 40: # 30 ~ 39
  print("30대")

# v2
print("v2")
if age >= 10 and age < 20: # 10 ~ 19
  print("10대")
elif age >= 20 and age < 30: # 20 ~ 29
  print("20대")
elif age >= 30 and age < 40: # 30 ~ 39
  print("30대")

# v3
print("v3")
if age >= 10 and age < 20: # 10 ~ 19
  print("10대")
elif age >= 20 and age < 30: # 20 ~ 29
  print("20대")
else :
  print("30대")

# 파이썬 특수 문법
print("파이썬 특수")
if 10 <= age < 20 :
  print("10대")
elif 20 <= age < 30:
  print("20대")
else :
  print("30대")
'''

'''
#C언어 기반. True, False 없다. if실행 1, if 실행X 0

if 1 :
  print("1은 실행")
if 0 :
  print("0은 실행안함")

'''

'''
# 문제 : 할인 대상인지 아닌지 출력해주세요. 주어진 코드를 수정해야 합니다.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.

age = 39

print("v1")
if age > 19 and age < 60:
  print("할인 대상이 아닙니다.")
if age <= 19 or age >= 60:
  print("할인 대상입니다.")

print("v2")
if age > 19 and age < 60:
  print("할인 대상이 아닙니다.")
elif age <= 19 or age >= 60:
  print("할인 대상입니다.")

print("v3")
if age > 19 and age < 60:
  print("할인 대상이 아닙니다.")
else:
  print("할인 대상입니다.")

print("v4")
if age <= 19 or age >= 60:
  print("할인 대상입니다.")
else:
  print("할인 대상이 아닙니다.")
'''

'''
# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : `and, or`없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.

age = 15

print("== 정답 v1 ==")
if age > 19:
  if age < 60:
    print("할인 대상이 아닙니다.")
  else :
    print("할인 대상입니다.")
else :
  print("할인 대상입니다.")


print("== 정답 v2 ==")
if age < 20:
  print("할인 대상입니다.")
elif age >= 60:
  print("할인 대상입니다.")
else :
  print("할인 대상이 아닙니다.")
'''

'''
# 문제 : 구구단 8단을 출력해주세요.
# 조건 : for, while문을 사용할 수 없습니다.

print("== v1 ==")
print("8 * 1 = 8")
print("8 * 2 = 16")
print("8 * 3 = 24")
print("8 * 4 = 32")
print("8 * 5 = 40")
print("8 * 6 = 48")
print("8 * 7 = 56")
print("8 * 8 = 64")
print("8 * 9 = 72")

print("== v2 ==")
print("8 * 1 = 8\n8 * 2 = 16\n8 * 3 = 24\n8 * 4 = 32\n8 * 5 = 40\n8 * 6 = 48\n8 * 7 = 56\n8 * 8 = 64\n8 * 9 = 72")


s = ""
s = s + "8 * 1 = 8" # -> s = "" + "8 * 1 = 8" -->  s = "8 * 1 = 8"
s = s + "\n8 * 2 = 16" # -> s = "8 * 1 = 8" + "\n8 * 2 = 16"
                       # -> s = "8 * 1 = 8\n8 * 2 = 16"
s = s + "\n8 * 3 = 24"
s = s + "\n8 * 4 = 32"
s = s + "\n8 * 5 = 40"
s = s + "\n8 * 6 = 48"
s = s + "\n8 * 7 = 56"
s = s + "\n8 * 8 = 64"
s = s + "\n8 * 9 = 72"

print("== v3 ==")
print(s)
'''

'''
print("8 * 1 = 8")
print("8 * 2 = 16")
print("8 * 3 = 24")
print("8 * 4 = 32")
print("8 * 5 = 40")
print("8 * 6 = 48")
print("8 * 7 = 56")
print("8 * 8 = 64")
print("8 * 9 = 72")

print("== smart ver.==")
print("8 * {} = {}".format(1, 8 * 1))
print("8 * {} = {}".format(2, 8 * 2))
print("8 * {} = {}".format(3, 8 * 3))
print("8 * {} = {}".format(4, 8 * 4))
print("8 * {} = {}".format(5, 8 * 5))
print("8 * {} = {}".format(6, 8 * 6))
print("8 * {} = {}".format(7, 8 * 7))
print("8 * {} = {}".format(8, 8 * 8))
print("8 * {} = {}".format(9, 8 * 9))

print("== smart ver.2 ==")
i = 1
print("8 * {} = {}".format(i, 8 * i))
i = 2
print("8 * {} = {}".format(i, 8 * i))
i = 3
print("8 * {} = {}".format(i, 8 * i))
i = 4
print("8 * {} = {}".format(i, 8 * i))
i = 5
print("8 * {} = {}".format(i, 8 * i))
i = 6
print("8 * {} = {}".format(i, 8 * i))
i = 7
print("8 * {} = {}".format(i, 8 * i))
i = 8
print("8 * {} = {}".format(i, 8 * i))
i = 9
print("8 * {} = {}".format(i, 8 * i))


print("== smart ver.3 ==")
i = 0
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))
i = i + 1
print("8 * {} = {}".format(i, 8 * i))


print("== smart ver.4 ==")
i = 0
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1 # i = 9
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))

print("ver 4의 i : {}".format(i))

print("== smart ver.5 ==") # i가 9 위로 연산 필요 X
i = 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1
if i <= 9 :
  print("8 * {} = {}".format(i, 8 * i))
  i = i + 1

print("ver5의 i : {}".format(i))
'''

# 반복문 while

# i = 1
# if i <= 9 :
#   print("8 * {} = {}".format(i, 8 * i))
#   i = i + 1


'''
# 문제 : 8단 while문으로 작성해보세요.
i = 1
while i <= 9:
  print("8 * {} = {}".format(i, 8 * i))
  i += 1

# 문제 1부터 300까지 출력해주세요.(개념 : while)
i = 1
while i <= 300:
  print("i : {}".format(i), end = "")
  i += 1

i = 1
while i <= 300:
  print(f"i : {i}", end = "")
  i += 1

# 문제 500부터 2330까지 출력해주세요.(개념 : while)
print() # 줄바꿈 용도
i = 500
while i <= 2330:
  print(f"i : {i}", end = "")
  i += 1

# 문제 100부터 -25까지 출력해주세요.(개념 : while)
print()
i = 100
while i >= -25:
  print("i : {}".format(i), end="")
  i -= 1
  '''

'''
# 문제 1부터 100 사이의 짝수만 출력해주세요.(개념 : while, if, %)

# i = 2
# while i <= 100:
#   print("i : {}".format(i))
#   i += 2

# 나누기의 나머지 구하기
# print(10 % 1) # 0
# print(10 % 2) # 0
# print(10 % 3) # 1
# print(10 % 4) # 2
# print(10 % 5) # 0
# print(10 % 6) # 4
# print(10 % 7) # 3
# print(10 % 8) # 2
# print(10 % 9) # 1
# print(10 % 10) # 0

# print(2 % 2) # 0
# print(3 % 2) # 1
# print(4 % 2) # 0
# print(5 % 2) # 1
# print(6 % 2) # 0
# print(7 % 2) # 1
# print(8 % 2) # 0

# a = 2
# if a % 2 == 0 :
#   print(f"{a}는 짝수야")
# a += 1
# if a % 2 == 0 :
#   print(f"{a}는 짝수야")
# a += 1
# if a % 2 == 0 :
#   print(f"{a}는 짝수야")
# a += 1
# if a % 2 == 0 :
#   print(f"{a}는 짝수야")

a = 1
while a <= 100:
  if a % 2 == 0:
    print(f"a : {a}")
  a += 1
  '''

'''
# 문제 - 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.(개념 : while, if, %)
a = 1
while a <= 1000:
  if a % 3 == 0:
    print(f"a : {a}", end="")
  a += 1
  '''

'''
# 문제 - 1부터 5까지의 합을 출력해주세요.(개념 : while)
sum = 0
i = 1
sum = sum + i
print("1 sum : {}".format(sum))
i += 1
sum = sum + i
print("2 sum : {}".format(sum))
i += 1
sum = sum + i
print("3 sum : {}".format(sum))
i += 1
sum = sum + i
print("4 sum : {}".format(sum))
i += 1
sum = sum + i
print("5 sum : {}".format(sum))




# i = 1
# i = i + i # i = 2
# i = i + i # i = 2 + 2 => 4
# i = i + i # i = 4 + 4 => 8
# i = i + i # i = 8 + 8 => 16
# print(i)

'''

'''
i = 1
while i <= 5:
  sum = 0
  sum = sum + i
  print("1 sum : {}".format(sum))
  i += 1

sum = 0
i = 1
while i <= 5:
  sum = sum + i
  print("1 sum : {}".format(sum))
  i += 1

# 1부터 5까지의 곱을 구하시오
sum = 1
i = 1
while i <= 5:
  sum = sum * i
  print("곱 : {}".format(sum))
  i += 1
'''

'''
# 문제 - 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.(개념 : while, if, %)
sum = 0
i = 1
while i <= 100 :
  if i % 2 == 0 :
    sum = sum + i
  i += 1

print(sum) # 2550
'''

'''
# 문제 - 1부터 100까지의 수 중에서 짝수이고 3의 배수가 아닌 수의 합을 출력해주세요.(개념 : while, if, %)
sum = 0
i = 1
while i <= 100:

  if i % 2 == 0 and i % 3 != 0:
    sum += i

  i += 1
print(sum) # 1734

'''

