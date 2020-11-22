import numpy as np

def sumMetaData(tree, index, metaDataSum):
    numChild = int(tree[index])
    numMetaData = int(tree[index+1])
    index += 2
    for _ in range(numChild):
        (index, metaDataSum) = sumMetaData(tree, index, metaDataSum)
    
    endIndex = index + numMetaData
    metaDataSum += np.sum(tree[index:endIndex])
    return (endIndex, metaDataSum) 

def main():
    # tree = np.genfromtxt('testdata.csv', delimiter=' ')
    tree = np.genfromtxt('input.txt', delimiter=' ')

    (index, metaDataSum) = sumMetaData(tree, 0, 0)
    print(index)
    print(metaDataSum)

if __name__ == "__main__": main()
	
