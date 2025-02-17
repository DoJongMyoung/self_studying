# numbers=input("숫자를 입력 :").split()
#
# num1 = int(numbers[0])
# num2 = str(numbers[1])
# num3 = int(numbers[2])
#
# print(f"{num1} , {num2}, {num3}")

course = "       *  1 KEs 2024# KEB !Bootcamp KEB...*!#        "
# print(course.find('KEB'))
# print(course.rfind('KEB'))
# print(course.index('KEB'))
# print(course.rindex('KEB'))
# # print(course.find('Inha'))  # -1
# # print(course.index('Inha'))  # ValueError: substring not found
# #
print(course)
course = course.replace('KEB', 'Inha', 2)
print(course)
print(course.strip())
print(course.strip("!#.*"))
print(course.strip("!#.* "))


# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)