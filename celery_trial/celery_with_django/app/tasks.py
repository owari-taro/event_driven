from celery import shared_task
import time

@shared_task
def long_task(seconds:int,short):
    print("please wait a minutes",seconds,sep="/n")
    #pr\int("asdlfjaslkfjaslfj\n\n")
    time.sleep(seconds)
    print("finished!!!!!!!!!\n")


@shared_task(soft_time_limit=10)
def short_task(seconds:int):
    print("please wait a minutes",seconds,sep="/n")
    #pr\int("asdlfjaslkfjaslfj\n\n")
    time.sleep(0.5)
    print("finished!!!!!!!!!\n")