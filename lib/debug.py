#!/usr/bin/env python3
import ipdb
from random import choice as rc, randint

from classes.many_to_many import Customer, Flight, Booking

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Customers
    c1 = Customer("Sara", "Hamersly")
    c2 = Customer("Sammy", "Jackson")
    c3 = Customer("Bobbi", "Dee")
    c4 = Customer("Tim", "Grey")
    c5 = Customer("Jeff", "Bezos")

    # Flights
    f1 = Flight("American Airlines")
    f2 = Flight("Delta Air Lines")
    f3 = Flight("British Airways")
    f4 = Flight("Southwest Airlines")
    f5 = Flight("Alaska Airlines")
    f6 = Flight("Spirit Airlines")
    f7 = Flight("Emirates")
    f8 = Flight("United Airlines")
    f9 = Flight("Air Canada")
    f10 = Flight("Air France")

    # Combine flights and destinations
    FLIGHTS = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    destinations = ["Los Angeles", "Baltimore", "London", "Chicago", "New York"]

    flights = [Flight(airline=f"{rc(FLIGHTS).airline} {dest}") for dest in destinations]

    # Bookings with customer names, flight details, and cost
    customers = [c1, c2, c3, c4, c5]
    bookings = [Booking(customer=rc(customers), flight=rc(flights), price=randint(500, 3000)) for i in range(5)]

    ipdb.set_trace()
