# Define tree structure 
class Tree: 
    def __init__(self, dataList, startIndex):
        # First, read number of children and meta 
        # data from input 
        self.numChildren = dataList[startIndex]
        self.numMetaDataEntries = dataList[startIndex+1]

        # Total length (number of  entries) this node occupied in the 
        # input data 
        self.totalLength = 2 

        # Now read all of the children nodes 
        self.children = [] 
        for k in range(self.numChildren):
            self.children.append(Tree(dataList, startIndex+self.totalLength))
            self.totalLength += self.children[k].totalLength
        
        self.metaData = dataList[(startIndex+self.totalLength):(startIndex+self.totalLength+self.numMetaDataEntries)]
        self.totalLength += self.numMetaDataEntries
    
    def sumMetaDataEntries(self): 
        totalSum = sum(self.metaData)
        for child in self.children: 
            totalSum += child.sumMetaDataEntries() 
            
        return totalSum 

    def getValue(self): 
        if self.numChildren == 0:
            # print('Inga barn: ' + str(sum(self.metaData)))
            return sum(self.metaData)
        else: 
            totalValue = 0
            for val in self.metaData: 
                if val-1 < self.numChildren: 
                    totalValue += self.children[val-1].getValue()  
            return totalValue

# Read input data 
with open('input.txt') as f:
    line = f.readlines()[0] 
    line = line.strip()
    inputData = line.split(' ')

for k in range(len(inputData)):
    inputData[k] = int(inputData[k])

parentNode = Tree(inputData, 0) 
print(parentNode.sumMetaDataEntries())
print(parentNode.getValue())