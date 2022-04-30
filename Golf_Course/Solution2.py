from datetime import datetime


class Golfer():
    """
    class variable: 
        _NEXT_ID : starting from 1
    """
    _NEXT_ID = 1
    # print(_NEXT_ID)

    def __init__(self, name, membership):
        """
        Input :
            name (str) : Name of golfer
            membership (str) : membership type ("Full" or "Basic") 

        Instance variables:
                _memberID (int): a unique member number for this golfer. Generated using _NEXT_ID class variable
                _name (str): the name of this golfer.
                _membership (str): either “Full” or “Basic” membership. Full membership can enjoy golfing at any time of the week, while Basic members are allowed to golf on weekdays only.
                _status (bool): this is the membership status, either True or False to represent active and inactive respectively. By default True.
        """

        self._name = name
        self._membership = membership
        self._memberID = Golfer._NEXT_ID
        self._status = True

        Golfer._NEXT_ID += 1
    

    """
    Getter method for the instance variable _memberID
    """
    @property
    def memberID(self):
        return self._memberID

    
    """
    Getter method for the instance variable _name
    """
    @property
    def name(self):
        return self._name


    """
    Getter method for the instance variable _membership
    """
    @property
    def membership(self):
        return self._membership



    """
    Setter method for _ membership.
    """
    @membership.setter
    def membership(self, membership):
        self._membership = membership

    
    def getMemebershipStatus(self):
        """
         returns the value of _status (Boolean).
        """
        return self._status
    

    def setMemebershipStatus(self, status):
        """
        Input : 
            status (bool) : boolean value of membership status
            
        Assign status to instance variable _status
        """
        self._status = status
    

    def getHandicap(self):
        """
        abstract method, which returns the handicap number for this golfer
        """
        pass

    def __str__(self):
        """
        returns a string representation of a Golfer object, which should include the memberID, name, membership, and status.
        """

        status = 'A' if self._status else 'I'
        output = "Member ID: " + str(self._memberID) + "\t" + "Name: " + self._name + "\t" + "Membership: " + self._membership + f"({status})"

        return output



class HandicappedGolfer(Golfer):
    """
    - Subclass of Golfer
    - These are skilled golfers with a handicap number that represents the golfer's ability. Golf handicap is generally between 0 and 36. The lower the handicap number, the better the player
    """

    def __init__(self, name, membership, handicap):
        """
        Input :
            name (str) : name of golfer
            membership : membership type of golfer ("Full" or "Basic")
            handicap : handicap number of golfer

        Additional Instance variable: 
                _handicap (float) : that represents the golfer's ability. Golf handicap is generally between 0 and 36.
        """

        super().__init__(name, membership)
        self._handicap = handicap


    def getHandicap(self):
        """
        returns the handicap number for this golfer
        """

        return self._handicap

    
    def __str__(self):
        """
        returns a string representation of a HandicappedGolfer object
        """

        output = super(HandicappedGolfer, self).__str__()
        output += "\tHandicap: " + str(self._handicap)
        return output



class PCHolder(Golfer):
    """
    - A subclass of Golfer
    - Proficiency Certificate (PC) is normally issued by a golf club to allow a new golfer to play in order to gain sufficient experience, prior to their Handicap Test. 
      Hence, there is an expiry date for the Proficiency Certificate. For PC Holders, their golf handicap is 99.

    """

    def __init__(self, name, membership, expiryDate):
        """
        Additional Instance variable: 
                _expiryDate (datetime) : that represents the validity date for the Proficiency Certificate. 
        """
        super().__init__(name, membership)
        self._expiryDate =  expiryDate

    
    def getMembershipStatus(self):
        """
        returns False if the expiry date of the Proficiency Certificate has lapsed (compare to current datetime). Otherwise, it returns the membership status of this golfer
        """
        if datetime.now() > self._expiryDate:
            return False
        
        return self._status
    

    def renew(self, newdate):
        """
        Input 
            newdate (datetime) : new expiration date
        
        Set a new expiry date for the Proficiency Certificate
        """
        self._expiryDate = newdate
    
    def getHandicap(self):
        """
        return 99.9
        """
        return 99.9

    def __str__(self):
        """
        returns a string representation of a PCHolder object
        """

        output = super(PCHolder, self).__str__()
        output += "\tExpiry: " + self._expiryDate.strftime("%d-%B-%Y")
        return output


class GolfingException(Exception):
    """
    A subclass, GolfingException of the Exception class
    """
    pass


class Flight():
    def __init__(self, golfers):
        """
        Input :
                golfers (list) : list of golfers object

        Instance variable: 
                _golfers (list) : represent the flight of golfers.

        Functions :
                validate the number of golfers to be minimum 3 and maximum 4. Otherwise, raise GolfingException
        """

        if len(golfers) < 3 or len(golfers) > 4:
            raise GolfingException("A flight can only consists of 3 or 4 golfers.")
        
        self._golfers = golfers

    def searchGolfer(self, memberID):
        """
        Input :
            memberID (int) : memberID of a golfer to search
        
        returns the Golfer object if there is a golfer in the flight with the matching memberID. 
        If not found, it returns None.

        """

        for golfer in self._golfers:
            if golfer._memberID == memberID:
                return golfer
        return None
    
    def getGolfersID(self):
        """
        returns the flight’s golfers’ memberID in a List.
        """

        return [golfer._memberID for golfer in self._golfers]
    
    def  getWeekendEligibility(self):
        """
         return a Boolean value indicating if this flight of golfers can book a golf session on weekend. 
        """

        for golfer in self._golfers:
            if golfer._membership == 'Basic' or golfer._status == False:
                return False
        
        return True


def main():
    golfers = [['Jeff', 'Full', 13.1],
                ['Jim', 'Basic', 4],
                ["Joe", "Full", 19],
                ["Jack", 'Full', 2.3]]

    golfers = [HandicappedGolfer(*detail) for detail in golfers]
    f1 = Flight(golfers)

    print(f1.getWeekendEligibility())

    golfers[1]._membership = 'Full'

    print(f1.getWeekendEligibility())
    print(golfers[1].membership)

    golfers2 = [['Tom', 'Full', 11],
                ['Neil', 'Full', 2.5],
                ['Charles', 'Full', datetime(2021, 7, 30)]]
    
    golfers2 = [ HandicappedGolfer(*golfers2[0]) , 
                 HandicappedGolfer(*golfers2[1]), 
                 PCHolder(*golfers2[2])
                 ]

    f2 = Flight(golfers2)


# main()
    

        
    
    

    
