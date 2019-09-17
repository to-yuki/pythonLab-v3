empList = {'001':['Yamada','090-xxxx-xxxx'], 
           '002':['Tanaka','080-xxxx-xxxx'], 
           '003':['Suzuki','070-xxxx-xxxx']}

def empSearch(no): 
    empData = None
    try:
        empData = empList[no]
        if (empData != None):
            return empData[0],empData[1]
    except:
        return None,None
