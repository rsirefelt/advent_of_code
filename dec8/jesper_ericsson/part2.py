import numpy as np

def sumMetaData(tree, index, metaDataSum):
    numChild = int(tree[index])
    numMetaData = int(tree[index+1])
    index += 2
    childSums = np.zeros(numChild)
    
    if numChild > 0:
        for iChild in range(numChild):
            (index, childSums[iChild]) = sumMetaData(tree, index, metaDataSum)
        
        endIndex = index + numMetaData
        for refIndex in tree[index:endIndex]:
            if refIndex <= numChild and refIndex > 0:
                metaDataSum += childSums[int(refIndex)-1]
    else:
        endIndex = index + numMetaData
        metaDataSum += np.sum(tree[index:endIndex])
    
    return (endIndex, metaDataSum) 

def main():
    # tree = np.genfromtxt('testdata.csv', delimiter=' ')
    tree = np.genfromtxt('input.txt', delimiter=' ')

    (index, metaDataSum) = sumMetaData(tree, 0, 0)
    print(metaDataSum)

if __name__ == "__main__": main()
	
