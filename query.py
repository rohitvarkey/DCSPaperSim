from dataCenter import DataCenter,Shard
from network import User

class Query:
    def __init__(self,userNodeId,network):
        self.network = network
        self.userNodeId = userNodeId

    def run(self):
        nameServer = self.network.nameServer
        dataCenter = nameServer.getDataCenter(self.userNodeId)
        cost = 0
        res = {}
        queryNodesList = dataCenter.shard.nodes[userNodeId]
        cost+=dataCenter.cost
        for nodeId in queryNodesList:
            if dataCenter.isAvailable(nodeId):
                cost+=dataCenter.cost
                reqNode = dataCenter.shard.nodes[nodeId]
                res[nodeId] = reqNode
            else:
                nodeDataCenter = nameServer.getDataCenter(self.nodeId)
                cost+=5*nodeDataCenter.cost #Assumption
                reqNode = nodeDataCenter.shard.nodes[nodeId]
                res[nodeId] = reqNode
        return res
