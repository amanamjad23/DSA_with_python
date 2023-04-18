def max_of_two(a , b):
    if a > b:
        return a
    return b
def max_of_three(a , b , c) :
    return max_of_two(max_of_two(a, b), c)
def max_of_four(a , b , c, d) :
    return max_of_two(max_of_three(a, b, c), d)
def max_of_six(a , b , c, d , e , f) :
    return max_of_two(max_of_three(a, b, c),max_of_three(d, e, f))

print("maximum among these numbers(6 , 8 , 10) are : ",max_of_three(6, 8, 10))