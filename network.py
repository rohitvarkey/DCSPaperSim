import random
import tarjan

from dataCenter import DataCenter,Node
from nameServer import NameServer
from user import User

class Network:
    def __init__(self,noOfUsers,rate,noOfDataCenters,wThreshold):
        """Setting up a network"""
        self.users = {}
        self.dataCenters = {}
        self.nodes = {}
        self.wThreshold = wThreshold
        for i in xrange (0,noOfUsers):
            #Creating users.
            newUser = User(i,rate,self)
            self.users[i] = newUser
        #Create associations. Create nodes.
        for userId in self.users:
            A={}
            noOfAssociations = random.randint(0,noOfUsers/16)
            #Setting up associations with random no of nodes.
            for i in xrange(0,noOfAssociations):
                #Choosing nodes and assigning weight randomly.
                associatedNode = random.choice(self.users.keys())
                weight = random.random()
                A[associatedNode] = weight
            self.nodes[userId] = Node(userId,4,A)
        for i in xrange (0,noOfDataCenters):
            self.dataCenters[i] = DataCenter(i,{})
        for dataCenter in self.dataCenters:
            print dataCenter,':',self.dataCenters[dataCenter].getNodeList() 
        #Finding strongly connected components and assigning all nodes that are part of it to a random datacenter
        self.findSCCAndAssign()
        self.nameServer = NameServer(self) #Creating a nameserver to handle shard and node based datacenter requests.
        print "Network set up."
        for dataCenter in self.dataCenters:
            print dataCenter,':',self.dataCenters[dataCenter].getNodeList()

    def findSCCAndAssign(self):
        graph = {}
        for nodeId in self.nodes:
            print len(self.nodes[nodeId].A.keys())
            print len(filter(lambda x:self.nodes[nodeId].A[x]>=self.wThreshold,self.nodes[nodeId].A.keys()))
            graph[nodeId] = filter(lambda x:self.nodes[nodeId].A[x]>=self.wThreshold,self.nodes[nodeId].A.keys())
        SCCList = tarjan.tarjan(graph)
        for SCC in SCCList:
            dataCenterId = random.choice(self.dataCenters.keys())
            print "SSC length of ", len(SCC),"Assigned to ", dataCenterId
            dataCenter = self.dataCenters[dataCenterId]
            nodesToAdd = {}
            for nodeID in SCC:
                nodesToAdd[nodeID] = self.nodes[nodeID]
            dataCenter.addNodes(nodesToAdd)

network = Network(2000,10,15,0.5)
