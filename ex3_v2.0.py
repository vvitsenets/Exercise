import random
import numpy as np
import time

def generate_matrix_user():
    print("Enter N1:")
    n1=int(input())
    print("Enter M1:")
    m1=int(input())
    print("Enter N2:")
    n2=int(input())
    print("Enter M2:")
    m2=int(input())
    if n1<100 or n1>1000 or n2<100 or n2>1000 or m1<100 or m1>1000 or m2<100 or m2>1000:
        print("n and m must be in range 100-1000")
    array1 = np.random.rand(n1,m1)
    array2 = np.random.rand(n2,m2)
    return array1,array2
def generate_matrix():
    n=np.random.randint(100, 1000)
#     n=10000
    print(n)
    array1 = np.random.rand(n,n)
    array2 = np.random.rand(n,n)
    print(array1,array2)
    return array1,array2
def generate_matrix_and_vector():
    n=np.random.randint(100, 1000)
    print(n)
    array1 = np.random.rand(n,n)
    array2 = np.random.rand(n,1)
    return array1,array2
def generate_vectors():
    n=np.random.randint(100, 1000)
    print(n)
    array1 = np.random.rand(n,1)
    array2 = np.random.rand(n,1)
    return array1,array2
#     print(array1)
#     print(array2)
def matrix_na_vector_multiply(array1,array2):
    for i in range(len(array2)):
        sum=0
        for j in range(len(array2)):
            sum+=array1[i,j]*array2[j]
#         print(h,"  ",i,"  ",j,"  ",sum)
        res.append(sum)
#     return res  
def matrix_multiply(array1,array2):
    for h in range(len(array2)):
        for i in range(len(array2)):
            sum=0
            for j in range(len(array2)):
                sum+=array1[h,j]*array2[j,i]
#             print(h,"  ",i,"  ",j,"  ",sum)
            res.append(sum)
#     print(res)
def vector_multiply(array1,array2):
    for i in range(len(array2)):
        sum=0
        for j in range(len(array2)):
            sum+=array1[i]*array2[j]
        res.append(sum)
#     print(res)
if __name__ == '__main__':
    res=[]
    array1,array2=generate_matrix()
#     matrix_na_vector_multiply(array1,array2)
#     vector_multiply(array1,array2)
    start_time = time.time()
    matrix_multiply(array1,array2)
    print("using for - %s seconds" % (time.time() - start_time))
    start_time = time.time()
    array1@array2
    print("using default python method @ - %s seconds" % (time.time() - start_time))
    start_time = time.time()
    np.dot(array1,array2)
    print("using np.dot - %s seconds" % (time.time() - start_time))