import time

#closure 개념 복습

def timer(func):
    def wrapper(*arg):

        start = time.time()
        result = func(*arg)
        end = time.time()
        print(f"함수 작동 시간 : {start - end}")

        return result
    return wrapper




def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num-1) * num

@timer
def nCr(n , r):
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

# print(nCr(7,4))


if __name__ != "__main__":
    print("나는 메인으로 실행되진 않고 임포트 되어 실행되었어.")