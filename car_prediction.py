import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
global v # wife working variable 
df=pd.read_csv("C:/Users/VINAY/Desktop/car_modified.csv")

print("Enlighten us with ur education Details")
print("Press 1 for Graduate:")
print("enter 2 for Post Graduate")

z=int(input())
if z==1:
   df= df[df["Education"]=="Graduate"]
   print("in graduate")
else:
   df= df[df["Education"]=="Post Graduate"]
   print("in pg")

print("Enlighten us with ur Profession Details")
print("Press 1 for Business:")
print("enter 2 for Salaried")

y=int(input())

if y==1:
    df=df[df["Profession"]=="Business"]
    print("in business:")
else:
    df=df[df["Profession"]=="Salaried"]
    print("in salary")




print("Enlighten us with ur Marrital Status Details")
print("Press 1 for Married:")
print("enter 2 for single")

x=int(input())

if x==1:
    c=df[df["Marrital Status"]=="Married"]
    v=1
    print("in married:")
else:
    v=0
    c=df[df["Marrital Status"]=="Single"]
    print("in single")
 
   
if v==1:
    print("Press 1 if ur wife working")
    print("Press 2 if ur wife not working ")
    w=int(input())
    if w==1:
       
        df=df[df["Wife Working"]=="Yes"]
        print("wife work")
        
    else:
        df=df[df["Wife Working"]=="No"]
        print("wife not work")



print("Enlighten us with ur Loan Status Details")
print("Press 1 if u have any loans:")
print("enter 2 if u dont have any loans ")

loan_checker=int(input())
if loan_checker==1:
    print(" press 1 if u have personal loan")
    print("Press 2 if u have house loan ")
    print( "Press 3 if u have both ")
    loan_type=int(input())
    if loan_type==1:
    
        df=df[df["Personal loan"]=="Yes"]
        df=df[df["House Loan"]=="No"]
    elif loan_type==2:
        df=df[df["Personal loan"]=="No"]
        df=df[df["House Loan"]=="Yes"]
    else:
        df=df[df["Personal loan"]=="Yes"]
        df=df[df["House Loan"]=="Yes"]
    
else:
    df=df[df["Personal loan"]=="No"]
    df=df[df["House Loan"]=="No"]

print("Enlighten us with ur Total_Salary Details")
print("Press 1 if <5Lakhs:")
print("enter 2 if 5-10Lakhs ")
print("enter 3 if 11-15Lakhs ")
print("enter 4 if >15 lakhs")

salary_checker=int(input())
if salary_checker==1:
    df=df[df["Total Salary(Lakhs)"]<5.0]
elif salary_checker==2:
    df=df[(df["Total Salary(Lakhs)"]>5.0)& (df["Total Salary(Lakhs)"]<10.0)]
elif salary_checker==3:
    df=df[(df["Total Salary(Lakhs)"]>11.0)& (df["Total Salary(Lakhs)"]<15.0)]
elif salary_checker==4:
    df=df[df["Total Salary(Lakhs)"]>15.0]
else:
    print("enter correct choice")



################################################################################
labels = list(df["Make"])
final_list=[]
sizes=[]
for num in labels: 
        if num not in final_list: 
            final_list.append(num)
for i in final_list:
   sizes.append(len(df[df["Make"]==i]))



# Plot
plt.pie(sizes,  labels=final_list, 
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()




