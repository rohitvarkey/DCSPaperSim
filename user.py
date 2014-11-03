import time
from query import Query

class User:
    def __init__(self,userID,rate,network):
        self.userID = userID
        self.nodeId = userID
        self.rate = rate
        self.network = network
   
    def query(self):
        query = Query(self.nodeId,self.network)
        cost, associatedData = query.run() #Get all data
        return cost
