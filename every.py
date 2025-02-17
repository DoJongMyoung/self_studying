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
