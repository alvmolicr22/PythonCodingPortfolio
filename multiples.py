# solution to multiples of 3 or 5
# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    number_list = []
    if number < 0:
        return 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            number_list.append(i)
    return sum(number_list)

a = solution(-10)
print(a)


 # def solution(number):
 #   return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)