def fizzBuzz(n):
        for i in range (1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i %3 == 0 and i % 5 != 0:
                print('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                print ('Buzz')
            elif i % 3 != 0 or i % 5 != 0:
                print(i)

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except Exception as e:
        print(e)
    else:
        fizzBuzz(n)