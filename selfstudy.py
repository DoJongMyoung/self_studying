#소수찾는 프로그램 만들기
#소수는 자기자신과 1만을 약수로 가짐 -> 자기자신과 1로 나누었을때만 나머지가 0이다.
#1은 소수가 아님.

def find_prime_number(num): #소수이면 True 반환 아니면 False반환
    i = 2 #num이라는 숫자를 나눌 변수 2부터 시작

    if num >= 2 : #num이 1인 경우와 2 이상인 경우를 나누기 위한 if문
        while i < (int(num ** 0.5) + 1) :
        #for i in range(2,int(num**0.5) + 1,1): #int의 제곱근 까지만 i를 +1씩 늘려가면서 반복
            if num % i == 0: #num을 i로 나눈 나머지가 0이면 i의 배수 이므로 소수가 아님.
                return False
            i = i + 1 # while문의 무한루프 막아줌, 비교할 변수에 1을 더해줌.
        return True # for문이 끝났으면 True 반환
    else:
        return False


number=int(input("숫자를 입력하세요 :"))


if (find_prime_number(number)):
    print(f"{number} is prime number")
else :
    print(f"{number} is not prime number")
