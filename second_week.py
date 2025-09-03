
# for i in range(row+1):
#     print("v" * i)

#rectangle
for i in range(1,6):
    for j in range(1,6):
        print("v",end="")
    print() #for one time run else it will run in i range
print()
#rectangle_2
for i in range(6):
    for j in range(6):
        print("b", end= "")
    print()

#triangle
for i in range(1,6):
    print("v"*i)
print()
#upper_triangle
#for i in range(1):
    
for j in range(5,0,-1):
    print("v"*j)
print()
#right_handed triangle
for i in range(1):
    for j in range(5,0,-1):
        print("#")
    print()
for i in range(1):

    for j in range(5):
        print(" " *j + "*" )
    for k in range(1,i+1):
        print("*",end= "")
for j in range(5):
    print(" " * (4 - j) + "*")
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end="")
        else:
            print(" ", end= "")
    print()
rows = 5

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
row= 5
for i in range(1,6):
    if i==3:
            print("* *")
    elif i== 4:
        print("*  *")
    else:
       print("*"*i)
row= 5
for i in range(1,row+1):
    if i == 1:
        print("*")
    elif i == row:
        print("*"*row)
    else:
        print("*"+" "*(i-2)+"*")
