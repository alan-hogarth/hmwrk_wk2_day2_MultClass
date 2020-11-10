class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue_length = []
    
    def add_to_queue(self, person):
        self.queue_length.append(person)

