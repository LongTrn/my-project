'''
    Use Aprori to get Support List and Max Support List
    Use Associative Rules to get rules
'''

import sys
import json
from itertools import combinations as C

def notDup(arr, check):
    return not (arr in check)
    
def combine(arr):
    output = []
    for each in arr[:-2]:
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
    for each in T:
        count = 0
        # print('each',each)
        for ele in arr:
            if each.count(ele): count += 1
            # print('\nele', ele, 'count', each.count(ele))
        if count == len(arr): output += 1
    # print(output)

    return output

def checkSP(arr,T,minsp):
    sup = countElements(arr,T)/len(T)
    return (sup > minsp,sup)

def arrangeAscending(arr):
    if not len(arr): return arr
    # get min max length of each element of list
    minNEle = min([len(each) for each in arr])
    maxNEle = max([len(each) for each in arr])

    # arrange a max list having each length's element ascending
    arr = [eles for each in [[each for each in arr if len(each) == i] for i in range(minNEle, maxNEle + 1)] for eles in each]
    return arr

# get not Duplicates for support Max List
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

    return supportMaxList

def doApriori(arr, T, minsp, supportList = [], supportMaxList = []):
    # get combinations
    arr = combine(arr)
    init = arr.copy()

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
    # toString(init, arr, supportList, supportMaxList)

    if len(arr) > 0: return doApriori(arr, T, minsp, supportList,supportMaxList)
    supportList = arrangeAscending(supportList)
    return (supportList, supportMaxList)

def toString (init, arr, supportList, supportMaxList):
    print('get combination: \n', init, '\n')
    print('after eliminating: \n', arr, '\n')
    print('support list: \n', supportList, '\n')
    print('support max list: \n', supportMaxList, '\n')
    return;

def Apriori(T, minsp):
    max_ele = max([ len(order) for order in T])
    init_arr = list(range(max_ele)) #
    totalList = doApriori(init_arr,T,minsp,[],[])
    
    SupportList = totalList[0]
    SupportMaxList = totalList[1]
    
    return (SupportList, SupportMaxList)

def getSupportList(T, minsp):
    SupportList = Apriori(T, minsp)[0]
    
    return SupportList

def getSupportMaxList(T, minsp):
    SupportMaxList = Apriori(T, minsp)[1]
    
    return(SupportMaxList)

def getAssociativeRule(arr, inputArr, minconf):
   
    allAssociativeRules = []
    for i in (range(1,len(arr))):
        c = [list(ele) for ele in list(C(arr,i))]
        for ele in c:
            rest = [i for i in arr if i not in ele]
            # print(ele)
            countEle = countElements(ele,inputArr)
            countArray = countElements(arr,inputArr)
            conf = countArray/countEle
            if conf >= minconf:
                allAssociativeRules.append([ele, rest])
    
    return allAssociativeRules
    
def AssociativeRules(inputArr, minsp, minconf):
    allAssociativeRules = []
    supportMaxList = getSupportMaxList(inputArr, minsp)
    for each in supportMaxList:
        allAssociativeRules += getAssociativeRule(each, inputArr, minconf)

    return (allAssociativeRules)

def do_default(Arr, minsp = 0.3, minconf = 1):
    AprioriResult = Apriori(Arr,minsp)
    SupportList = getSupportList(Arr,minsp)
    SupportMaxList = getSupportMaxList(Arr,minsp)
    allAssociativeRules = AssociativeRules(Arr, minsp, minconf)
    
    return( Arr, minsp, Apriori, SupportList, 
            SupportMaxList, allAssociativeRules
    )

def sepLine():
    print('\n' + '#'*156 + '\n')

def get_raw_data(path):
    with open(path, 'r') as j:
        json_data = json.load(j)

    raw_data = []
    for obj in json_data:
        for each in obj:
            raw_data += (obj[each]) 

    return raw_data

def seperated_raw_data(raw_data):
    seperated_data = []
    for order in raw_data:
        # [[0, 1, 8, 4, 4] ..., [9, 9, 4]]
        seperate_orders = [int(item) for item in order] #[0,1,8,4,4]
        seperated_data.append(seperate_orders)

    return seperated_data

def get_trained_data(seperated_raw_data):
    trained_data = []
    max_ele = max([ max(each) for each in seperated_raw_data])
    
    for order in seperated_raw_data:
        tmp_init = [0]*(max_ele + 1)
        for item in order:
            tmp_init[item] = order.count(item)
        trained_data.append(tmp_init)

    return trained_data

'''
    1   get combinations
    2   check minsp
    3   eleminating
    
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
    
        A
        1,2,3,4,5
        12,13,14,15,24,25,34,45 !34
        124,125,134,145,245 !134
        1245!
        134, 1245

    # do_default(A,minsp,minconf)
    # print(Apriori(A,minsp))
    # print(getSupportList(A,minsp))

    # SpMaxA = getSupportMaxList(A,minsp)
    # print(SpMaxA)
    # print(AssociativeRules(SpMaxA, A))

    sepLine()

        B
        45, 68, 178, 1267

    # do_default(B,minsp,minconf)
    # print(Apriori(B,minsp))
    # print(getSupportList(B,minsp))

    # SpMaxB = getSupportMaxList(B,minsp)
    # print(SpMaxB)
    # print(AssociativeRules(SpMaxB, B))

    "03", 
    "0409"
    "01844", 
    "02595", 
    "02810",
    num contains numbers
    1, 0, 0, 1, 0, 0, 0, 0, 0, 0
    2, 0, 0, 0, 1, 0, 0, 0, 0, 1
    1, 1, 0, 0, 2, 0, 0, 0, 1, 0
    1, 0, 1, 0, 0, 2, 0, 0, 0, 1
    2, 1, 1, 0, 0, 0, 0, 0, 1, 0

    testdemo = [
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 2, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 2, 0, 0, 0, 1],
        [2, 1, 1, 0, 0, 0, 0, 0, 1, 0]
    ]
A = [
        [1,0,1,1,0],
        [1,0,1,1,0],
        [0,0,1,0,1],
        [1,1,0,1,1],
        [1,1,0,1,0],
        [1,1,0,1,1]
    ]
'''
A = [
    [1,3,4],
    [1,3,4],
    [3,5],
    [1,2,4,5],
    [1,2,4],
    [1,2,4,5],
]
minsp = 0.1
minconf = 1

# inputed_file_path = sys.argv[1]
options = str(sys.argv[1])
minsp = float(sys.argv[2])
minconf = float(sys.argv[3])

file_path = './../../assets/crawl/crawl_lottery.json';
raw_data = get_raw_data(file_path)
data = seperated_raw_data(raw_data)

def export(argument, data, minsp, minconf):
    switcher = {
        'Apriori': Apriori(data, minsp),
        'SupportList': getSupportList(data, minsp),
        'SupportMaxList': getSupportMaxList(data, minsp),
        'AssociativeRules': AssociativeRules(data, minsp, minconf),
    }
    return switcher.get(argument, do_default(data, minsp, minconf))

result = {
    "result": (export(options, A, minsp, minconf))
}
print(result)
sys.stdout.flush()
