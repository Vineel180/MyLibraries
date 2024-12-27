from datetime import datetime

def getDateTimeWeekday():
    """
    o:
        str(YYYY + MM + DD + HH + MM + SS + W)
            where W=0 for monday
    """
    now = datetime.now()
    dateTime = now.strftime("%Y%m%d%H%M%S")
    weekday = now.weekday()
    return dateTime + str(weekday)

def getDate(separator="", DDMMYYYY_format=False):
    """
    o:
        str
    """
    if DDMMYYYY_format:
        return datetime.now().strftime(f"%d{separator}%m{separator}%Y")
    else:
        return datetime.now().strftime(f"%Y{separator}%m{separator}%d")

def getTime(separator=""):
    """
    o:
        str
    """
    return datetime.now().strftime(f"%H{separator}%M{separator}%S")

def getWeekday():
    """
    o:
        str
    """
    return str(datetime.now().weekday())
