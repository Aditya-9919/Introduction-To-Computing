#Q.1
#printing result.
print("answer1")
m=int(input("Enter Marks :"))
if(m<25):
    print(" Grade F ")
elif(m>=25 and m<45):
    print(" Grade E ")
elif(m>=45 and m<50):
    print(" Grade D ")
elif(m>=50 and m<60):
    print(" Grade C ")
elif(m>=60 and m<80):
    print(" Grade B ")
elif(m>=80):   
    print(" Grade A ")
else:
    print(" No result ")

#Q.2
    print("answer2")
#printing nature of the year.
year = int(input("Enter a year: "))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("not a leap year")
else:
    print("leap year")
#Q.3
    print("answer3")
#printing random questions.
import random
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{num1}X{num2}="))
    if user_output == (num1*num2):
        print("Right!")
    else:
        print(f"Wrong.The right answer is {num1*num2}")
    

#Q.4
        print("answer4")    
x=200

for candies in range(x):

    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')
             break
