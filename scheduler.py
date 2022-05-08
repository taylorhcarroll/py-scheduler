import schedule
import time
from emailer import sendEmail


SENDER_EMAIL = "youremail@xyz.com"
PASSWORD = "password"
TO = "yourfrnds@email.com"
SUBJECT = "Time to take lunch"
MESSAGE = "Daily reminder to take lunch if you haven't already and come back in 30 min."


def job():
    print("I'm working...")

def job2():
    print("yo boiss..", __name__)

def job3():
    print("Hello")

# unfortunately, these emails end up in your spam folder :(
def job4():
    print("Email is in transit")
    sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)

schedule.every(5).seconds.do(job4)
# some other variations 
schedule.every().hour.do(job)
# by default, the schedule module uses the 24hr format
schedule.every().day.at("12:25").do(job4)
schedule.every(5).to(10).minutes.do(job)
schedule.every().thursday.at("19:15").do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
schedule.every(2).seconds.do(job2)





while True:
    schedule.run_pending()
    time.sleep(1)



