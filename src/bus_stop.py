class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []
    
    def queue_length(self):
        return len(self.queue)
    
    def add_to_queue(self, person):
        self.queue.append(person)
        
# Try writing a method that the bus would call, to collect all of the passengers from a stop. This might look like bus.pick_up_from_stop(self, bus_stop_1). This should take all of the passengers waiting in line at the stop, and put them inside of the bus. So the stop will now have nobody in the queue, and the number of people on the bus will increase by however many people the stop had at it.

    def pick_up_from_stop(self, bus_stop_1):
        
    
