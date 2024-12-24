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
