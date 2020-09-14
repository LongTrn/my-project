
from itertools import combinations as C

arr = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]]
sett = {}
string = [''.join([str(item) for item in order]) for order in arr]
# string = ['12', '13', '14', '15', '24', '25', '34', '35']
for key in string:
    sett.setdefault(key,0.0)
# sett = {'12': 0.0, '13': 0.0, '14': 0.0, '15': 0.0, '24': 0.0, '25': 0.0, '34': 0.0, '35': 0.0}
minNEle = min([len(each) for each in sett])
maxNEle = max([len(each) for each in sett])

# arrange a max list having each length's element ascending
arr = {eles for each in [[each for each in sett if len(each) == i] for i in range(minNEle, maxNEle + 1)] for eles in each}

# ano = {'1':0.0,'132':0.0}
# sett.update(ano.copy())
# sett.keys
test = sett.copy()

# for each in test:
#     print('each:', each)
#     for eles in list(test)[list(test).index('12'):]:
#         print('eles:', eles)
#         flag=0
#         for i in each:
#             if i in eles:
#                 flag += 1
#         if flag == len(each): 
#             test.remove(each)
#             break
# tmp = list(test).index('12') # index like list
# first2pairs = list(test)[list(test).index('12'):] # arr[arr.index(each)]
# first2pairs = {k: test[k] for k in list(test)[1:]} # arr[arr.index(each)] 



# sett_items = sett.items()[0]
# print(sett_items)
# for each in sett.items():
    # print((each)[0])
    # print((each)[1])
# supportMaxList = arrangeAscending(test)
# {'12': 0.0, '13': 0.0, '14': 0.0, '15': 0.0, '24': 0.0, '25': 0.0, '34': 0.0, '35': 0.0}
    
def notDup(arr, check):
    return not (arr in check)

def combine(arr):
    output = {}
    for each in list(arr)[:-1]:
        for ele in list(arr)[list(arr).index(each) + 1:]:
            string = sorted(set(''.join(each + ele)))
            newKey = (''.join(string))
            output.setdefault(newKey, 0.0)
    return output

demo = {'1':0.0, '2': 0.0}
arr = sett.copy()

def countElements(arr, T):
    output = 0
    for each in T:
        count = 0
        # print('each',each)
        for ele in arr:
            # for char in ele:
            if each.count(ele): count += 1
            # print('\nele', ele, 'count', each.count(ele))
        if count == len(arr): output += 1
    # print(output)

    return output

def checkSP(arr,T,minsp):
    tmp_arr = []
    for each in arr:
        tmp_arr.append(int(each))
    sup = countElements(tmp_arr,T)/len(T)
    return (sup)

def arrangeAscending(arr):
    # get min max length of each element of list
    minNEle = min([len(each) for each in arr])
    maxNEle = max([len(each) for each in arr])

    # arrange a max list having each length's element ascending
    arr = {eles: arr[eles] for each in [{each for each in arr if len(each) == i} for i in range(minNEle, maxNEle + 1)] for eles in each}
    return arr

# get not Duplicates for support Max List
def validate(supportMaxList, arr = {}):
    # combine into a sorted support max list
    supportMaxList.update(arr.copy())

    # arrange a max list having each length's element ascending
    supportMaxList = arrangeAscending(supportMaxList)

    # temporary result to eleminate not max elements
    maxList = supportMaxList.copy()
    for each in maxList:
        for eles in list(maxList)[list(maxList).index(each)+1:]:
            flag=0
            for i in each:
                if i in eles:
                    flag += 1
            if flag == len(each): 
                list(supportMaxList).remove(each)
                break
    return supportMaxList

def doApriori(arr, T, minsp, supportList = {}, supportMaxList = {}):
    # get combinations
    arr = combine(arr)
    init = arr.copy()

    # eliminating
    # check support fit condition of minsp
    for each in arr:
        i = list(arr).index(each)
        arr[each] = checkSP(each, T, minsp)
    arr = {each: arr[each] for each in arr if arr[each] > minsp}
    
    # find out support list and max list
    tmp = {each:arr[each] for each in arr if each not in supportList}
    supportList.update(tmp.copy())
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
    init_arr = (list((range(max_ele + 2)))) #
    init_dict = {}
    string = ''.join([str(item) for item in init_arr])
    for key in string:
        init_dict.setdefault(key,0.0)

    totalList = doApriori(init_dict,T,minsp,{},{})
    
    SupportList = totalList[0]
    SupportMaxList = totalList[1]
    
    return (SupportList, SupportMaxList)

def getAssociativeRule(arr, inputArr, minconf):
    print(type(arr))
    print(arr)
    arr = [int(each) for each in sorted((set(''.join(arr))))]
    print(string)
    allAssociativeRules = {}
    for i in (range(1,len(arr))):
        c = [list(ele) for ele in list(C(arr,i))]
        print(type(c))
        print(c)
        for ele in c:
            rest = [i for i in arr if i not in ele]
            # print(ele)
            countEle = countElements(ele,inputArr)
            countArray = countElements(arr,inputArr)
            conf = countArray/countEle
            print('chec', ele, rest)
            if conf >= minconf:
                allAssociativeRules.setdefault(str(ele) + '->' + str(rest), conf)
    
    return allAssociativeRules
    
def AssociativeRules(inputArr, minsp, minconf):
    allAssociativeRules = {}
    supportMaxList = Apriori(inputArr, minsp)[1]
    for each in supportMaxList:
        allAssociativeRules.setdefault(str(getAssociativeRule(each, inputArr, minconf)), 0.0)

    return (allAssociativeRules)

def export(argument, trained_data, minsp, minconf):
    switcher = {
        'Apriori': Apriori(trained_data, minsp),
        'AssociativeRules': AssociativeRules(trained_data, minsp, minconf),
    }
    # return switcher.get(argument, 'do_default(trained_data, minsp, minconf)')
    return switcher.get(argument, Apriori(trained_data, minsp))

A = [
        [1,3,4],
        [1,3,4],
        [3,5],
        [1,2,4,5],
        [1,2,4],
        [1,2,4,5]
    ]

options = 'AssociativeRules'
minsp = 0.3
minconf = 1

result = {
    "result": (export(options, A, minsp, minconf))
}
print(result)
sets = {'21'}