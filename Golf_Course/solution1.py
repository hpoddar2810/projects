from datetime import datetime, timedelta

from regex import R


class Hole:
    """Hole class models a single hole on a golf course """

    def __init__(self, number, par, distance, index):

        """
        Instance variables: 
                _number: an integer number from 1 to 18, indicating the order of play.
                _par: PAR indicates the number of strokes a golfer is expected to complete playing of the hole.
                _distance: representing the length of the hole in meters, from tee box to the pin/cup.
                _index: an integer number from 1 to 18, representing the difficulty ranking of the hole in a golf course, with a lower number signifying a more difficult hole. 
        """
        self._number = number
        self._par = par
        self._distance = distance
        self._index = index
    
    def getDuration(self):
        """ computes the estimated time (in seconds) to complete playing the hole """

        if self._index <= 6:
            setupTime = self._par*180
        elif self._index <= 12:
            setupTime = self._par*150
        elif self._index <= 18:
            setupTime = self._par*120

        if self._distance <= 100:
            playTime = 60
        elif self._distance <= 200:
            playTime = 120
        elif self._distance <= 300:
            playTime = 180
        elif self._distance <= 400:
            playTime = 240
        elif self._distance <= 500:
            playTime = 300
        else:
            playTime = 360
        
        return setupTime + playTime

    def __str__(self):
        """return a string representation of a Hole object, with the information: Hole number, PAR, Index and Distance. """

        return f"{self._number}\t{self._par}\t{self._index}\t{self._distance}"


class Course:
    def __init__(self, fileName):
        """
        Instance variables:         
                _name: this is the filename without the extension. Hence if filename is given as “abc,txt”, the _name will be “abc”.
                _holes: create the 18 holes and place them into a List.
                _totalPar: represents the par for the course as a whole. This is obtained by adding up the par of each hole.
        """

        self.fileName = fileName
        self._name = fileName.split('.')[0]
        self._totalPar = 0
        self._holes = []

        """
        Reading the file and creating Hole class for each hole.
        Appending Hole class into the self._holes
        Calculating Total Par of the Course
        """

        with open("data/" + fileName, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                par, index, distance = [int(data) for data in line.split(",")]

                self._holes.append(Hole(i+1, par, distance, index))
                self._totalPar += par


    """
    Getter method for the instance variable _name
    """
    @property
    def name(self):
        return self.fileName.split('.')[0]


    def getPlaySchedule(self, teeTime):
        """
        returns the estimated start and finish time for all 18 holes, given the teeTime (datetime) as parameter.
        """

        result = \
        f"""
Tee Off Time: {teeTime.strftime("%H:%M")}
Course: {self._name}\t\tTotal PAR: {self._totalPar}
Hole\tPAR\tIndex\tDistance\tStart\tFinish
"""
        # print("\n")
        # print("Tee Off Time: ", teeTime.strftime("%H:%M"))
        # print("Course: ", self._name, "\t\t", "Total PAR: ", self._totalPar)
        # print("Hole\tPAR\tIndex\tDistance\tStart\tFinish")

        start = teeTime
        end = teeTime - timedelta(minutes=1)

        for hole in self._holes:
            start = end + timedelta(minutes=1)
            end = start + timedelta(seconds=hole.getDuration())
            r = f"{hole._number}" + "\t" + f"{hole._par}" + "\t" + f"{hole._index}" + '\t' + f"{hole._distance}" + "m\t" + f" {start.strftime('%H:%M')}" + "\t" + f"{end.strftime('%H:%M')}\n"
            result += r
        
        return result + "\n"

        

    def __str__(self):
        """
        returns a string containg details of Course
        """


        output = """
        '\n',
        'Course: ', self._name, '\t\t', 'Total PAR: ', self._totalPar, '\n', 
        'Hole\tPAR\tIndex\tDistance\n' 
        """
        
        for hole in self._holes:
            s = "hole._number, '\t', hole._par, '\t', hole._index, '\t', hole._distance, 'm\n'"
            output = output + s

        return output
    

def main():
    course1 = Course("Augusta.txt")
    course2 = Course("Laguna.txt")
        
    print(course1.getPlaySchedule(datetime(2001, 1, 1, 7, 8)))
    print(course2.getPlaySchedule(datetime(2001, 1, 1, 9, 18)))

# main()