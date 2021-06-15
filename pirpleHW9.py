## HOMEWORK #9 - Classes
## Homework Assignment #9: Classes

## Details:
## Create a class called "Vehicle" and methods that allow you to set 
# the "Make", "Model", "Year,", and "Weight".
## The class should also contain a "NeedsMaintenance" 
# boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
## Next an inheritance classes from Vehicle called "Cars".
## The Cars class should contain a method called "Drive" 
# that sets the state of a boolean isDriving to True.  
# It should have another method called "Stop" that sets the value of isDriving to false.
## Switching isDriving from true to false should increment 
# the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, 
# then the NeedsMaintenance boolean should be set to true.
## Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, 
# and NeedsMaintenance to false.
## Create 3 different cars, using your Cars class, 
# and drive them all a different number of times. 
# Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, 
# and TripsSinceMaintenance
"""
## Extra Credit:
## Create a Planes class that is also an inheritance class from Vehicle. 
# Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), 
# but different in one respect: Once the NeedsMaintenance boolean gets set to true, 
# any attempt at flight should be rejected (return false), 
# and an error message should be printed saying that the plane can't fly until it's repaired.
"""

import random

class vehicle():
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False


class cars(vehicle):
    def __init__(self, make, model, year, weight ,isDriving = False):
        vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving
            
    def drive(self):
        self.isDriving = True

    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False

def driveCar(car):
    driveTime = random.randint(1, 101)
    for i in range(driveTime):
            car.drive()
            car.stop()       

def valueCar(car):
    print("="*30)
    print('Make ', car.make)
    print('Model ', car.model)
    print('Year ', car.year)
    print('Weight ', car.weight)
    print('Needs Maintenance ', car.needsMaintenance)
    print('Trips Since Maintenance ', car.tripsSinceMaintenance)
    print("="*35)

car1 = cars("Fiat", "kere", 1990, 1234)
car2 = cars("Honda", "ayla", 2000, 1023)
car3 = cars("BMW", "mini", 1988, 666)

driveCar(car1)
valueCar(car1)
driveCar(car2)
valueCar(car2)
driveCar(car3)
valueCar(car3)

