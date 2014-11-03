import random
from dataCenter import DataCenter,Shard
#from user import User

class Query:
    def __init__(self,userNodeId,network):
        self.network = network
        self.userNodeId = userNodeId

    def run(self):
        nameServer = self.network.nameServer
        dataCenter = nameServer.getDataCenter(self.userNodeId)
        cost = 0
        dataCenterInst = self.network.dataCenters[dataCenter]
        res = {}
        queryNodesList = dataCenterInst.shard.nodes[self.userNodeId].A.keys()
        cost+=dataCenterInst.cost
        for nodeId in queryNodesList:
            if dataCenterInst.isAvailable(nodeId):
                cost+=dataCenterInst.cost
                reqNode = dataCenterInst.shard.nodes[nodeId]
                res[nodeId] = reqNode
            else:
                nodeDataCenter = nameServer.getDataCenter(nodeId)
                nodeDataCenterInst = self.network.dataCenters[nodeDataCenter]
                cost+=random.randint(10,100)*nodeDataCenterInst.cost #Assumption
                reqNode = nodeDataCenterInst.shard.nodes[nodeId]
                res[nodeId] = reqNode
                nodeDataCenterInst.addToCache({nodeId:reqNode})
        print "Query by", self.userNodeId, "Cost = ", cost
        return (cost,res)
