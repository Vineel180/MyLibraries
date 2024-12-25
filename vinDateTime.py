from datetime import datetime

def getDateTimeWeekday():
    """1
    o:
        str(YYYY + MM + DD + HH + MM + SS + W)
            where W=0 for monday
    """
    now = datetime.now()
    dateTime = now.strftime("%Y%m%d%H%M%S")
    weekday = now.weekday()
    return dateTime + str(weekday)

def getDate(separator="", reverse=False):
    """1
    o:
        str
    """
    if reverse:
        return datetime.now().strftime(f"%d{separator}%m{separator}%Y")
    else:
        return datetime.now().strftime(f"%Y{separator}%m{separator}%d")
def getTime(separator=""):
    """1
    o:
        str
    """
    return datetime.now().strftime(f"%H{separator}%M{separator}%S")
def getWeekday():
    """1
    o:
        str
    """
    return str(datetime.now().weekday())
