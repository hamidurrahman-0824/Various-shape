
# for i in range(row+1):
#     print("v" * i)

#square
for i in range(1,6):
    for j in range(1,6):
        print("v",end="")
    print() #for one time run else it will run in i range
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
        print(" " *j+ "v"*i)
    print()