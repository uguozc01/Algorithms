'''
Write a method/function that
* takes three integer values that represent the lengths of the three sides of a triangle, 
* and outputs a value that signifies the category of the triangle.

The possible categories of the triangle are
* equilateral
* isosceles
* right-angle
* scalene.
# (Some input combinations can indicate impossible/invalid triangles)
'''
#_________________________________________
# a == b == c -- equilateral
# a == b != c -- isosceles
# a != b and b != c and c != a  -- scalene
# sqrt(( a * a) + (b * b)) == c  -- right angle
#----------------------------------------------

import math

def isTriangle(side_list):

    # newlist = [s for s in side_list if s.isdigit()]
    if len(side_list) != 3:
        print(f'Bad input: {side_list}, please provide integers only!')
    else:
        a = side_list[0]
        b = side_list[1]
        c = side_list[2]
        if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a > 0 and b > 0 and c > 0:
            new = sorted(side_list)
            if new[2] < (new[0] + new[1]):
                if len(set((a,b,c))) == 1:
                    print(f'({a},{b},{c}) forms an equilateral')
                elif len(set((a,b,c))) == 2:
                    print(f'({a},{b},{c}) forms an isosceles')
                elif new[2] == math.sqrt( new[0] * new[0] + new[1] * new[1]):
                    print(f'({a},{b},{c}) forms a right angle')
                else:
                    print(f'({a},{b},{c}) forms a scalane ')
            else:
                print(f'{side_list} does not form a triangle at all!')
        else:
            print(f'Bad input: {side_list}, provide positive integers')

isTriangle([3,3,3])  # will yield equilateral
isTriangle([3,3,2])  # will yield isosceles
isTriangle([7,8,9])  # will yield scalene  
isTriangle([3,4,5])  # will yield right-angle
isTriangle([2,3,9])  # will not form a triangle
isTriangle([2147483647,2147483647,2147483648]) # boundary int limit
isTriangle([1,2,-1]) # negatif value test
isTriangle([0,1,2])  # zero value test
isTriangle([3.0, 4.0, 5.0])  # float value test
isTriangle([3, 4, 'a']) # alpha
isTriangle([1, '£$%!', 5]) # symbol
isTriangle([math.e, 3, 3]) # euler value (so float)