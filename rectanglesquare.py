# solution to rectangles to squares
# https://www.codewars.com/kata/55466989aeecab5aac00003e

def sq_in_rect(lng, wdth):
    str_col = []
    if lng != wdth:
        tot_sq = lng * wdth
        while tot_sq != 0:
            i = min(lng, wdth)
            str_col.append(i)
            tot_sq -= i ** 2
            wdth = max(lng, wdth) - min(lng, wdth)
            lng = i
        return str_col
    return None


print(sq_in_rect(5,3))



# another solution

# def sqInRect(a, b):
#    if a != b:
#        n = []
#        while a > 0:
#            n.append(min(a,b))
#            a,b = max(a,b)-min(a,b),min(a,b)
#        return n
#    return None


# Recursive solution
# def sqInRect(lng, wdth, recur = 0):
#    if lng == wdth:
#        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
#                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
#    lesser = min(lng, wdth)
#    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)