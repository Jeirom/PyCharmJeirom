def number_double(x):
    return [x,x]

result = list(map(number_double, range(10)))
print(result)



result = [x for num in range(20) for x in [num, num] if num % 2 == 0]

cubes = [x*x for x in range(11) if x % 2 == 0]
print(cubes)

ssps = [1,2,3,4,5,6,7,8,9,10]

summa = [x*2 for x in ssps if x > 0]
print(sum(summa))

vowels = (x for x in "hello" if x in ['a', 'e', 'i', 'o', 'u'])




import random

def random_number_generator(start, stop):
    while True:
        yield random.randint(start, stop)

