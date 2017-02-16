import psutil
from operator import itemgetter


class Network_Connection_Status:
    __pid = "pid"
    __laddr = "laddr"
    __raddr = "raddr"
    __status = "status"

    def __init__(self, pid, laddr, raddr, status):
        self.__pid = pid
        self.__laddr = laddr
        self.__raddr = raddr
        self.__status = status

    def set_pid(self, value):
        self.__pid = value

    def set_laddr(self, value):
        self.__laddr = value

    def set_raddr(self,value):
        self.__raddr = value
    
    def set_status(self, value):
        self.__status = value

    def get_pid(self):
        return self.__pid
    
    def get_laddr(self):
        return self.__laddr
    
    def get_raddr(self):
        return self.__raddr
    
    def get_status(self):
        return self.__status

#Sorting PID with no of connections

def make_sl(nl):
    sl = []
    temp_pid = 0
    count = 1
    for x in range(1,len(nl)):
        temp_pid = nl[x-1][0]
        if nl[x][0] == nl[x-1][0]:
            temp_pid = nl[x-1][0]
            count +=1
        else:
            sl.append([temp_pid,count])
            count = 1
    sl.append([temp_pid,count])
    sl = sorted(sl,key=itemgetter(1))
    return sl



#Creating the connection list from psutil command

tc = psutil.net_connections()
count = len(tc)
firstobject = Network_Connection_Status("pid", "laddr", "raddr", "status")

objectlist = []
print "\"", "pid", "\", \"", "laddr", "\", \"","raddr", "\", \"","status","\""


for x in range(count):
    temp = Network_Connection_Status(tc[x].pid, tc[x].laddr, tc[x].raddr, tc[x].status)
    if tc[x].status != 'NONE' and tc[x].status != 'LISTEN':
        objectlist.append([temp.get_pid() , temp.get_laddr(), temp.get_raddr(), temp.get_status(),temp])

nl = sorted(objectlist,key=itemgetter(0))

'''
for x in range(len(nl)):
    print "\"", nl[x][4].get_pid(), "\", \"", nl[x][4].get_laddr(), "\", \"",nl[x][4].get_raddr(), "\", \"",nl[x][4].get_status(),"\""
'''

sortedlist = make_sl(nl)







