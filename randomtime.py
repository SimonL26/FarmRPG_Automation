import time
import random

def random_time(start_time:float, end_time:float):
    """Get program to sleep for a random time between start_time and end_time"""
    time.sleep(random.uniform(start_time, end_time))