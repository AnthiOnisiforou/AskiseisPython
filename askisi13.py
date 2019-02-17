def bubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
#edw prepei na vriskei to megalitero athroisma pou na einai mikrotero i ison apo ton arithmo X
#den einai aparaitito na einai diadoxika ta stoixeia afta
def maxDistance(lista,x):
    max=0
    sum=0
    l=[]
    bubbleSort(lista)
    for i in range(len(lista)):
        sum+=int(lista[i])
        if (sum == x):
            break
        if(sum<x):
            l.append(lista[i])
    return l
#dinei lista diadoxika tous arithmous(enan-enan) gia na staamatisei i eisodos prepei na grapeis exit
lista=[]
while(1):
    num=input("dwse num:")
    if(num=="exit"):
        break
    lista.append(int(num))
#o arithmos x einai o akeraios pou tha sigkrinei to athroisma stn sinaρtisi maxDistance
x =int(input("dwse x:"))
b= maxDistance(lista,x)
print(b)