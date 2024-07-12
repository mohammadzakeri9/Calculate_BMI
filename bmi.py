#This program can calculate bmi
import decimal
import math

while True:
    print("Enter your choice: "
    "\n\t1:calculate bmi"
    "\n\t2:Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        height = int(input("Enter your height(cm): "))
        height = height/100
        weight = int(input("Enter your weight(kg): "))
        bmi = (weight/(height*height))
        print("\n********************")
        print("\nyour bmi=>","%.2f"%bmi)

        if bmi < 18.5:
            print("\nUnderweight!")
            print("\n********************")

        elif bmi > 18.5 and bmi <= 24.9:
            print("\nGood weight!")
            print("\n********************")

        elif bmi > 25 and bmi <= 29.9:
            print("Overweight!")
            print("\n********************")

        elif bmi >= 30:
            print("Fat")
            print("\n********************")

    elif choice == 2:
        print("\n********************")
        print("code closed!")
        print("\n********************")
        exit(0)

    else:
        print("\n********************")
        print("not found!")
        print("\n********************")
        exit(0)