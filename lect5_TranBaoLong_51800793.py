import os 

Path = os.path.dirname(os.path.realpath(__file__))
inputData = open(Path + "\\inputs\\text1.txt")  
data = {}
for each in inputData:
    info = each.split()
    data.setdefault(info[0],info[1:])

'''
    ['C', 'F', 'R', 'S', 'Result']
    ['1', '1', '1', '0', 'positive']
    ['1', '1', '0', '0', 'positive']
    ['0', '0', '1', '1', 'positive']
    ['1', '0', '0', '0', 'negative']
    ['0', '0', '0', '0', 'negative']
    ['0', '1', '1', '0', 'negative']

'''

def doBayes(obj, data):
    prep = [data[each] for each in data if data[each][-1] == obj[-1]]
    # if not len(prep):
    probability = 1
    for i in range(len(obj)-1):
        n_prob = len([True for j in range(len(prep)) if prep[j][i] == obj[i]]) / len(prep) 
        probability *= n_prob
    probability *= len(prep) / (len(data) - 1)
    return probability
    # return 0

listItem = [
    ['0','1','0','0','0'],
    ['0','1','0','1','1'],
    ['0','1','0','1','0'],
    ['1','0','1','0','1'],
    ['1','0','1','0','0']
]
