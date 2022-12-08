#Multiplication of 2 matrix whose value is pre given

A=[[1,2],[2,3]]
B=[[1,3],[1,2]]

print("A Matrix is- ")

for i in range(len(A)):
    for j in range(len(B)):
        print(A[i][j], end = ' ')
    print()

print("B Matrix is- ")

for i in range(len(A)):
    for j in range(len(B)):
        print(B[i][j], end = ' ')
    print()

print("Multiplication of the Matrices -")

C=[]

for i in range(len(A)):
    a=[]
    
    for j in range(len(B)):
        m=0
        for k in range(len(B)):
            m+= A[i][k]*B[k][j]
        a.append(m)
    C.append(a)
print("The new Matrx is -")
for i in range(len(A)):
    for j in range(len(B)):
        print(C[i][j], end = ' ')
    print()
