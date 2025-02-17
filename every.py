#memoization -> 재귀함수 복습 .
import time

import mymath

def Fibonazzi(n):
    """
    입력받는 수에 해당하는 피보나치 수를 찾는 프로그램.
    :param n: 입력받는 값
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonazzi(n-2) + Fibonazzi(n-1)

#이게 재귀를 이용한 시간 복잡도 높은 Fibonazzi 함수

#memoization ver
#한번 계산 한 값을 저장해야함 . -> 배열을 담을 리스트 하나 준비

start = time.time()
print(Fibonazzi(40))
end = time.time()
print(f"걸린 시간 : {start-end}")




F_list = [0,1]



def Fibonazzi_memo(num):
    """
    memo를 이용한 시간복잡도 낮은 피보나치 함수 -> 배열안에 피보나치 수를 저장하고 배열안에 있는 경우 함수를 재귀 시키지 않고
    그냥 결과값을 불러오게해 소요시간을 줄임
    :param num:
    :return:
    """
    if num < len(F_list) : #index가 1 작으므로 등호를 쓸 수 없음
        return F_list[num]
    else:
        F_list.append(Fibonazzi_memo(num-2) + Fibonazzi_memo(num - 1))
        return F_list[num]


num = int(input()) # 찾으려는 피보나치 수


start = time.time()
print(Fibonazzi_memo(num))
end = time.time()
print(f"걸린 시간 : {start-end}")
#나는 5번째 피보나치 수를 찾고싶은데 그건 컴퓨터에는 index번호가 4인 수임