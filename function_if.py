def max_of_two(a , b):
    if a > b:
        print("Using max of Two")
        print("Max is ",a)
    print("Using max of Two")
    print("Max is ",b)    

def max_of_three(a , b , c) :
    if a > b & a > c :
        print("Using max of Three")
        print("Max is ",a)
    elif b > a & b > c :
        print("Using max of Three")
        print("Max is ",b)
    print("Using max of Three")
    print("Max is ",c)      

def max_of_four(a , b , c, d) :
    if a > b & a > c & a > d :
        print("Using max of four")
        print("Max is ",a)
    elif b > a & b > c & b > d :
        print("Using max of four")
        print("Max is ",b)
    elif c > a & c > b & c > d :
        print("Using max of four")
        print("Max is ",c)
    print("Using max of four")
    print("Max is ",c)

     
max_of_two(9, 10)


max_of_three(5, 1, 7)


max_of_four(12, 6, 16, 4)

