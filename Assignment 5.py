
#question-1------------------------------------------------------------------------------------------------------------------

def reverse(s):              #define the reverse function
    str = ""
    for i in s:               #using loop to reverse the string
        str = i+str
    return str

s= input("write the string:")
print("original string:",s)
print("reversed string is:",reverse(s) )

#question-2-------------------------------------------------------------------------------------------------------------------
print("ANS.2")
x=int(input("Enter the minimum value :"))
y=int(input("Enter the maximum value: "))
num=int(input("Enter the number for divisibility check :"))
i=x
while i<=y:
    if i%num==0 :
        print(i)
    i+=1

#question-3--------------------------------------------------------------------------------------------------------------------
print("ANS.3")
a=float(input("Enter the length of side:"))
b=float(input("Enter the length of side:"))
c=float(input("Enter the length of side:"))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    ar_tri=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(ar_tri)
else :
    print("Error")


#question-4--------------------------------------------------------------------------------------------------------------------
print("ANS.4")
n=int(input("Enter no of rows"))
for i in range(1,n):
    if i<6:
        k = i
    else:
        k = 10-i
    for j in range(1,n//2+1):
        if j<=k:
            print("*",end="")
    print()



#question-5---------------------------------------------------------------------------------------------------------------------
print("ANS.5")
row=int(input("enter row"))
k=0
for i in range(1,row):
    
    for j in range(1,i+1):
        if j<=i:
            if k<26:
                print(chr(65+k),end="")
            else:
                k=0
                print(chr(65+k),end="")
           
            k+=1
    print()





#question-6---------------------------------------------------------------------------------------------------------------------------------
print("ANS.6")
lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    # input from user the lowest and the upper range
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                           # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:                             # if YES, the code will move on
                break       
        else:  
            print (number)                                    # if NO, the code prints the number




#question-7---------------------------------------------------------------------------------------------------------------------------------
print("ANS.7")
accum=[]
for i in range(1,500):
    if i%7==0 and i%11==0 :
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :",accum)        




#question-8----------------------------------------------------------------------------------------------------------------------------------
print("ANS.8")
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number "))
    li.append(num)
    if num>=0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)




#question-9---------------------------------------------------------------------------------------------------------------------------------------
print("ANS.9")
n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)
