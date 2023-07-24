from celery import shared_task
from time import sleep

@shared_task
def process_agreement_changes():
    print("Processing agreement changes...")
    sleep(10)
    print ("Finish processing agreement changes!")
    return None
