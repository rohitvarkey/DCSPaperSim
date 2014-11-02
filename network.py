import random

from dataCenter import DataCenter,Node
from nameServer import NameServer
from user import User

class Network:
    def __init__(self,noOfUsers,rate,noOfDataCenters,wThreshold):
        self.users = {}
        self.dataCenters = {}
        self.nodes = {}
        for i in xrange (0,noOfUsers):
            #Creating users.
            newUser = User(i,rate,self)
            self.users[i] = newUser
        #Create associations. Create nodes.
        for userId in self.users:
            A={}
            noOfAssociations = random.randint(0,noOfUsers)
            #Setting up associations with random no of nodes.
            for i in xrange(0,noOfAssociations):
                #Choosing nodes and assigning weight randomly.
                associatedNode = random.randint(0,noOfUsers)
                weight = random.random()
                A[associatedNode] = weight
            self.nodes[userId] = Node(userId,4,A)
        #Finding strongly connected components and assigning all nodes to a random datacenter
        self.nameServer = NameServer(self) #Creating a nameserver to handle datacenter requests.

network = Network(10,2,3,0.5)
