#i kathe sinartisi epistefei ton arithmo tis
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9

#i kathe sinartisi pairnei ws orisma to a k to b apo ta if kai epistrefeii epistrefei to simvolo tis
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def times(a,b):
    return a*b

#dilwnoume mia keni lista list=[], pernume apo ton xristi px.: seven(times(five())) k to vazei stnmetavliti praksi
#kai stn keni lista vazoume to praksi gia tn elegxo meta.
list=[]
praksi=input("dwse praksi: ")
for i in range (len(praksi)):
    list.append(praksi[i])

#elegxei gia to kathe stoixeio tis list an isoute to prwto orisma me ta grammata t kathe arithmou k kalei tn antistoixi sinartisi
#enw apothikevei to apotelesma stin metavliti a
if(list[0]=="z" and list[1]=="e"and list[2]=="r"and list[3]=="o") :
    a=zero()
elif(list[0]=="o"and list[1]=="n"and list[2]=="e"):
    a=one()
elif(list[0]=="t" and list[1]=="w"and list[2]=="o"):
    a=two()
elif(list[0]=="t" and list[1]=="h"and list[2]=="r" and list[3]=="e" and list[4]=="e"):
    a=three()
elif(list[0]=="f" and list[1]=="o"and list[2]=="u" and list[3]=="r" ):
    a=four()
elif(list[0]=="f" and list[1]=="i"and list[2]=="v" and list[3]=="e"):
    a=five()
elif(list[0]=="s" and list[1]=="i"and list[2]=="x"):
    a=six()
elif(list[0]=="s" and list[1]=="e"and list[2]=="v" and list[3]=="e" and list[4]=="n"):
    a=seven()
elif(list[0]=="e" and list[1]=="i"and list[2]=="g" and list[3]=="h" and list[4]=="t"):
    a=eight()
elif(list[0]=="n" and list[1]=="i"and list[2]=="n" and list[3]=="e"):
    a=nine()

#elegxei gia to kathe stoixeio tis list an isoute to trito orisma me ta grammata t kathe arithmou k kalei tn antistoixi sinartisi
#enw apothikevei to apotelesma stin metavliti b
for i in range(len(list)-7):
    if(list[i+4]=="z" and list[i+5]=="e"and list[i+6]=="r"and list[i+7]=="o"):
        b = zero()
for i in range(len(list)-5):
    if(list[i+3]=="o" and list[i+4]=="n"and list[i+5]=="e"):
        b = one()
for i in range(len(list)-5):
    if(list[i+3]=="t" and list[i+4]=="w"and list[i+5]=="o"):
        b = two()
for i in range(len(list)-9):
    if(list[i+5]=="t" and list[i+6]=="h"and list[i+7]=="r"and list[i+8]=="e"and list[i+9]=="e"):
        b = three()
for i in range(len(list)-7):
    if(list[i+4]=="f" and list[i+5]=="o"and list[i+6]=="u"and list[i+7]=="r"):
        b = four()
for i in range(len(list) - 7):
    if (list[i + 4] == "f" and list[i + 5] == "i" and list[i + 6] == "v" and list[i + 7] == "e"):
        b = five()
for i in range(len(list)-5):
    if(list[i+3]=="s" and list[i+4]=="i"and list[i+5]=="x"):
        b = six()
for i in range(len(list)-9):
    if(list[i+5]=="s" and list[i+6]=="e"and list[i+7]=="v"and list[i+8]=="e"and list[i+9]=="n"):
        b = seven()
for i in range(len(list)-9):
    if(list[i+5]=="e" and list[i+6]=="i"and list[i+7]=="g"and list[i+8]=="h"and list[i+9]=="t"):
        b = eight()
for i in range(len(list)-7):
    if(list[i+4]=="n" and list[i+5]=="i"and list[i+6]=="n"and list[i+7]=="e"):
        b = nine()

#elegxei gia to kathe stoixeio tis list to 2o orisma an isoute me ta grammata tis kathe praksis k kalei tn antistoixi sinartisi
#enw apothikevei to apotelesma stin metavliti c
for i in range(len(list)-4):
    if(list[i]=="p"and list[i+1]=="l"and list[i+2]=="u"and list[i+3]=="s"):
        c=plus(a,b)
for i in range(len(list)-4):
    if(list[i]=="m"and list[i+1]=="i"and list[i+2]=="u"and list[i+3]=="s"):
        c=minus(a,b)
for i in range(len(list)-4):
    if(list[i]=="t"and list[i+1]=="i"and list[i+2]=="m"and list[i+3]=="e"and list[i+4]=="s"):
        c=times(a,b)


#tipwnei to apotelesma tis praksis c
print(c)