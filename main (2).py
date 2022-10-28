import numpy
import random
t=int(input("введите кол-во знаков после запятой t:"))
m = random.randint(1, 10)
suma=0
Matrix = numpy.array([ [ random.randint(1, 100) for j in range(m)] for i in range(m) ], dtype='float')
n=2
nf=2
print(Matrix)
while abs(numpy.linalg.det(Matrix*(n-1))/nf)>0.1**t:
    suma+=numpy.linalg.det(Matrix*(n-1))/nf
    n+=1
    nf=n*nf

print(round(suma, t))
