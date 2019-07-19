import logging
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def thread_function(number):
    logging.info("Thread %s: starting", number)
    time.sleep(number)
    # Thread finished after the Main section of your code did.
    logging.info("Thread %s: ending", number)
def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    # the arguments pass to the threafing target function shoulde be tuple.
    x = threading.Thread(target=thread_function, args=(1, ))
    y = threading.Thread(target=thread_function, args=(2, ))
    logging.info("Main : before running thread")
    # start the threads
    x.start()
    y.start()
    logging.info("Main : wait for the thread to finish")
    # wait for the threads to finish.
    x.join()
    y.join()
    logging.info("Main : all done")

import random
SENTINEL = object()


def producer(pipline):
    for index in range(10):
        # Pretenf we're get 10 message from the network.
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipline.set_message(message, "Producer")
    # uses a sentinel value to signal the consumer to stop after it has
    # sent ten values
    pipline.set_message(SENTINEL, "Producer")


def consumer(pipline):
    message = 0
    while message is not SENTINEL:
        message = pipline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    
    def get_message(self, name):
        logging.info("%s: about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.info("%s: have getlock", name)
        message = self.message
        logging.info("%s: about to release setlock", name)
        self.producer_lock.release()
        logging.info("%s: setlock released", name)
        return message
    
    def set_message(self, message, name):
        logging.info("%s: about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.info("%s: have setlock", name)
        self.message = message
        logging.info("%s: about to release getlock", name)
        self.consumer_lock.release()
        logging.info("%s: getlock released", name)

if __name__ == "__main__":
    pipline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline)
        executor.submit(consumer, pipline)