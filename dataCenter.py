class Node(object):
    """Class to represent each node"""
    def __init__(self,nodeID,dataLength,A={}):

        self.nodeID = nodeID 
        self.data = bytearray(dataLength) #Dummy data.
        self.A = A #List of associations(id:w).
        self.demand = 0 #Initializing demand to 0.

    def getData():
        """Return the data stored"""
        return self.data

class Shard(object):
    """Represents each shard"""
    def __init__(self,shardID,nodes):
        self.shardID = shardID #Unique id
        self.nodes = nodes #Dictionary containing nodes stored in the shard (id:Node)
        self.cache = {} #Cache dictionary

class DataCenter(object):
    """Represents a dataCenter. Each datacenter contains a shard."""
    def __init__(self,dataCenterID,nodes,port=10000,cost=100):
        self.dataCenterID = dataCenterID
        self.shard = Shard(dataCenterID,nodes)
        self.port = port
        self.cost = cost
        #Add a socket here to write to.

    def isAvailable(self,nodeId):
        """Returns True if node is found in the shard, else False"""
        return nodeId in self.shard.nodes.keys()

    def getNode(self,nodeId):
        """Returns node."""
        try:
            return self.shard.nodes[nodeId]
        except:
            return None

    def getNodeList(self):
        """Return list of node ID's"""
        return self.shard.nodes.keys()

    def addNodes(self,nodesToBeAdded):
        for nodeId in nodesToBeAdded:
            self.shard.nodes[nodeId] = nodesToBeAdded[nodeId]


