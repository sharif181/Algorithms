from operator import attrgetter

class PROCESS():
    def __init__(self,process,AT,BT):
        self.process = process
        self.AT=AT
        self.BT=BT

class PROCESS2():
    def __init__(self,process,AT,BT,PR):
        self.process = process
        self.AT=AT
        self.BT=BT
        self.PR=PR

class info(PROCESS):
    def __init__(self,process,AT,BT,RT,TAT,WT):
        super().__init__(process,AT,BT)
        self.RT = RT
        self.TAT = TAT
        self.WT = WT

class info2(PROCESS2):
    def __init__(self,process,AT,BT,PR,RT,TAT,WT):
        super().__init__(process,AT,BT,PR)
        self.RT = RT
        self.TAT = TAT
        self.WT = WT

def minObj(ready):
    n = len(ready)
    index = 0
    for i in range(n):
        if ready[i].BT < ready[index].BT:
            index = i
    return index

def minobj2(queue):
    n = len(queue)
    index = 0
    for i in range(n):
        if queue[i].AT < queue[index].AT:
            index = i
    return index

def minobj3(queue):
    n = len(queue)
    index = 0
    for i in range(n):
        if queue[i].PR < queue[index].PR:
            index = i
    return index

def SJF_non():
    n = int(input("Number of processes "))
    table = []
    gantChart = []
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time "))
        BT = int(input("Process Brust time "))
        obj = PROCESS(process,AT,BT)
        table.append(obj)
    
    taskTime = 0
    ready=[]
    while( True ):
        if len(ready)==0 and len(table) == 0:
            break
        
        k = []
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                ready.append(table[i])
                k.append(i)
        
        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1
         

        if len(ready):
            index = minObj(ready)
            RT = taskTime - ready[index].AT
            taskTime = taskTime + ready[index].BT
            TAT = taskTime - ready[index].AT
            WT = TAT - ready[index].BT
            objTemp = info(ready[index].process,ready[index].AT,ready[index].BT,RT,TAT,WT)
            gantChart.append(objTemp)
            ready.pop(index)
        else:
            taskTime += 1   

    totalTat = 0
    totalWt = 0
    totalRt = 0
    seq=[]
    
    for pro in gantChart:
        seq.append(pro.process)
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT
    gantChart.sort(key = attrgetter('process'))

    print("Process\t\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in gantChart:
        print(f"{item.process}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")
    print("Gant Chart : ",end='')
    for i in seq:
        print(i,end=" ")
    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")

def SJF_preemtive():
    n = int(input("Number of processes "))
    table = []
    final_table = []
    BrustTime = []
    temTable = []
    gantChart = []
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time "))
        BT = int(input("Process Brust time "))
        BrustTime.append(BT)
        obj = PROCESS(process,AT,BT)
        temTable.append(obj)
        table.append(obj)
    taskTime = 0
    queue = [] 
    resTime = []
    completeTime = []
    while True:
       
        if len(queue)==0 and len (table)==0:
            break

        k=[]
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                queue.append(table[i])
                k.append(i)

        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1
        
        if len(queue):
            index = minObj(queue)
            flag = False
            for value,pro in resTime:
                if pro == queue[index].process:
                    flag = True
                    break

            if not flag:
                res = taskTime-queue[index].AT
                resTime.append((res,queue[index].process))
            
            queue[index].BT -= 1
            taskTime += 1
            if len(gantChart)==0:
                gantChart.append(queue[index].process)
            else:
                if queue[index].process != gantChart[len(gantChart)-1]:
                    gantChart.append(queue[index].process)
            if queue[index].BT == 0:
                completeTime.append((taskTime,queue[index].process))
                queue.pop(index) 
        else:
            taskTime += 1   

    resTime.sort(key = lambda x: x[1]) 
    completeTime.sort(key = lambda x: x[1]) 
    for i in range(n):
        tat = completeTime[i][0] - temTable[i].AT
        wt = tat - BrustTime[i]
        tempObj = info(temTable[i].process,temTable[i].AT,BrustTime[i],resTime[i][0],tat,wt)
        final_table.append(tempObj)


    print("Process\t\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in final_table:
        print(f"{item.process}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")


    totalTat = 0
    totalWt =  0
    totalRt =  0
    print("Gant Chart : ",end=" ")
    for item in gantChart:
        print(item,end=" ")
    for pro in final_table:
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")

def FCFS():
    n = int(input("Number of processes "))
    table = []
    gantChart = []
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time "))
        BT = int(input("Process Brust time "))
        obj = PROCESS(process,AT,BT)
        table.append(obj)

    taskTime = 0
    queue = [] 

    while True:
        if len(queue)==0 and len (table)==0:
            break

        k=[]
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                queue.append(table[i])
                k.append(i)

        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1

        if len(queue):
            index = minobj2(queue)
            RT = taskTime - queue[index].AT
            taskTime = taskTime + queue[index].BT
            TAT = taskTime - queue[index].AT
            WT = TAT - queue[index].BT
            objTemp = info(queue[index].process,queue[index].AT,queue[index].BT,RT,TAT,WT)
            gantChart.append(objTemp)
            queue.pop(index)
        else:
            taskTime += 1   

    totalTat = 0
    totalWt = 0
    totalRt = 0
    seq=[]
    for pro in gantChart:
        seq.append(pro.process)
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT
    gantChart.sort(key = attrgetter('process'))

    print("Process\t\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in gantChart:
        print(f"{item.process}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")
    print("Gant Chart : ",end='')
    for i in seq:
        print(i,end=" ")

    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")
        
def PSN():
    n = int(input("Number of processes "))
    table = []
    gantChart = []
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time: "))
        BT = int(input("Process Brust time: "))
        PR = int(input("Process Priority: "))
        obj = PROCESS2(process,AT,BT,PR)
        table.append(obj)

    taskTime = 0
    queue = [] 

    while True:
        if len(queue)==0 and len (table)==0:
            break

        k=[]
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                queue.append(table[i])
                k.append(i)

        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1

        if len(queue):
            index = minobj3(queue)
            RT = taskTime - queue[index].AT
            taskTime = taskTime + queue[index].BT
            TAT = taskTime - queue[index].AT
            WT = TAT - queue[index].BT
            objTemp = info2(queue[index].process,queue[index].AT,queue[index].BT,queue[index].PR,RT,TAT,WT)
            gantChart.append(objTemp)
            queue.pop(index)
        else:
            taskTime += 1   

    totalTat = 0
    totalWt = 0
    totalRt = 0
    seq=[]
    for pro in gantChart:
        seq.append(pro.process)
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT
    gantChart.sort(key = attrgetter('process'))
    print("Process\t\tPriority\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in gantChart:
        print(f"{item.process}\t\t{item.PR}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")
    print("Gant Chart : ",end='')
    for i in seq:
        print(i,end=" ")

    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")

def PSP():
    n = int(input("Number of processes "))
    table = []
    final_table = []
    BrustTime = []
    temTable = []
    gantChart = []
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time "))
        BT = int(input("Process Brust time "))
        BrustTime.append(BT)
        PR = int(input("Process Priority: "))
        obj = PROCESS2(process,AT,BT,PR)
        temTable.append(obj)
        table.append(obj)
    taskTime = 0
    queue = [] 
    resTime = []
    completeTime = []
    while True:    
        if len(queue)==0 and len (table)==0:
            break
        k=[]
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                queue.append(table[i])
                k.append(i)

        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1
        
        if len(queue):
            index = minobj3(queue)
            flag = False
            for value,pro in resTime:
                if pro == queue[index].process:
                    flag = True
                    break

            if not flag:
                res = taskTime-queue[index].AT
                resTime.append((res,queue[index].process))
            
            queue[index].BT -= 1
            taskTime += 1
            if len(gantChart)==0:
                gantChart.append(queue[index].process)
            else:
                if queue[index].process != gantChart[len(gantChart)-1]:
                    gantChart.append(queue[index].process)
            if queue[index].BT == 0:
                completeTime.append((taskTime,queue[index].process))
                queue.pop(index) 
        else:
            taskTime += 1   

    resTime.sort(key = lambda x: x[1]) 
    completeTime.sort(key = lambda x: x[1]) 
    for i in range(n):
        tat = completeTime[i][0] - temTable[i].AT
        wt = tat - BrustTime[i]
        tempObj = info2(temTable[i].process,temTable[i].AT,BrustTime[i],temTable[i].PR,resTime[i][0],tat,wt)
        final_table.append(tempObj)

    final_table.sort(key=attrgetter('process'))
    print("Process\t\tPriority\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in final_table:
        print(f"{item.process}\t\t{item.PR}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")


    totalTat = 0
    totalWt =  0
    totalRt =  0
    print("Gant Chart : ",end=" ")
    for item in gantChart:
        print(item,end=" ")
    for pro in final_table:
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")


def RR():
    n = int(input("Number of processes "))
    table = []
    final_table = []
    BrustTime = []
    temTable = []
    gantChart = []
    quantum = int(input("Enter quantum Time: "))
    for i in range(n):
        process = 'P'+str((i+1))
        AT = int(input("Process arival time "))
        BT = int(input("Process Brust time "))
        BrustTime.append(BT)
        obj = PROCESS(process,AT,BT)
        temTable.append(obj)
        table.append(obj)
    taskTime = 0
    queue = [] 
    resTime = []
    completeTime = []
    kk=0
    while True:    
        print("len queue: ",len(queue))
        print("len table: ",len(table))
        if len(queue)==0 and len(table)==0:
            break
        k=[]
        for i in range(len(table)):
            if table[i].AT <= taskTime:
                queue.append(table[i])
                k.append(i)
        if kk > 0:
            tempO=queue[0]
            queue.pop(0)
            queue.append(tempO)
        kk +=1
        minus = 0
        for idx in k:
            idx = idx - minus
            table.pop(idx)
            minus += 1
        
        if len(queue):
            index = 0
            flag = False
            for value,pro in resTime:
                if pro == queue[index].process:
                    flag = True
                    break

            if not flag:
                res = taskTime-queue[index].AT
                resTime.append((res,queue[index].process))
            
            if queue[index].BT >= quantum:
                queue[index].BT -= quantum
                taskTime = taskTime + quantum
                gantChart.append(queue[index].process)
                if queue[index].BT == 0:
                    completeTime.append((taskTime,queue[index].process))
                    queue.pop(index)
                    kk=0
            else:
                taskTime +=queue[index].BT
                gantChart.append(queue[index].process)
                completeTime.append((taskTime,queue[index].process))
                queue.pop(index)
                kk=0
        else:
            taskTime += 1   

    resTime.sort(key = lambda x: x[1]) 
    completeTime.sort(key = lambda x: x[1]) 
    for i in range(n):
        tat = completeTime[i][0] - temTable[i].AT
        wt = tat - BrustTime[i]
        tempObj = info(temTable[i].process,temTable[i].AT,BrustTime[i],resTime[i][0],tat,wt)
        final_table.append(tempObj)

    final_table.sort(key=attrgetter('process'))
    print("Quantam Time: ",quantum)
    print("Process\t\tArrival Time\t\tBrust Time\tTAT\tWT\tRS")
    for item in final_table:
        print(f"{item.process}\t\t{item.AT}\t\t\t{item.BT}\t\t{item.TAT}\t{item.WT}\t{item.RT}")


    totalTat = 0
    totalWt =  0
    totalRt =  0
    print("Gant Chart : ",end=" ")
    for item in gantChart:
        print(item,end=" ")
    
    for pro in final_table:
        totalTat += pro.TAT
        totalWt += pro.WT
        totalRt += pro.RT    
    print() 
    print(f"Average TAT: {totalTat/n}")
    print(f"Average WT: {totalWt/n}")
    print(f"Average RT: {totalRt/n}")




option = int(input("1.FCFS\n2.SJF non preemtive \n3.SJF preemtive\n4.Priority Schduling Non preemtive\n5.Priority Schduling preemtive\n6.Round Robin\nSelect your Choice: "))
if option == 1:
    FCFS()
elif option == 2:
    SJF_non()
elif option == 3:
    SJF_preemtive()
elif option == 4:
    PSN()
elif option == 5:
    PSP()
elif option == 6:
    RR()

