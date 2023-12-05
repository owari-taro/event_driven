from celery import shared_task
import time
from celery.exceptions import SoftTimeLimitExceeded


# max retryを超えたときはsoft_time_limit exceptionがなげられる
@shared_task(
    max_retries=3, soft_time_limit=3, autoretry_for=(Exception,), retry_backoff=True
)
def long_task(seconds: int):
    print("please wait a minutes", seconds, sep="/n")
    # pr\int("asdlfjaslkfjaslfj\n\n")
    time.sleep(seconds)
    print("finished!!!!!!!!!\n")


@shared_task(soft_time_limit=10)
def short_task(seconds: int):
    print("please wait a minutes", seconds, sep="/n")
    # pr\int("asdlfjaslkfjaslfj\n\n")
    time.sleep(0.5)
    print("finished!!!!!!!!!\n")
