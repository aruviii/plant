from celery import shared_task
import random 
import time

@shared_task
def sending_data():
	time.sleep(10)
	print("sending data")
