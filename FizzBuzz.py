##https://open.kattis.com/problems/fizzbuzz
def FizzBuzz():
    s = input()
    x,y,n = map(int, s.split())
        
    x = int(x)
    y = int(y)
    n = int(n)
    xcheck = 0
    ycheck = 0
    for i in range(1,n+1):
        if i%x == 0:
            xcheck = 1
        if i%y == 0:
            ycheck = 1

        if xcheck == 1 and ycheck == 1:
            print("FizzBuzz")
        elif xcheck == 1 and ycheck == 0:
            print("Fizz")
        elif xcheck == 0 and ycheck == 1:
            print("Buzz")
        else:
            print(i)
        xcheck = 0
        ycheck = 0
FizzBuzz()