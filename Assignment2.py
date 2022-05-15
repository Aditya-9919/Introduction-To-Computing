#Q.1
#(a)
inputstr = input("Enter the string : ")
length = len(inputstr)
print("Length of the given string: ",length)
#(b)
rstr = inputstr[length: :-1]
print("Reverse string: ",rstr)
#(c)
nstr = inputstr[10:26]
print("New string:",nstr)
#(d)
replacestr = inputstr.replace("a case sensitive","object oriented")
print("New replaced string :", replacestr)
#(e)
index = inputstr.find("a")
print("Index of 'a':",index)
#(f)
wstr = inputstr.replace(" ","")
print("String without white spaces :",wstr)

#Q.2
name = input("Enter your name :") 
sid = int(input("Enter your sid :"))
dep = input("Enter your department :")
cgpa = float(input("Enter your cgpa :"))
print(f"Hey, {name} Here!")
print(f"My SID is {sid}")
print(f"I am from {dep} department and my CGPA is {cgpa}")

#Q.3
a = 56
b = 10
print("a&b :", (a&b))
print("a|b :", (a|b))
print("a^b :", (a^b))
print("Left shift both a and b with 2 bits : a = %d, b = %d", (a << 2,b << 2))
print("Right shift a with 2 bits and b with 4 bits : a = %d, b = %d", (a >> 2,b >>4))

#Q.4
s = input("Enter a string")
s1 = s.lower()
if "name" in s1:
    print("Yes")
else:
    print("No")
#Q.5
num1 = int(input())
num2 = int(input())
num3 = int(input())

while num1+num2<=num3 or num3+num1<=num2 or num2+num3<=num1:
    print("No")
    break
while num1+num2>num3 and num1+num3>num2 and num2+num3>num1:
    print("Yes")
    break
#Q.6
s1 = int(input("Enter number a:"))
s2 = int(input("Enter number b:"))
count = 0
while(s1>0 or s2>0):
    temp1 = s1&1
    temp2 = s2&1
    if temp1!=temp2:
        count+=1
    s1 = s1>>1
    s2 = s2>>1

print(count)



 
             
