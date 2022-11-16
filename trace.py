A = [[1,2,1],[2,3,1],[1,1,1]]

B = [[4,5,6],[5,6,4],[1,1,1]]
ta=0
tb=None
#displaying martrix A
print("Matrix A-")
for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j],end = ' ')
    print()
print()
print("Matrix B")
#displaying matrix B
for i in range(len(B)):
    for j in range(len(B[0])):
        print(B[i][j],end = ' ')
    print()

print()


#multiplication of A B
if len(A[0])==len(B):
    print("The multiplied matrix AB is -")

    AB=[]

    for i in range(len(A)):
        a=[]
        for j in range(len(B[0])):
            m=0
            for k in range(len(A[0])):
                m+= A[i][k]*B[k][j]
            a.append(m)
        AB.append(a)

    #the AB matrix
    for i in range(len(A)):
        for j in range(len(B[0])):
            print(AB[i][j],end = ' ')
        print()

    #trace of AB matrix
    if len(AB)==len(AB[0]):
        print()
        ta=0
        for i in range(len(A)):
            ta+= AB[i][i]

        print("The trace of AB matrix is -",ta)
        print()
    else:
        print("Trace can not be calculated, Row is not equal to Column")

else:
    print("Multiplication can not be done since Column of A not equal to Row of B")


#multiplication of B A

if len(B[0])==len(A):

    print("The multiplied BA matrix is-")
    BA=[]

    for i in range(len(B)):
        a=[]
        for j in range(len(A[0])):
            m=0
            for k in range(len(B[0])):
                m+= B[i][k]*A[k][j]
            a.append(m)
        BA.append(a)

    #the BA matrix
    for i in range(len(B)):
        for j in range(len(A[0])):
            print(BA[i][j],end = ' ')
        print()
    #trace of BA matrix
    if len(BA)==len(BA[0]):
        print()
        tb=0
        for i in range(len(A)):
            tb+= BA[i][i]

        print("The trace of BA matrix is -",tb)
        print()
    else:
        print("Trace can not be calculated, Row is not equal to Column")

else:
    print("Multiplication can not be done since Column of B not equal to Row of A")
    
if ta==tb:
    print("Trace of [AB] = trace of [BA] Proved!")

