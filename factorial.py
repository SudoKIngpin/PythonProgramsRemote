##'''Program for calclating trailing zeroes  in python'''

fact=1
num=int(input("Enter no :"))
for i in range(1,num+1):
    fact=fact*i
print("Factorial of given number is :",fact)
fact1=str(fact)
print(fact1)
ct=0
for i in fact1:
    if i=='0':
        ct+=1
print("Given factorial contains",ct,'trailing zeroes ')
