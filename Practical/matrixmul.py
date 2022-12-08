
#Multiplication of 2 matrices

print("Input for the Matrix :-" )

#input for the first matrix
i = int(input("Enter the number of rows-"))
j = int(input("Enter the number of column-"))


print("Enter the entries row wise")

A=[]

for a in range(i):
    a = []
    for b in range(j):
        a.append(int(input()))
    A.append(a)

print("Matrix A is -") 

#display of A matrix
for r in range(i):
    for t in range(j):
        
        print(A[r][t], end = ' ')
    print()

#input for the second matrix

i = int(input("Enter the number of rows-"))
j = int(input("Enter the number of column-"))


print("Enter the entries row wise")

B=[]

for a in range(i):
    a = []
    for b in range(j):
        a.append(int(input()))
    B.append(a)

print("Matrix B is -")

#display of B matrix

for r in range(i):
    for t in range(j):
        
        print(B[r][t], end = ' ')
    print()
    
#Multiplication of above matrices

print("Multiplication of the Matrices -")

C=[]

for i in range(len(A)):
    a=[]
    
    for j in range(len(B[0])):
        m=0
        for k in range(len(A[0])):
            m+= A[i][k]*B[k][j] # formula for matrix multiplication
        a.append(m)
    C.append(a)

print("The new Matrx is -") #new matrix
#display of new matrix
for i in range(len(A)):
    for j in range(len(B[0])):
        print(C[i][j], end = ' ')
    print()

            
