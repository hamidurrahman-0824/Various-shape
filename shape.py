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

polyline(5,5)