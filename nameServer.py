import random

class NameServer:
    def __init__(self,network):
        self.DataCenterHasShards = {}
        self.network = network
        for dataCenter in network.dataCenters:
            self.DataCenterHasShards[dataCenter] = network.dataCenters[dataCenter].getNodeList()

    def addDataCenter(self,dataCenter):
        self.DataCenterHasShards[dataCenter] = dataCenter.getNodeList()

    def getDataCenter(self,nodeId):
        dataCenterList = []
        for dataCenter in self.DataCenterHasShards:
            if self.network.dataCenters[dataCenter].isAvailable(nodeId):
                dataCenterList.append(dataCenter)
        return random.choice(dataCenterList)
