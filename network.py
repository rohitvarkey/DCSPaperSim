import random
import tarjan
import time

from dataCenter import DataCenter,Node
from nameServer import NameServer
from user import User
from parse import parseFile

maxSCCGivenw = {}

class Network:
    def __init__(self,fileName,rate,noOfDataCenters,wThreshold,shardCapacity):
        """Setting up a network"""
        self.users = {}
        self.dataCenters = {}
        self.nodes = {}
        self.wThreshold = wThreshold
        self.rate = rate
        self.shardCapacity = shardCapacity
        nodes, graph =  parseFile(fileName)
        for i in nodes:
            self.users[i] = User(i,rate,self)
            if i not in graph.keys():
                graph[i] = {}
            self.nodes[i] = Node(i,4,graph[i])
        for i in xrange (0,noOfDataCenters):
            self.dataCenters[i] = DataCenter(i,{},10000,10,shardCapacity)
        #Finding strongly connected components and assigning all nodes that are part of it to a random datacenter
        self.findSCCAndAssign()
        self.nameServer = NameServer(self) #Creating a nameserver to handle shard and node based datacenter requests.
        print "Network set up."
        for dataCenter in self.dataCenters:
            print dataCenter,':',self.dataCenters[dataCenter].getNodeList()
        for dataCenter in self.dataCenters:
            print dataCenter,':',len(self.dataCenters[dataCenter].getNodeList())
    
    def findSCCAndAssign(self):
        graph = {}
        for nodeId in self.nodes:
            b = len(filter(lambda x:self.nodes[nodeId].A[x]>=self.wThreshold,self.nodes[nodeId].A.keys()))
            graph[nodeId] = filter(lambda x:self.nodes[nodeId].A[x]>=self.wThreshold,self.nodes[nodeId].A.keys())
        SCCList = tarjan.tarjan(graph)
        maxSCClen = max(map(lambda x: len(x), SCCList))
        maxSCCGivenw[self.wThreshold] = maxSCClen
        for SCC in SCCList:
            dataCenterId = random.choice(self.dataCenters.keys())
            if len(SCC) is not 1:
                print "SSC length of ", len(SCC),"Assigned to ", dataCenterId
            dataCenter = self.dataCenters[dataCenterId]
            nodesToAdd = {}
            if len(SCC)<=self.shardCapacity:
                for nodeID in SCC:
                    nodesToAdd[nodeID] = self.nodes[nodeID]
                dataCenter.addNodes(nodesToAdd)
            else:
                for nodeID in SCC:
                    dataCenterId = random.choice(self.dataCenters.keys())
                    dataCenter = self.dataCenters[dataCenterId]
                    dataCenter.addNodes({nodeID:self.nodes[nodeID]})

    def start(self,logFile):
        call_spacing = 1.0/self.rate #Time between queries.
        simStartTime = time.time()
        costSum = 0
        """
        while (time.time() - simStartTime)/60.0 <2: #2 minutes
            start_time = time.time()
            queryUserId = random.choice(self.users.keys())
            queryUser = self.users[queryUserId]
            cost = queryUser.query()
            costSum+=cost
            costNum+=1
            while time.time() - start_time<call_spacing:
                pass
        """
        for i in range(0,1200):
            queryUserId = random.choice(self.users.keys())
            queryUser = self.users[queryUserId]
            cost = queryUser.query()
            costSum+=cost
        
        costAvg = costSum/1200.0
        logFile.write(str(self.wThreshold)+' '+str(costAvg)+'\n')
        print self.wThreshold,"done"

    def logReplicationFactor(self,logFile):
        noOfNodes = 0
        noOfDataCenters = len(self.dataCenters)
        for dataCenterId in self.dataCenters:
            dataCenter = self.dataCenters[dataCenterId]
            noOfNodes+=dataCenter.getSize()
        repRatio = noOfNodes/float(noOfDataCenters)
        logFile.write(str(self.wThreshold)+' '+str(repRatio)+'\n')

log = open('log','w')
rep = open('replicationRatio','w')
#Network initialized.
for i in range(0,1000):
    network = Network('graph.dot',10,15,i/1000.0,300)
    network.start(log)
    network.logReplicationFactor(rep)
