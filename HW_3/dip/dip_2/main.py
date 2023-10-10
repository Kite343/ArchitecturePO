from diesel import Diesel
from petrol import Petrol
from car import Car


if __name__ == '__main__':
    diesel_car = Car('diesel car', Diesel())
    petrol_car = Car('petrol car', Petrol())
    print(diesel_car)
    diesel_car.start()
    print(petrol_car)
    petrol_car.start()