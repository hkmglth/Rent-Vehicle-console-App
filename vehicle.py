import datetime
import os

class vehicle(object):

    def __init__(self,stock):
        self.stock = stock
        self.rented = 0

    def display(self):
        print(f"There are {self.stock} rental vehicles")
    
    def rentHourly(self,n):

        try:
            int(n)
        except ValueError: 
            print("Please enter a integer value !")
            return False

        if n < 0: 
            print("Error! It must be positive")
            return False
        elif n >= self.stock:
            print(f"Sorry {self.stock} vehicles can be rented")
            return None
        else:
            self.rentTime = datetime.datetime.now()
            print(f"You rented {n} vehicles for hourly at {self.rentTime.hour} hours")
            self.rented = 1
            self.stock -= n
            return self.rentTime

    def rentDaily(self,n):
        try:
            int(n)
        except ValueError: 
            print("Please enter a integer value !")
            return False

        if n < 0: 
            print("Error! It must be positive")
            return False
        elif n >= self.stock:
            print(f"Sorry {self.stock} vehicles can be rented")
            return None
        else:
            self.rentTime = datetime.datetime.now()
            print(f"You rented {n} vehicles for daily at {self.rentTime.day} day")
            self.rented = 1
            self.stock -= n
            return self.rentTime
    
    def returnVehicle(self,request,brand):

            time, typ, vehicle = request

            carHourly = 15
            carDaily = (carHourly*24)*0.6

            bikeHourly = 5
            bikeDaily = (bikeHourly*24)*0.8

            caravanDaily = (50*24) - (50*0.1) # caravan can rented just daily

            if brand == "car":
                self.stock += vehicle
                time = self.rentTime
                now = datetime.datetime.now()

                rentPeriod = now - time

                if typ == 1:# hourly
                    bill = (rentPeriod.seconds/3600)*carHourly*vehicle
                    
                    if vehicle >= 5:
                        print("You have %10 discount")
                        bill *= 0.9
                        print(f"Amount you have to pay ${bill}")

                    print(f"Amount you have to pay ${bill}")

                elif typ == 2:#daily
                    bill = (rentPeriod.seconds/3600)*carDaily*vehicle*24
                    
                    if vehicle >= 5:
                        print("You have %15 discount")
                        bill *= 0.85
                        print(f"Amount you have to pay ${bill}")
                    
                    print(f"Amount you have to pay ${bill}")

                else: print("Please enter 1 or 2")

            elif brand == "bike":
                self.stock += vehicle
                time = self.rentTime
                now = datetime.datetime.now()
                rentalPeriod = now - time

                if typ == 1:
                    bill = (rentalPeriod.seconds/3600)*bikeHourly*vehicle
                    if vehicle >= 3:
                        print("You have %20 discount")
                        bill *= 0.8
                        print(f"Amount you have to pay ${bill}")

                    print(f"Amount you have to pay ${bill}")

                elif typ == 2:
                    bill = (rentalPeriod.seconds/3600)*bikeDaily*vehicle*24
                    if vehicle >= 6:
                        print("You have %25 discount")
                        bill *= 0.75
                        print(f"Amount you have to pay ${bill}")

                    print(f"Amount you have to pay ${bill}")

                else: print("Please enter 1 or 2")
            else: #Caravan
                if typ == 2:
                    bill = caravanDaily*vehicle
                    if vehicle >= 1:
                        print("You have %15 discount")
                        bill *= 0.85
                        print(f"Amount you have to pay ${bill}")

class car(vehicle):

    def __init__(self,stock):
        super().__init__(stock)

class bike(vehicle):
    def __init__(self,stock):
        super().__init__(stock)

class caravan(vehicle):
    def __init__(self,stock):
        super().__init__(stock)

class customer(object):

    def __init__(self):
        self.cars = 0
        self.typeCars = 0
        self.timeCars = 0

        self.bikes = 0
        self.typeBikes = 0
        self.timeBikes = 0

        self.caravs = 0
        self.typeCaravs = 2
        self.timeCaravs = 0

    def request(self,brand):

        if brand == "car":
            cars = 0
            try:
                cars = int(input("How many cars would like to rent ? "))
            except ValueError:
                print("Please enter integer value")
            
            if cars <= 0:
                print("Number must be positive")
            else: 
                self.cars = cars
                return self.cars

        elif brand == "bike":
            bikes = 0
            try:
                bikes = int(input("How many bikes would like to rent ?"))
            except ValueError:
                print("Please enter integer value")
            
            if bikes <= 0:
                print("Number must be positive")
            else: 
                self.bikes = bikes
                return self.bikes

        elif brand == "caravan":
            caravs = 0
            try:
                caravs = int(input("How many caravans would like to rent ?"))
            except ValueError:
                print("Please enter integer value")
            
            if caravs <= 0:
                print("Number must be positive")
            else: 
                self.caravs = caravs
                return self.caravs

    def returnRequest(self,brand):

        if brand == "bike":
            if self.timeBikes and self.typeBikes and self.bikes: 
                return self.timeBikes, self.typeBikes, self.bikes

        elif brand == "car":
            if self.timeCars and self.typeCars and self.cars: 
                return self.timeCars, self.typeCars, self.cars
        
        elif brand == "caravan":
            if self.timeCaravs and self.typeCaravs and self.caravs: 
                return self.timeCaravs, self.typeCaravs, self.caravs

        else: print("Return vehicle error")

bike = bike(100)
car = car(150)
caravan = caravan(12)

customer = customer()

main_menu = True

while main_menu:

    print("Welcome to my python oop app :)\n")
    try:
        select = str(input("*** Vehicle Rent Shop *** \n A.Bike Menu \n B.Car Menu \n C.Caravan Menu \n D.Exit \n Choice: "))
    except ValueError: print("You should enter a string value")

    if select == 'a' or select == 'A':

        try: select = int(input("\n *** Bike Menu ***\n 1.Display available bikes \n 2.Request a bike hourly basis $5 \n 3.Request a bike daily basis $96 \n 4.Return bike \n 5.Main Menu \n 6.Exit \n Choice: "))
        except ValueError:
            print("Please enter integer value.")
            continue

        if select == 1:
            bike.display()
            
        elif select == 2:
            customer.timeBikes = bike.rentHourly(customer.request("bike"))
            customer.typeBikes = 1

        elif select == 3:
            customer.timeBikes = bike.rentDaily(customer.request("bike"))
            customer.typeBikes = 2

        elif select == 4:
            if bike.rented == 0:
                print("You dont rent vehicle please try again")
                continue
            else:
                bike.returnVehicle(customer.returnRequest("bike"),"bike")
                customer.timeBikes, customer.typeBikes, customer.bikes = 0,0,0

        elif select == 5:
            main_menu = True

        elif select == 6:
            break

        else: print("Please enter value between 1-6")
    
    elif select == 'b' or select == 'b':
        try: select = int(input("\n *** Car Menu ***\n 1.Display available cars \n 2.Request a car hourly basis $15 \n 3.Request a car daily basis $216 \n 4.Return car \n 5.Main Menu \n 6.Exit \n Choice: "))
        except ValueError:
            print("Please enter integer value.")
            continue

        if select == 1:
            car.display()
        elif select == 2:
            customer.timeCars = car.rentHourly(customer.request("car"))
            customer.typeCars = 1
        elif select == 3:
            customer.timeCars = car.rentDaily(customer.request("car"))
            customer.typeCars = 2
        elif select == 4:
            if car.rented == 0:
                print("You dont rent vehicle please try again")
                continue
            else:
                car.returnVehicle(customer.returnRequest("car"),"car")
                customer.timeCars, customer.typeCars, customer.cars = 0,0,0
        elif select == 5:
            main_menu = True
            continue
        elif select == 6:
            break
        else: print("Please enter value between 1-6")
    
    elif select == 'c' or select == 'C':
        try: select = int(input("\n *** Caravan Menu ***\n 1.Display available caravans \n 2.Request a caravan daily basis $216 \n 3.Return caravan \n 4.Main Menu \n 5.Exit \n Choice: "))
        except ValueError:
            print("Please enter integer value.")
            continue

        if select == 1:
            caravan.display()
        elif select == 2:
            customer.timeCaravs = caravan.rentDaily(customer.request("caravan"))
            customer.typeCaravs = 2
        elif select == 3:
            if caravan.rented == 0:
                print("You dont rent vehicle please try again")
                continue
            else:
                caravan.returnVehicle(customer.returnRequest("caravan"),"caravan")
                customer.timeCaravs, customer.typeCaravs, customer.caravs = 0,0,0
        elif select == 4:
            main_menu = True
            continue
        elif select == 5:
            break
        else: print("Please enter value between 1-6")

    elif select == 'D' or select == 'd':
        break

    else:
            print("Invalid input. Please enter A-B-C-D")
            main_menu = True
            continue

print("Thanks for use my rental vehicle shop :) Thats my first oop python app")



    


