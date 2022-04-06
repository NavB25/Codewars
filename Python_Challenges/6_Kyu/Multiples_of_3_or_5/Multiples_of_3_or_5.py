def solution(number):
    
    multiples = []

    if number < 0:
        return 0
    else:
        for num in range(1,number):
            if num % 3 == 0 and num % 5 == 0:
                multiples.append(num)
            elif num % 3 == 0:
                multiples.append(num)
            elif num % 5 == 0:
                multiples.append(num)
            else:
                continue
                
        return sum(multiples)
