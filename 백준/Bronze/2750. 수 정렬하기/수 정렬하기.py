N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))


#버블 정렬
for j in range(N-1):
    for i in range(N-1-j):
        if array[i]>array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
        
for i in range(N):        
    print(array[i])