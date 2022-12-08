print("Input for the Matrix :-" )


i = int(input("Enter the number of rows-"))
j = int(input("Enter the number of column-"))


print("Enter the entries row wise")

M=[]

for a in range(i):
    a = []
    for b in range(j):
        a.append(int(input()))
    M.append(a)

print("The matrix is -")

for r in range(i):
    for t in range(j):
        print(M[r][t], end = ' ')
    print()
    
