# solution to find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836/

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

print(find_it())