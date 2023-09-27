import datetime
import schedule
import time

def schedule_minute():
    print("Schedular schedules after a minute")
    print("Current time is",datetime.datetime.now())


def schedule_hour():
    print("Schedular schedules after a hour")
    print("Current time is",datetime.datetime.now())

def schedule_sunday():
    print("Schedular schedules after sunday")
    print("Current time is",datetime.datetime.now())


def main():

    print("Automation")

    schedule.every(1).minutes.do(schedule_minute)
    schedule.every().hour.do(schedule_hour)
    schedule.every().hour.do(schedule_sunday)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()