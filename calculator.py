num_1=int(input("enter the number1:"))
num_2=int(input("enter the number2:"))
select=int(input("choose 1.addition/2.substraction/3.multiply/4.division:"))
if select==1:
    print(num_1,"+",num_2,"=",num_1+num_2)
elif select==2:
    print(num_1,"-",num_2,"=",num_1-num_2)
elif select==3:
    print(num_1,"*",num_2,"=",num_1*num_2)
elif select==4:
    print(num_1,"/",num_2,"=",num_1/num_2)
else:
    print("invalid input!")