"""
Cracking the Coding Interview 7.3
Parking Lot: Design a parking lot using object-oriented principles.

1) Scoping:
    a) Who: is this parking lot for?
        - ASSUME it's for a small plaza containing:
            - ma and pop convenience store
            - a small pizza rest.
        - ASSUME we only need to support regular-sized
            1) cars, vans, pickup trucks  
            2) number of people per vehical - 3-4
    b) What:
        - used for people to come in,
        - leave their car (for free) at one of the available spots
        - then they come back and leave the lot
    c) Where:
        - located by a backroad in a suburban town
        - high traffic near lunchtime and holidays
        - only one exit/enter between lot and the road
    d) HOW:
        - no double parking

2) Core Objects:
    a) Vehicle
        a) Properties:
            a) entrance time
            b) license
            c) parking_space: coordinates
        b) Subclasses:
            i). Car, PickupTruck, Van
    b) ParkingLot
        a) parking_spaces: 2D array
            A = available - null value
            V = vehicle - store license
                |STORE|
            [AAAAAAAAAAV]
            [AAAAAAAAAAA]
            [AAAAVVVAAAV]
                            | ENTER |
                                ^
                                | <--- ROAD
        b) Methods:
            a) hasSpaceAvailable()
                - return bool
                - global

3) Analyze Relationships:
    a) TODO

4) Actions:
    1) Cars Enter the Lot: --> Vehicle method, modifies the Lot object
        a) if lot.hasSpaceAvailable():
            a) car traverse the grid from the top ---> get the first space, put the id there
            b) modify the car's entrance_parking space property
            c) if sucessfuly:
                return the coordinate where car is sotred
            d) others:
                return a null

    2) Cars Exit --> Vehicle method, modifies the Lot object
        a) car.exit(lot)
            1) check the car's parking_space coords
                  a) is that space in the lot
                - b) is its license num in the given lot object?
            2) if so:
                change the car's space to "Available"
                set the car's space prop to null

"""
