import asyncio 
import time
#subroutine block of code that can be called as needed, run until done

#coroutine special f((x) that can be called and paused 
#concurrency start and stop times if coruotnes can overlap 
#parallelism different threads execute at same time

class Jupiter:
    def __init__(self, request, waiting_time, position):
        self.request = request
        self.waiting_time=waiting_time
        self.position=position

    def send_message(self):
        print("please input message below") 
        user_message = input(":")
        time.sleep(3)
        print("message ready"+ user_mesaage)
        return("message sent")
    