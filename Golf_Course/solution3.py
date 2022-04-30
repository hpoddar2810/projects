from logging import raiseExceptions
from tkinter import SEL_FIRST
from solution1 import Course, Hole
from Solution2 import Flight, GolfingException, PCHolder, HandicappedGolfer, Golfer
from datetime import datetime
from os import path


class GolfClub():
    """
    Class variable: 
        _TEE_SLOTS (list) : a List containing the 6 initial tee slots/times that are available for booking.
    """
    _TEE_SLOTS = ["07:08", "07:18", "07:28", "07:38", "07:48", "07:58"]

    def __init__(self, name, course, golfingDate):

        """
        Input :
            name (str) : name of golf club
            course (Course Object) : course object in club
            golfingDate (datetime) : Date of bookings


        Instance variables: 
            _name (str): the name of the golf club.
            _golfers (Dictionary): collection of all golfers for this golf club. The key for this dictionary is the memberID, and the value is the Golfer object.
            _course (Course): the course that Fantasy Golf Club 
            _bookings (Dictionary): The key for this dictionary is the tee slot/time, and the value is the Flight object that has booked this tee slot/time.
            _golfingDate (datetime): this is the golfing date for which golfers/members can submit their bookings for.
        """

        self._name = name
        self._course = course
        self._golfingDate = golfingDate
        self._golfers = {}
        self._bookings = {key : None for key in GolfClub._TEE_SLOTS}

    
    """
    Getter method for the instance variable _golfingDate
    """
    @property
    def golfingDate(self):
        return self._golfingDate


    """
    Getter method for the instance variable _course
    """
    @property
    def course(self):
        return self._course



    def setupGolfers(self, fileName):

        """
        Input : 
            fileName (str) : File name of golfers data
        
        Do :
            Read the content of the given file to setup all the golfers into the dictionary _golfers
        """

        with open(fileName, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            li = line.split(',')

            if len(li) == 3:
                golfer = HandicappedGolfer(li[0], li[1], float(li[2]))
            else:
                golfer = PCHolder(li[0], li[1], datetime.strptime(li[3].rstrip(), "%d-%b-%Y"))
            
            key = golfer.memberID

            self._golfers[key] = golfer


    def searchGolfer(self, memberId):

        """
        Input 
            memberId (int) : member Id of a golfer
        
        Do : 
            Searches and returns the Golfer object matching this memberID. If not found, the method returns None.
        """
        return self._golfers[memberId] if memberId in self._golfers else None
    

    def searchBooking(self, teeTime):
        """
        Input :
            teeTime (str) : tee time for search booking
        
        Do :
            Searches and returns the Flight object playing at this tee slot/time. If no flight has booked this tee slot/time, the method returns None
        """
        return self._bookings[teeTime] if teeTime in self._bookings else None


    def searchMemberBooking(self, memberId):
        """
        Input :
            memberId (int) : member Id to search booking for
        
        Do :
            Searches and returns the tee slot/time (str) that this member has a booking for. If this member has no booking, the method returns None.

        """
        for teeTime in self._bookings.keys():
            if self._bookings[teeTime] and self._bookings[teeTime].searchGolfer(memberId):
                return teeTime
        return None
    


    def addBooking(self, teeTime, flight):
        """
        Input :
            teeTime (str) : tee time for add booking
            flight (Flight Object) :  Flight object of golfers to add booking for
        
        Do : 
            After validating all checks, it allowing this flight to “book” this tee slot/time:
        """

        if teeTime not in self._bookings:
            raise GolfingException("There is no such tee slot/time")
        
        if self._bookings[teeTime] != None:
            raise GolfingException("Tee slot/time is already booked by another flight")
        
        golferIds = flight.getGolfersID()

        for golferId in golferIds:
            if self.searchMemberBooking(golferId):
                raise GolfingException("Booking has failed as one member already has another booking")
        
        if self._golfingDate.weekday() > 4 and not flight.getWeekendEligibility():
            raise GolfingException("Given Flight do not have weekend eligibility")
        
        self._bookings[teeTime] = flight


    def cancelBooking(self, teeTime):
        """
        Input :
            teeTime (str) : tee time for cancel booking
        
        Do :
            After validating checks, its cancels the booking at the given tee time
        """

        if teeTime not in self._bookings:
            raise GolfingException("There is no such tee slot/time")
        
        if self._bookings[teeTime] == None:
            raise GolfingException("Tee slot/time has no booking to be cancelled")

        self._bookings[teeTime] = None
    

    def getBookings(self):
        """
        Returns a string representing all tee slot/time and the memberID of the flight of golfers (if booked), or “no booking” is tee slot/time is not booked.
        """
        print()

        for teeTime in self._bookings.keys():
            output = teeTime + " - "

            if self._bookings[teeTime] == None:
                print(output + "no booking")
            else:
                flight = self._bookings[teeTime]
                print(output, flight.getGolfersID())
        
        print()
    
    def getEmptyTeeTimes(self):
        """
        Returns a list of tee slots/times that is not booked.
        """

        return [key for key in self._bookings.keys() if self._bookings[key] == None]







def application():
    GolfClub._TEE_SLOTS.extend(["08:08", "08:18", "08:28"])

    course_file = input("\nEnter course filename: ")
    while not path.exists("data/" + course_file):
        print("File : data/", course_file, " does not exists. Please enter valid file name")
        course_file = input("Enter course filename: ")

    got_date = False
    while not got_date:
        date = input("Enter golfing date in dd/mm/yyyy: ")
        try:
            date = datetime.strptime(date, "%d/%m/%Y")
            got_date = True
        except:
            print("This is the incorrect date string format. It should be dd/mm/yyyy")


    Fantasy_Golf_Club = GolfClub("Club1", Course(course_file), date)
    Fantasy_Golf_Club.setupGolfers('data/golfer.txt')

    data = [
        ["07:28", [21, 57, 58, 5]],
        ['07:48', [8, 11, 17]],
        ["07:58", [9, 27, 34]]
            ]
    
    for teeTime, memberIDS in data:
        golfer_data = [ Fantasy_Golf_Club._golfers[memberID] for memberID in memberIDS ]
        flight = Flight(golfer_data)

        Fantasy_Golf_Club.addBooking(teeTime, flight)

    print("""
Golf Booking for \033[;;42m 01-May-2022 Sunday: \x1b[0m
======================================
1. Submit Booking
2. Cancel Booking
3. Edit Booking
4. Print play schedule
5. Overview of Tee Schedule
0. Exit
"""
    )

    i = input("Enter option: ")
    while not i.isdigit() or not (-1 < int(i) < 6):
        i = input("Enter a valid option[0-5] : ")
    
    if int(i) == 1:
        submit_booking(Fantasy_Golf_Club)
    
    elif int(i) == 2:
        cancel_booking(Fantasy_Golf_Club)
    
    elif int(i) == 3:
        edit_booking(Fantasy_Golf_Club)
    
    elif int(i) == 4:
        print_schedule(Fantasy_Golf_Club)
    
    elif int(i) == 5:
        print_overview(Fantasy_Golf_Club)
    
    else:
        exit()
    

def input_golfers():
    memberIds = []
    for i in range(4):
        memberId = int(input("Enter ID for golfer {i+1} or -1 to stop: "))
        
        if memberId == -1:
            return memberIds
        
        memberIds.append(memberId)
    

def validate(golfclub, memberIds):
    if len(memberIds) < 3 or len(memberIds) > 4:
        print(f"Flight should have atleast 3 and atmost 4 golfers")
        return False
    
    for memberId in memberIds:
        if not golfclub.searchGolfer(memberId):
            print(f"Golfer {memberId} is not a member of the club")
            return False
        
        elif not golfclub.searchMemberBooking(memberId):
            print(f"Golfer {memberId} already have a booking.")
            return False
    
    golfer_data = [ golfclub._golfers[memberID] for memberID in memberIds ]
    flight = Flight(golfer_data)

    if golfclub.golfingDate.weekday() > 5 and not flight.getWeekendEligibility():
        print(f"Flight don't have eligibility to play on {golfclub.golfingDate}")
        return False
    
    return Flight


def submit_booking(golfclub):
    print("""
Enter 3 or 4 golfers to form a flight
=====================================
    """)

    valid_memberIds = False
    while not valid_memberIds:
        memberIds = input_golfers()

        if len(memberIds) == 0:
            return

        valid_memberIds = validate(golfclub, memberIds)

    
    print("""
List of available tee times
=========================
    """
    )

    available_teeTime = golfclub.getEmptyTeeTimes()
    
    for i, teeTime in enumerate(available_teeTime):
        print(f"{i+1} : {available_teeTime[i]}")
    
    i = int(input("Enter Selection : "))

    golfer_data = [ golfclub._golfers[memberID] for memberID in memberIds ]
    flight = Flight(golfer_data)

    if golfclub.golfingDate.weekday() > 5 and not flight.getWeekendEligibility():
        print(f"Given golfers flight don't have eligibility to play on {golfclub.golfingDate}")
        submit_booking(golfclub)
    else:
        golfclub.addBooking(available_teeTime[i-1], flight)
        print(f"Tee time {available_teeTime[i-1]} booked for flight with golfers {memberIds}")


def cancel_booking(golfclub):

    print("\n")
    memberId = int(input("Enter member ID to cancel booking: "))

    if not golfclub.searchGolfer(memberId) or not golfclub.searchMemberBooking(memberId):
        print("Unsuccessfull : No such member/ booking found.")
    else:
        teeTime = golfclub.searchMemberBooking(memberId)
        golfclub._bookings[teeTime] = None
        print(f"Tee Time {teeTime} cancelled successfully")


def edit_booking(golfclub):
    print("\n")
    teeTime = input("Enter tee time (HH:MM) to edit booking: ")

    if teeTime not in golfclub._bookings or not golfclub._bookings[teeTime]:
        print("Not a valid tee time/ no booking available at the given tee time.")
        application()
    
    else:
        memberIds = golfclub._bookings[teeTime].getGolfersID()
        print(f"Current flight of golfers {memberIds} will be replaced by a new flight")
        confirm = input("Confirm to replace? (Y/N): ")

        if confirm == 'y' or confirm == 'Y':

            valid_memberIds = False
            while not valid_memberIds:
                newmemberIds = input_golfers()
                valid_memberIds = validate(golfclub, newmemberIds)

            golfclub._bookings[teeTime] = valid_memberIds
            print(f"Tee time {teeTime} updated with flight with golfers {memberIds}")
        
        else:
            print("Unsuccessfull : confirmation not given")
            application()
        



def print_schedule(golfclub):
    print("\n")
    memberId = int(input("Enter member ID to print play schedule: "))

    if not golfclub.searchGolfer(memberId) or not golfclub.searchMemberBooking(memberId):
        print("Unsuccessfull : Entered golfer not in Club or Do not have any current booking")
    
    else:
        teeTime = golfclub.searchMemberBooking(memberId)
        hr, mi = [int(t) for t in teeTime.split(":")]
        golfclub.course.getPlaySchedule(datetime(2000, 1, 1, hr, mi))

        print(f"Successfully printed the schedule for member ID {memberId}")

def print_overview(golfclub):
    print('\n')
    print("Overview of Tee Schedule")
    print("===========================")
    golfclub.getBookings()
        


application()
    





    
