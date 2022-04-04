class ClockTime:   
    def __init__(self, hours, minutes, seconds): #initialise three object's attributes hours, minutes seconds
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    #set is =, get is return
    def setHours(self, hours): #only set hours value
        self.hours = hours

    def setMinutes(self, minutes):#only set minute value
        self.minutes = minutes

    def setSeconds(self, seconds): #only set second value
        self.seconds = seconds 
    
    def setTime(self, hours, minutes, seconds): #set hour, minutes and seconds
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
    
    def showTime(self): #display time in the format of hours:minutes:seconds
        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))

#main program; ask for user input on hours, minutes and seconds
hours = int(input("Enter hour: "))
minutes = int(input("Enter minute: "))
seconds = int(input("Enter seconds: "))

object = ClockTime(hours, minutes, seconds)#create object for clockTime class 

object.setTime(hours, minutes, seconds) #set the time by keyboards input for hours, minutes and seconds.

object.showTime()#display time


