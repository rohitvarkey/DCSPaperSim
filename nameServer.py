import random

class NameServer:
    def __init__(self,network):
        self.DataCenterHasShards = {}
        self.network = network
        for dataCenter in network.dataCenters:
            self.DataCenterHasShards[dataCenter] = network.dataCenters[dataCenter].getNodeList()

    def addDataCenter(self,dataCenter):
        self.DataCenterHasShards[dataCenter.id] = dataCenter.getNodeList()

    def getDataCenter(self,nodeId):
        dataCenterList = []
        for dataCenter in self.DataCenterHasShards:
            if dataCenter.isAvailable(nodeId):
                dataCenterList.append(dataCenter.id)
        return random.choice(dataCenterList)
