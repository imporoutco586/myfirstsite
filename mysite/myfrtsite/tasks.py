import datetime
from time import sleep
from celery import shared_task
import logging
logger = logging.getLogger(__name__)
import os
import subprocess


@shared_task()
def task1(x):
    for i in range(int(x)):
        sleep(1)
        logger.info('this is task1 '+str(i))
    return x


@shared_task
def scheduletask1():
    now = datetime.datetime.now()
    logger.info('this is scheduletask '+now.strftime("%Y-%m-%d %H:%M:%S"))
    return None

@shared_task
def sum(x, y):
    logger.info('this is sum')
    return x + y

@shared_task
def runworkflow():
    now = datetime.datetime.now()
    result = subprocess.run(['python3','/home/zfym/Desktop/myfirstsite/ts/test/run_wokerflow2.py']
                            ,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(result.stdout)
    logger.info('this is runworkflow result'+now.strftime("%Y-%m-%d %H:%M:%S"))
    return result.stdout



@shared_task
def runfile(file):
    now = datetime.datetime.now()
    string = os.path.join('/home/zfym/Desktop/myfirstsite/ts/test/',file)
    print(string)
    result = subprocess.run(['python3',string]
                            ,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(result.stdout)
    logger.info('this is runworkflow result'+now.strftime("%Y-%m-%d %H:%M:%S"))
    return result.stdout