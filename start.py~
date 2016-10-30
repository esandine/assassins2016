import random
import hashlib
def start():
    #Reads names.csv and adds all to kills.csv for leaderboard
    instream = open("names.csv", 'r')
    names =  instream.read()
    names =  names.split('\n')
    instream.close()
    retstr=""
    i=0
    while(i<len(names)):
        retstr+=names[i]
        retstr+=",0\n"
        i+=1
    file = open("kills.csv",'w')
    file.write(retstr)
    file.close()
    #randomizes the list
    newNames=[]
    while(len(names)>0):
        i = random.randint(0,len(names)-1)
        newNames.append(names.pop(i))
    #Prints who has who
    for player in newNames:
        if newNames.index(player) == len(newNames)-1:
            print player + " kills " + newNames[0]
        else:
            print player + " kills " + newNames[newNames.index(player)+1]
    #Hashes everyone
    retstr=""
    for player in newNames:
        h=hashlib.md5()
        h.update(player)
        retstr+=h.hexdigest()
        retstr+=","
    #Write to a names.csv
    instream = open("list.csv", 'w')
    instream.write(retstr[:-1])
    instream.close()    

start()
