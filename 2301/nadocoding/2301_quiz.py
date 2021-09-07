import math
'''
Quiz 3-1)
주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
예시
id_number = 020316 일 때

출력 예시
02
0316
632
'''
# id_number = "020316"
# year = id_number[0:2] #[:2], [-6:-4]
# month_day = id_number[2:6] #[2:], [-4:]
# print(year + "\n" + month_day)
# print(int(year) * int(month_day))
#
# print("------------------------")
'''
Quiz 3-2
집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
예시
phone_number = 02-1234-5678 또는 032-9876-4321
'''
# print("Quiz 2)")
# phone_number1 = "02-1234-5678"
# print(phone_number1[:phone_number1.index('-')] + "\n" + phone_number1[-4:])
# index() 없으면 ValueError, find() 없으면 -1
# print("------------------------")
#
# phone_number2 = "032-1234-5678"
# print(phone_number2[:phone_number2.index('-')] + "\n" + phone_number2[-4:])

#전화번호 입력 시 -가 있든, -가 없든, 찰떡같이 알아먹기
#phone_number1 = '010-1234-5678'
#phone_number2 = '01098765432'
#phone_number3 = '010 1111 2222'

#phone_number = phone_number3
#result = phone_number.replace('-', '').replace(' ', '')
#print(result)

'''
Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100' 또는 student_number = '2000'
<출력 예시>
1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
'''

#student_number = '2100'
#cls = int(student_number[1])
# if cls < 0 or cls > 6 :
#     print("잘못 입력했습니다.")
# elif cls >= 1 or cls <= 2 :
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif cls >= 3 or cls <= 4:
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif cls >= 5 or cls <= 6 :
#     print(f"{number}반 뉴미디어디자인과")

# majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f'{number}반 {mojors[number-1]}')

#majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']

#if 1 <= cls <= 6:
#    print(f'{cls}반 {majors[(cls - 1) // 2]}')
#else:
#    print("잘못입력했습니다.")

'''
Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
<함수 호출>
grade, major = get_major('2100')
print(major, grade) #뉴미디어소프트웨어과 2
'''
#def get_major(argument):
#    if argument[1] == "1" or argument[1] == "2":
#        major = "뉴미디어소프트웨어과"
#        return argumenet[0], major
#    elif argument[1] == "3" or argument[1] == "4":
#        major = "뉴미디어웹솔루션과"
#        return argument[0], major
#    elif argument[1] == "5" or argument[1] == "6":
#        major = "뉴미디어디자인과"
#        return argument[0], major

#grade, major = get_major("2501")
#print(major, grade)
'''
Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
<함수 호출>
print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5
'''

#def average(*nums):
#    sum = 0
#    for num in nums:
#        sum += num
#    return sum / len(nums)

#print(average(10, 20, 30))
#print(average(4, 23))

'''
Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
(소수 첫째자리까지 반올림)
* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
18.5 미만: 저체중
18.5 이상 23 미만: 보통
23 이상 25 미만: 과체중
25 이상: 비만

<함수 호출>
bmi = get_bmi(176, 69)
print(bmi) #22.3

def get_bmi(cm, kg) :
    return round(kg / ((cm/100)**2),1)
bmi = get_bmi(176, 69)

print(bmi)
'''

#def get_bmi(hight, weight):
#    height /= 100
#    return round(width / (height**2), 1)

#bmi = get_bmi(176, 69)
#print(bmi)
#if bmi < 18.5:
#    print('저체중')
#elif 18.5 <= bmi <= 23:
#    print('정상')
#elif bmi < 25:
#    print('과체중')
#elif 25 <= bmi:
#    print('비만')


#구구단 7단 출력하기
#for i in range(1, 9+1):  #i : 1~9
#    print(f'7 x {i} = {7 * i}')

#구구단 2~9단 출력하기
#for dan in range(2, 10):  #dan : 2~9
#    for i in range(1, 9+1):
#        print(f'{dan} x {i} = {dan * i}')
#    print('-' * 10)

#구구단 2~7단까지 출력하기
#for dan in range(2, 10):  #dan : 2~9
#    for i in range(1, 9+1):  #i : 1~9
#        print(f'{dan} x {i} = {dan * i}')
#    print('-' * 10)
#    if dan == 7:
#        break

#구구단 2~7단 출력하되, x1, x3, x5, x7, x9인 것만 출력하기
#for dan in range(2, 10):  #dan : 2~9
#    for i in range(1, 9+1):  #i : 1~9
#        if i == 2 or i == 4 or i == 6 or i == 8:
#            continue
#        print(f'{dan} x {i} = {dan * i}')
#    print('-' * 10)
#    if dan == 7:
#        break



'''
 Quiz3-1. n_sum() 함수를 만든다.
 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다.
 10자리 이상이면 -1 리턴한다.
'''
#
# def n_sum(argument):
#     if argument < 10:
#         return argument
#     elif len(str(argument)) >= 10:
#         return -1
#     else:
#         return (argument%10) + int(n_sum(argument/10))
#
# result = n_sum(10)
# print(result)  # 1
# result = n_sum(331)
# print(result)  # 7
# result = n_sum(408)
# print(result)  # 12
# result = n_sum(1000000000)
# print(result)  # -1
#
'''
 Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
 * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''
#
# def get_subway_fare(km):
#     basic = 720
#     tenToFifty = basic + math.ceil((km - 10) / 5) * 100
#     Over50km = basic + (40 / 5 * 100) + math.ceil((km - 50) / 8) * 100
#
#     if km < 10:
#         return int(basic)
#     elif 10 <= km <= 50:
#         return int(tenToFifty)
#     else:
#         return int(Over50km)
#
# fare = get_subway_fare(5)
# print(fare)  # 720
# fare = get_subway_fare(26)
# print(fare)  # 1120
# fare = get_subway_fare(61)
# print(fare)  # 1720
#
'''
 Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
 * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''
# def get_three_six_nine(num):
#     cnt = str(num).count('3') + str(num).count('6') + str(num).count('9')
#     if cnt == 0:
#         return num
#     else:
#         return '짝' * int(cnt)
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝
#
'''
 Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
 1. 함수의 이름을 정해준다.
 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
 3. 리턴하는 것을 말해준다.
 4. 출력 예시를 보여준다.
 5. 내가 낸 문제의 답안을 제출한다.

 가지고 있는 돈(money)과 사고 싶은 음식(food)을 입력하면
 가지고 있는 돈으로 몇 개의 음식을 살 수 있는지
 알려주는 get_food()함수를 만든다.
 초콜릿은 1000원, 아이스크림은 1500원, 빵은 2000원이다.
'''
# def get_food(money, food):
#     choco = 1000
#     icecream = 1500
#     bread = 2000
#     print("사고 싶은 음식은? " + food)
#     if food == "choco":
#         if money < choco:
#             print("못사요")
#         else:
#             result = str(int(money/choco))
#             print(result + "개 살 수 있습니다.")
#     elif food == "icecream":
#         if money < icecream:
#             print("못사요")
#         else:
#             result = str(int(money / icecream))
#             print(result + "개 살 수 있습니다.")
#     elif food == "bread":
#         if money < bread:
#             print("못사요")
#         else:
#             result = str(int(money/bread))
#             print(result + "개 살 수 있습니다.")
#
# get_food(2000, "choco")  #2개
# get_food(3000, "icecream")  #2개
# get_food(3000, "bread")  #1개
# get_food(1500, "bread")  #못사요

'''
 Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
 is_prime() 함수를 만든다.
 인수로 1개의 숫자를 받는다.
 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
# def is_prime(num):
#     res = "소수"
#     if num != 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 res = "소수 아님"
#     else:
#         res = "소수 아님"
#
#     return res

# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
# def get_compliment(str):
#     if '고구마' in str:
#         res = "왓쇼이!"
#     elif '맛있는' in str:
#         res = "우마이!"
#     elif '놀랄 만한' in str or '황당한' in str or '굉장한' in str:
#         res = "요모야..!"
#     else:
#         res = "으무!"
#     return res
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

'''
Quiz5-1. 모듈이란?
필요한것들끼리 부품처럼 만들어진 파일
'''

'''
Quiz5-2. 패키지란?
모듈들을 모아놓은 집합
'''

'''
Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
from theater_module import price as p2301
'''

'''
Quiz5-4. __all__의 역할은?
패키지 내에서 * 사용할때 참조시킬 파일을 정의하는것

'''

'''
Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
if __name__ == "__main__":
'''

'''
Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 
detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?

import travel.vietnam
< 가 > 
trip_to = travel.vietnam.VietnamPackage() 
trip_to.detail()

from travel import vietnam
< 나 > 
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel.vietnam import VietnamPackage
< 다 > 
trip_to = VietnamPackage()
trip_to.detail()
'''