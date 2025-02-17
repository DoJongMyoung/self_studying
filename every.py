# a = 11 # 01011
# b = 30 # 11110
#
# print(a & b) #01010 -> 10 // 둘다 1일때만 1
# print(a ^ b) #10101 -> 21 // 둘이 다를때만 1
# print(a | b) #11111 -> 31 //하나라도 1이면 1
#
# def is_even(num):
#     # if num & 1: #num이 홀수면 T반환
#     #     print("홀수입니다.")
#     # else:
#     #     print("짝수입니다")
#     return not num & 1 # num & 1 은 num이 홀수이면 T 짝수이면 F 그런데 not이 있으므로 이 함수는 홀수이면 F 짝수이면 T를 반환함.
#
#
#
# print(is_even(8))
# print(is_even(7))


#팔진수 변환 프로그램

def my_oct(num):
     if num == 0:
        return ""
     else:
        return my_oct(num // 8) + str(num % 8)
        # str을 나중에 추가하므로 62를 8로 나눈 나머지인 6은 제일 마지막에 왼쪽에 추가될 예정
        # 62 // 8의 값인 7이 num으로 대입되어서 함수가 다시 실행되고, 7의 나머지인 7은 나중에 추가
        # 7 // 8의 값인 0이 num으로 대입되는데 이때는 if문에 의해서 ""를 출력함.
        # 따라서 순차적으로 "" + "7" + "6"이 문자열 형태로 출력됨.
print(my_oct(62))
print(type(my_oct(62)))