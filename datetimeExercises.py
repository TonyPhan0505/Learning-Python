import time
from datetime import datetime
import calendar
import datetime
from datetime import date
import math
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from tkinter import Tk
from tkinter import Label


def find_systemS_current_time():
    return time.time()

def find_current_datetime():
    return time.asctime(time.localtime(time.time()))

def display_current_date(year,month,day):
    return datetime(year,month,day)

def is_leap(year):
    return calendar.isleap(year)

def display_monthcalendar(year,month):
    return calendar.monthcalendar(year,month)

def find_weekday(year,month,day):
    return calendar.weekday(year,month,day)

def find_month_range(year,month):
    return calendar.monthrange(year,month)

def display_current_year():
    now = datetime.now()
    return now.year

def display_current_month():
    now = datetime.now()
    return now.month

def display_current_day():
    now = datetime.now()
    return now.day

def current_time_for_reference():
    return datetime.datetime.now()

# Format time strings for the datetime library
# 1. syntax to display days: .strftime('%d)
# 2. syntax to display day/month/year: .strftime('%D')
# 3. syntax to display month: .strftime('%b') = .strftime('%B')
# 4. syntax to display year: .strftime('%y') or .strftime('%Y')
# 5. syntax to display weekday: .strftime('%a') or .strftime('%A')

def parse_timestring_display_structtime():
    return time.strptime('22 January, 2020','%d %B, %Y')

def structtime_to_timestring():
    return time.asctime(((2020,1,22,2,34,6,6,362,0)))

def current_structtime():
    return time.localtime()

def current_structtime_to_formated_timestring():
    return time.strftime('UTC time: %a, %d %b %Y, %H:%M:%S -7',time.localtime())

def secondsSinceEpoch_to_localDatetime():
    return datetime.fromtimestamp(time.time())

def suspend_execution(s):
    for i in ['Ready...','Set...','GO!!']:
        time.sleep(s)
        print(i)

def change_timezone(chosenTZ = 'Asia/Ho_Chi_Minh'):
    #print('TZ:', os.environ['TZ']= chosenTZ)
    print(f'TZ abbreviation: {time.tzname}')
    print(f'Timezone: {time.timezone}')

def local_and_gm_structtime():
    return time.localtime(), time.gmtime()

def secondsSinceEpoch_to_structtime():
    return time.locatime(time.time())

def local_timezone():
    return time.timezone

def first_and_last_second():
    return datetime.time.min, datetime.time.max

def dates_between_dates(date1,date2):
    for n in range(int((date2-date1).days)+1):
        print(date1 + timedelta(days = n))
    
def timestring_to_datetime(str1):
    datetime.strptime('str1','%b %d %Y %I:%M%p')

def print_calendar_prmonth(year,month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.prmonth(year,month)

def secondSaturdayOfEveryMonth(year):
    for month in range(1,13):
        if calendar.monthcalendar(year,month)[0][5]:
            date = calendar.monthcalendar(year,month)[1][5]
            return(f'{year},{month},{date}')
        elif not calendar.monthcalendar(year,month)[0][5]:
            date = calendar.monthcalendar(year,month)[2][5]
            return(f'{year},{month},{date}')
        
def printHTMLcodeOfCalendar(year,month):
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    return cal.formatmonth(year,month)

def week_number(year,month,date):
    dt = date(year,month,date)
    return dt.isocalendar()[1]

def print_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.pryear(year)

def currentDatetimeToTimestring():
    now = datetime.datetime.now()
    return now.strftime('%Y-%b-%d %H:%M:%S')

def currentDatetime():
    return datetime.datetime.now()

def find_age(DOB):
    return date.today().year - date(DOB).year

def datetimeOfModification(filepath):
    return datetime.fromtimestamp(os.stat(filepath).st_mtime)

def time_difference(date1,date2):
    result = date1-date2
    return result.days, int(divmod(result.seconds/60,60)[0]), int(divmod(result.seconds,60)[0]), result.seconds, result.seconds*1000

def date_difference_in_seconds(date1,date2):
    result = date1 - date2
    return result.seconds

def datetimeToUnixtime(dt):
    return time.mktime(dt.timetuple())

def format_timestring(timestring):
    return time.strftime(timestring,'%a, %d-%b-%Y, %I:%M:%S%p')

def date_difference_in_days(date1,date2):
    result = date2 - date1
    return result.days

def currentGMandLocalTime():
    return time.asctime(time.gmtime()), time.ctime()

def thirtyDaysAgoAndFromNow(dt):
    return dt + timedelta(days = 30), dt + timedelta(days = -30)

def twelveDatesFromDateWithDifference(dt, d):
    for i in range(0,12*d+1, d):
        print(dt + timedelta(days = i))

def sixMonthsFromDate(dt):
    return dt + relativedelta(months=6)

def numberOfMondayFirstMonthDay(year1,year2):
    ctr = 0
    for year in range(year1,year2+1):
        for month in range(1,13):
            if calendar.monthcalendar(year,month)[0].index(1) == 0: ctr += 1
            else: pass
    return ctr

def numberOfDaysInMonth(year,month):
    return calendar.monthrange(year,month)[1]

def lstOfWeeksInMonth(year,month):
    return calendar.monthcalendar(year,month)

def isThirdTuesdayOfMonth(dt):
    cal = calendar.monthcalendar(dt.year,dt.month)
    if (cal[2][1] == dt.day) or (cal[3][1] == dt.day): return True
    else: return False

def lastTuesdayOfMonth(year,month):
    return date(year,month,calendar.monthcalendar(year,month)[-1][1])

def keepMicrosecondsNull():
    now = datetime.datetime.now()
    return now.replace(microseconds = 0)

def nYearsFromNow(dt,n):
    return dt + relativedelta(years = n)

def sundaysOfYear(year):
    for month in range(1,13):
        for week in calendar.monthcalendar(year,month):
            print(year,'/',month,'/',week[6])


def yearWeekWeekday(dt):
    return dt.isocalendar([1])

def microsecondSinceEpoch():
    return time.time()*1000

def dayOfYear(dt):
    return (dt - datetime(dt.year,1,1)).days + 1

def fiveSecondsFromCurrentTime():
    return (datetime.now()+timedelta(seconds = 5)).time()

def printNextFiveDays():
    for i in range(0,6):
        print(date.today() + timedelta(days = i))

def newDay():
    return datetime.combine(date.today(), datetime.min.time())

def yesterdayAndTomorrow():
    return date.today()+timedelta(days = -1), date.today(), date.today()+timedelta(days = 1)

def secondsSinceEpochToDatetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def currenttime():
    return datetime.datetime.now().time()

def isLeapYear(year):
    return calendar.isleap(year)

def time_difference_in_seconds(future_time):
    now = datetime.now()
    difference = datetime(future_time) - now
    return difference.seconds

#digital clock
def andyouknowit():
    digi_clock.config(text = 'Tớ đi lấy nước uống một tẹo')
def iloveyou():
    digi_clock.config(text = 'I love you')
    digi_clock.after(5000, andyouknowit)

def digital_clock():
    display_time = time.strftime('%I:%M:%S %p')
    digi_clock.config(text = display_time + ' now')
    digi_clock.after(5000, digital_clock)

# root = Tk()
# root.title('clock')
# digi_clock = Label(root,font=('Arial',150), bg = 'black', fg = 'RosyBrown2')
# digi_clock.pack()
# digital_clock()
# root.mainloop()
   
def countdown(t):
    t = int(t)
    while t:
        mins, secs = divmod(t,60)
        timer_str = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_str, end = "\r")
        time.sleep(1)
        t -= 1
