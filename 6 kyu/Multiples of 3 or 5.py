def solution(number):
    return sum([x for x in range(1,number) if x%5==0 or x%3==0])
