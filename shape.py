# row = 5
# for i in range(5):
#     print("*"*i)
# x = 5 
# for k in range (x-1,0,-1):
#     print("*" * k)
# row = 5
# for i in range (1, row+1):
#     print(" " * (row-i) + "*" *(2*-1))
# rows = 5
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2*i - 1))
def polyline(r,c):
    for i in range(1,r+1):
        for _ in range(c-i):
            print(" ",end="")
        print("*"*i)
def downward(row,col):
    for r in range(1,row+1):
        for _ in range(r):
            print(" ",end= " ")
        print(" *"*r)
# downward(5,5)
def upward(rw,co):
    for r in range(1,rw+1):
        for _ in range(r-1):
            print("",end = " ")
        print(" *"*(co-r))
# tt(4,4)
def polys(row,col,alignment = "pyramid" ):
    for r in range(1,row+1):
        if alignment =="pyramid":
            print(" "* (col-r),end="")
        elif alignment == "triangle":
            pass
        print(" *"*r)
# polys(5,5,"pyramid")
def downward(row, col, align="pyramid"):
    for r in range(1, row + 1):
        if align == "pyramid":
            # add spaces for pyramid alignment
            print(" " * (col - r), end="")
        elif align == "triangle":
            # no spaces for left-aligned triangle
            pass  
        print(" *" * r)

# Example usage:
# downward(5, 5, "pyramid")   # prints pyramid
def home(he,wi):
    for h in range(1,he+1):
        for _ in range(wi - h):
            print(" ",end = "")
        print(" *"*h)
    for _ in range(1,he+1):
        for _ in range(wi+1):
            print("*",end=" ")
        print()
home(5,5)
upward(6,6)
