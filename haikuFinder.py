import re

'''
A haiku will contain only lowercase letters ('a'-'z'), forward slashes ('/'), and spaces, 
and will be no more than 200 characters long (not counting the end-of-row characters)
Write a function that returns Yes for each haiku line or No which is not haiku line e.g.
happy purple frog/eating bugs in the marshes/get indigestion  5,7,5,Yes
computer programs/the bugs try to eat my code/i will not let them 5,7,5 Yes
supercelestial/unconventionality/appendectomy 5,7,5
'''

def filter_haiku():
    with open('test_file.txt', 'r') as f:
        while True:
            row = f.readline()
            process_haiku(row)
            if not row:
                break
# I seperated every row as 3 lines(groups) and then every group into words and then by using every words counted syylables.
# It is O(n^2) operation which is not brilliant but if we want to consider counting syllables in words such as "code, make" as one syylable
# we need to consider looping through each word. Otherwise we do not have to iterate through words and we will have O(n) operation
def process_haiku(row):
    row_pattern = re.compile(r'([a-z][a-z ]+)/([a-z][a-z ]+)/([a-z][a-z ]+)')
    if len(row) > 0 and len(row.strip("\n")) <= 200 and len(re.findall('/', row)) == 2:
        haiki_row = re.match(row_pattern, row)
        if haiki_row:
            result = []
            isHaiku = False
            for i, group in enumerate(haiki_row.groups(), start=1):
                syllable_count_row = 0
                words = group.split()

                for word in words:
                    cs = count_syllables(word)
                    syllable_count_row += cs
                syllable_count_row = sum([count_syllables(word) for word in words])

                result.append(syllable_count_row)
                if i == 1 and syllable_count_row == 5:
                    isHaiku = True
                if i == 2 and isHaiku and syllable_count_row != 7:
                    isHaiku = False
                if i == 3 and isHaiku and syllable_count_row != 5:
                    isHaiku = False

            result.append("Yes") if isHaiku else result.append("No")
            return result
    else:
        return None

def count_syllables(word):
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e") and count > 1: # because "the" ends with e but "e" is only vowel sound in it
        count -= 1
    if word.endswith("le"):
        count += 1
    if word.endswith("ate") and word[-4:-3:1] in vowels:
        count += 1
    return count