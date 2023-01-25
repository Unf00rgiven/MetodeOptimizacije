import math

#faktorijel broja N!
#N1=1*2*3*4*...*(N-1)*N

########################################
#Upotreba FOR petlje
N=6
f=1
for i in range(1, N+1):
    f=f*i
print ("Faktorijel broja "+str(N)+" je: " +str(f))


########################################
#Upotreba WHILE  petlje
N=6
f=1
i=1
while i<=N:
    f=f*i
    i=i+1

print ("Faktorijel broja "+str(N)+" je: " +str(f))