#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
alice = Secretary("Alice")  # implements Descriptor protocol

(data descriptor = full service)

The idea being, self.secretary knows the self that 
calls it, the self.worker, and so can save the 
message directly in self.worker.__dict__['inbox']

Think of other secretaries for other tasks besides
taking taking messages.
"""
import datetime, pytz

UTC = pytz.timezone('UTC')
PACIFIC = pytz.timezone('US/Pacific')

class Secretary:

    """
    descr.__get__(self, obj, type=None) --> value

    descr.__set__(self, obj, value) --> None

    descr.__delete__(self, obj) --> None
    
    'inbox' is hard-coded as one of the api elements of an obj
    """
    
    def __init__(self, nm):
        self.name = nm
        
    def __set__(self, obj, val):
        print("{}: thank you.  Saving...".format(self.name))
        if not 'inbox' in obj.__dict__:
            obj.inbox = [ ] # initialize empty list
        # (datetime, message) appended to list
        obj.inbox.append((datetime.datetime.now(tz=UTC), val))

    def __get__(self, obj, cls):
        print("OK {}. Retrieving...".format(obj.worker))
        if not 'inbox' in obj.__dict__:
            return 'Empty'
        else:
            messages = [ ]
            for message in obj.inbox:
                # list of tuples
                messages.append((message[0].astimezone(tz=PACIFIC), 
                                message[1]))
        return messages  

class BusyOfficeWorker:

    my_assistant = Secretary("Frank")  # add a layer of politeness

    def __init__(self, worker_bee):
        self.worker = worker_bee

    def leave_message(self, message):
        self.my_assistant = message

    def pickup_message(self):
        return self.my_assistant # that'll be *my* inbox

    def empty_inbox(self):
        # simplest possible
        if "inbox" in self.__dict__: # if there
            del self.__dict__["inbox"]

worker1 = BusyOfficeWorker("Cindy")
worker2 = BusyOfficeWorker("Shelly")

print("worker2:", worker2.pickup_message())

def report(ms):
    for m in ms:
        print("Time: {}\n Message: {}\n".format(*m))
        
worker1.leave_message("Hello, this is to remind you...")
worker2.leave_message("Your dentist appointment for...")
worker2.leave_message("Your car is ready for pickup.")
worker1.leave_message("Hello, this is to remind you...")
worker1.leave_message("Spam call")
print("Retrieving messages...\n\n")
print("worker1:") 
mess = worker1.pickup_message()
report(mess)
print()
print("worker2:")
mess = worker2.pickup_message()
report(mess)
