import itertools

# Write a function that takes in two arrays of integers and 
# finds the pair of numbers (one from each array) whose |abs|
# difference is the closest to zero. Give output as an array.
# array1 = [-2, 5, 11, 21, 29, 4]
# array2 = [ 27, 135, 136, 16, 18]
# sample output is [29, 27]

def findDiff(arrayOne, arrayTwo):
    # Write your code here.
    smallest = float("inf")
    tempArray = list(itertools.product(arrayOne, arrayTwo))
    smallestPair = []
    for firstNum, secondNum in tempArray:
        delta = abs(firstNum - secondNum)
        if smallest > delta:
            smallest = delta
            smallestPair = [firstNum, secondNum]
    return smallestPair