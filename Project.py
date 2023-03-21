from datetime import datetime
date=datetime.now().strftime("%d-%b-%Y")
time=datetime.now().strftime("%I:%M %p")
print("\t\t------WELCOME TO PARKING STAND------\t\t")
print("----STANDARD PARKING WAGES----")
print("CAR-₹30 \nTRUCK-₹50 \nBIKE-₹10")
car=0
truck=0
bike=0
caramt=0
truckamt=0
bikeamt=0
tveh=0
tamt=0
str1=input("PLEASE ENTER YOUR NAME:")
while True:
    print("\n\nPRESS 1 TO ADD VEHICLE \nPRESS 2 TO REMOVE VEHICLE \nPRESS 3 TO SEE YOUR RECEIPT  \nPRESS 4 TO EXIT")
    n=int(input("\nCHOICE:"))
    if n==1:
        print("TOTAL CARS ADDED:",car)
        print("TOTAL TRUCKS ADDED:",truck)
        print("TOTAL BIKES ADDED:",bike)
        print("\nPRESS 1 FOR CAR \nPRESS 2 FOR TRUCK \nPRESS 3 FOR BIKE")
        x=int(input("WHICH VEHICLE YOU WANT TO ADD?:"))
        y=int(input('NUMBER OF SELECTED VEHICLES TO BE ADDED:'))
        print("VEHICLES ADDED SUCCESSFULLY!")
        if x==1:
            car+=y
            caramt+=y*30
            tveh+=y
            tamt+=y*30
        elif x==2:
            truck+=y
            truckamt+=y*50
            tveh+=y
            tamt+=y*50
        elif x==3:
            bike+=y
            bikeamt+=y*10
            tveh+=y
            tamt+=y*10
