#두 수를 입력받아서 두 수 사이의 소수를 출력하는 프로그램만들기
#큰 수까지의 소수를 출력하자 if문으로 작은수 보다 큰것만 골라서 출력하게 만들면 될듯

def prime_number(num1, num2):
    if num1 > num2 : #만약 앞에있는 수가 뒤에 있는 수보다 크다면
        num1 , num2 = num2 , num1 # 앞뒤에 저장된 숫자 바꿔주기.

    num = 2 # num은 2부터 시작해서 num2까지 커질 변수

    while(num < num2) :

        i = 2  # num이라는 숫자를 나눌 변수 2부터 시작

        if num >= 2:  # num이 1인 경우와 2 이상인 경우를 나누기 위한 if문
            while i < (int(num ** 0.5) + 1):
                # for i in range(2,int(num**0.5) + 1,1): #int의 제곱근 까지만 i를 +1씩 늘려가면서 반복
                if num % i == 0:  # num을 i로 나눈 나머지가 0이면 i의 배수 이므로 소수가 아님.
                    break
                    # return False
                i = i + 1  # while문의 무한루프 막아줌, 비교할 변수에 1을 더해줌.
            else :
                if (num1<num):
                    print(f"{num} is prime number")
             # return True  # for문이 끝났으면 True 반환
        # else:
        #     return False
        num = num + 1

prime_number(20,451)


#소수찾는 프로그램 만들기
#소수는 자기자신과 1만을 약수로 가짐 -> 자기자신과 1로 나누었을때만 나머지가 0이다.
#1은 소수가 아님.

# def find_prime_number(num): #소수이면 True 반환 아니면 False반환
#     i = 2 #num이라는 숫자를 나눌 변수 2부터 시작
#
#     if num >= 2 : #num이 1인 경우와 2 이상인 경우를 나누기 위한 if문
#         while i < (int(num ** 0.5) + 1) :
#         #for i in range(2,int(num**0.5) + 1,1): #int의 제곱근 까지만 i를 +1씩 늘려가면서 반복
#             if num % i == 0: #num을 i로 나눈 나머지가 0이면 i의 배수 이므로 소수가 아님.
#                 return False
#             i = i + 1 # while문의 무한루프 막아줌, 비교할 변수에 1을 더해줌.
#         return True # for문이 끝났으면 True 반환
#     else:
#         return False
#
#
# number=int(input("숫자를 입력하세요 :"))
#
#
# if (find_prime_number(number)):
#     print(f"{number} is prime number")
# else :
#     print(f"{number} is not prime number")
