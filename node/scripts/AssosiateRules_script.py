'''
    Use Aprori to get Support List and Max Support List
    Use Associative Rules to get rules
'''

import sys
from itertools import combinations as C

def notDup(arr, check):
    return not (arr in check)
    
def combine(arr):
    output = []
    for each in arr:
        for ele in arr[arr.index(each) + 1:]:
            if type(each) is list and type(ele) is list: 
                # sort() 
                ele.sort()
                each.sort()
                # get list then append new elements
                tmp = each.copy()
                for j in ele:
                    if j not in each: 
                        tmp.append(j)
                tmp.sort()
                if notDup(tmp, output):
                    output.append(tmp)
            else:
                output.append([each,ele])
    return output
    
def countElements(arr, T):
    output = 0
    for i in range(len(T)):
        count = 0
        for j in arr:
            if T[i][j - 1]: count += T[i][j - 1]
            if count == len(arr): 
                output += 1 
                break
    return output

def checkSP(arr,T,minsp):
    sup = countElements(arr,T)/len(T)
    return (sup > minsp,sup)
    
def arrangeAscending(arr):
    
    # get min max length of each element of list
    minNEle = min([len(each) for each in arr])
    maxNEle = max([len(each) for each in arr])

    # arrange a max list having each length's element ascending
    arr = [eles for each in [[each for each in arr if len(each) == i] for i in range(minNEle, maxNEle + 1)] for eles in each]
    return arr

def validate(supportMaxList, arr = []):
    # combine into a sorted support max list
    supportMaxList += arr
    supportMaxList.sort()

    # arrange a max list having each length's element ascending
    supportMaxList = arrangeAscending(supportMaxList)

    # temporary result to eleminate not max elements
    maxList = supportMaxList.copy()
    for each in maxList:
        for eles in maxList[maxList.index(each)+1:]:
            flag=0
            for i in each:
                if i in eles:
                    flag += 1
            if flag == len(each): 
                supportMaxList.remove(each)
                break
    # print((supportMaxList))

    return supportMaxList

def doApriori(arr, T, minsp, endpoint, supportList = [], supportMaxList = []):
    
    # get combinations
    arr = combine(arr)
    print('get combination: \n',arr, '\n')

    # check support fit condition of minsp
    sup = [False]*len(arr)
    setSP = [0]*len(arr)
    for i in range(len(arr)):
        #list valid items
        sup[i] = checkSP(arr[i],T,minsp)[0]
        # list value of if sup
        setSP[i] = checkSP(arr[i],T,minsp)[1]
    
    # eliminating
    arr = [arr[i] for i in range(len(arr)) if sup[i]]

    # find out support list and max list
    supportList += [each for each in arr if each not in supportList]
    supportMaxList = validate(supportList)

    # print
    toString(arr, supportList, supportMaxList)

    if len(arr) > 0: return doApriori(arr, T, minsp, endpoint, supportList,supportMaxList)
    supportList = arrangeAscending(supportList)
    return (supportList, supportMaxList)

def toString (arr, supportList, supportMaxList):
    print('after eliminating: \n', arr, '\n')
    print('support list: \n', supportList, '\n')
    print('support max list: \n', supportMaxList, '\n')
    return;

def Apriori(T, minsp):
    n = len(T[0])
    init = list(range(1, n + 1)) #
    endpoint = max([len([ele for ele in each if ele == 1]) for each in A])
    
    totalList = doApriori(init,T,minsp, endpoint,[],[])
    SupportList = totalList[0]
    SupportMaxList = totalList[1]
    
    return (SupportList, SupportMaxList)

def getSupportList(T, minsp):
    getSupportList = Apriori(T, minsp)
    return getSupportList[0]

def getSupportMaxList(T, minsp):
    getSupportMaxList = Apriori(T, minsp)
    return getSupportMaxList[1]

def getAssociativeRule(arr, inputArr):
    AssociativeRules = []
    for i in (range(1,len(arr))):
        c = [list(ele) for ele in list(C(arr,i))]
        for ele in c:
            rest = [i for i in arr if i not in ele]
            # print(ele)
            countEle = countElements(ele,inputArr)
            countArray = countElements(arr,inputArr)
            conf = countArray/countEle
            # print(ele,'->', rest, 'Proportion:\t', countArray, '/', countEle, '=',conf)
            if conf >= 1:
                AssociativeRules.append([ele, rest])
    return AssociativeRules
    
def AssociativeRules(supportMaxList, inputArr):
    AssociativeRules = []
    for each in supportMaxList:
        AssociativeRules += getAssociativeRule(each, inputArr)
    return AssociativeRules 

def do(Arr, minsp = 0.3, minconf = 1):
    print('Apriori of ', Arr, 'with ', minsp, ':\n',Apriori(Arr,minsp))
    print('Support List: \n',getSupportList(Arr,minsp))

    SpMax = getSupportMaxList(Arr,minsp)
    print('Support Max List: \n', SpMax)
    print('AssociativeRules: \n', AssociativeRules(SpMax, Arr))

    return;

def sepLine():
    print('\n' + '#'*156 + '\n')
'''
    1   get combinations
    2   check minsp
    3   eleminating
'''

A = [
    [1,0,1,1,0],
    [1,0,1,1,0],
    [0,0,1,0,1],
    [1,1,0,1,1],
    [1,1,0,1,0],
    [1,1,0,1,1]
]

B = [
    [1,0,0,0,0,0,1,1],
    [1,1,0,0,0,1,1,1],
    [1,1,0,0,0,1,1,0],
    [1,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,0,1],
    [1,0,0,1,1,0,0,0]
]

minsp = 0.3
minconf = 1

'''
    A
    1,2,3,4,5
    12,13,14,15,24,25,34,45 !34
    124,125,134,145,245 !134
    1245!
    134, 1245
'''

# do(A,minsp,minconf)
# print(Apriori(A,minsp))
print(getSupportList(A,minsp))

# SpMaxA = getSupportMaxList(A,minsp)
# print(SpMaxA)
# print(AssociativeRules(SpMaxA, A))

sepLine()

'''
    B
    45, 68, 178, 1267
'''

# do(B,minsp,minconf)
# print(Apriori(B,minsp))
# print(getSupportList(B,minsp))

# SpMaxB = getSupportMaxList(B,minsp)
# print(SpMaxB)
# print(AssociativeRules(SpMaxB, B))

import json

with open('DM/w5/lect5/assets/crawl/crawl_lottery.json', 'r') as j:
    json_data = json.load(j)

for obj in json_data:
    for each in obj:
        data_demo = (obj[each]) 

# for each in data_demo:
text = data_demo[0] #01844
test = [int(each) for each in text] #[0,1,8,4,4]

'''
    "03", 
    "0409"
    "01844", 
    "02595", 
    "02810",
    num contains numbers
    1   0   0   1   0   0   0   0   0   0
    2   0   0   0   1   0   0   0   0   1
    1   1   0   0   2   0   0   0   1   0
    1   0   1   0   0   2   0   0   0   1
    2   1   1   0   0   0   0   0   1   0

'''
sys.stdout.flush()
