import datetime
import pytz

def getTime(zone):
    #  Get local datetime
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    #  now get datetime for local timezone
    cur_now = utc_now.astimezone(pytz.timezone(zone))
    # Ensure that local datetime is the same at any other location
    if (cur_now == utc_now):
        #   extract time portion of the datetime
        cur_time = cur_now.strftime("%H:%M:%S")
    else:
        cur_time = None
    return cur_time

def checkHrs(cur_time):
    strTime = "09:00:00"
    endTime = "17:00:00"

    if (cur_time > strTime and  cur_time < endTime):
        isOpen = True
    else:
        isOpen = False
    #  identified whether that location is open or not
    return isOpen     
   

    #  print out informational message
def printInfo(location, isOpen):
    #    isOpen tells us whether the hq is open in their timezone
    if isOpen:
        print("HQ " + location + " is open now.")
    else:
        print("HQ " + location + " is NOT open now.")    

if __name__== "__main__":

    #  Get Portland, OR datetime
    location = "Portland, OR"
    zone = "America/Los_Angeles"
    cur_time = getTime(zone)
    isOpen = checkHrs(cur_time)
    printInfo(location, isOpen)

    # Get New York, NY datetime
    location = "New York, NY"
    zone = "America/New_York"
    cur_time = getTime(zone)
    isOpen = checkHrs(cur_time)
    printInfo(location, isOpen)
        
    # Get London, UK datetime
    location = "London, UK"
    zone = "Europe/London"
    cur_time = getTime(zone)
    isOpen = checkHrs(cur_time)
    printInfo(location, isOpen)
    
