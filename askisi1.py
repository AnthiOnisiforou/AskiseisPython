def sumintervals(lista1,lista2):
    spaces=0
    max = 0
    min =999999
    for i in range(len(lista1)):
        if (int(lista1[i]) > max):
            max = int(lista1[i])
    for i in range(len(lista2)):
        if (int(lista2[i]) > max):
            max = int(lista2[i])
    for i in range(len(lista1)):
        if (int(lista1[i]) < min):
            min = int(lista1[i])
    for i in range(len(lista2)):
        if (int(lista2[i]) < min):
            min = int(lista2[i])
    nums = []
    for i in range(max + 1):
        if(i>=min):
            nums.append(i)
    for i in range(len(lista1)):
        for j in range(int(lista1[i]),int(lista2[i])):
            for z in range(len(nums)):
#thetw tin thesi t kathe arithmou p tha metrisw ws -1 gia na kanw count ta -1.
                if(j==int(nums[z])):
                    spaces+=1
                    nums[z]=str(-1)
    #edw tipwnei ta stoixeia pou den mettrame diladi tn lista nums pou exei -1 ekeina p metrame
    # k ts arithmus p den metrame
    #tis listes opou lista 1 ta prota stoixia tis kathe listas t paradigmatos
    #kai opou lista 2 ta deftera stoixeia t paradeigmatos
    print(nums)
    print(lista1)
    print(lista2)
    return spaces
lista1=[]
lista2=[]
#dineis arithmous k otan theleis na stamatisei dineis tin timi "exit"
while(1):
    num1=input("give the num1(from 0 up to 999999): ")
    if(num1=="exit"):
        break
    num2=input("give the num2(from 0 up to 999999): ")
    if(num1>="0" and num2>="0"):
        lista1.append(num1)
        lista2.append(num2)
    else:
        print("you have to give numbers that are greater than 0")
print(sumintervals(lista1,lista2))