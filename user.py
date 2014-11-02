import time

class User:
    def __init__(self,userID,rate,network):
        self.userID = userID
        self.nodeId = userID
        self.rate = rate
        self.network = network
   
    def query(self):
        query = Query(self.nodeId,self.network)
        associatedData = query.run() #Get all data

    def run(self):
        call_spacing = 1.0/rate #Time between queries.
        while True:
            start_time = time.time()
            tic = start_time
            while tic - start_time < call_spacing:
                tic = time.time()
            self.query()
