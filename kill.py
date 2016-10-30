import hashlib
def kill():
    killer = input("Who got a kill (put in quotations): ")
    file = open("leaderboard.csv","r")
    #Updates Leaderboard
    leaderboard=file.readlines()
    file.close()
    dict = {}
    for row in leaderboard:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(int)(row[1])
    if killer in dict.keys():
        dict[killer]+=1
    else:
        print "Killer not found"
        return 0
    retstr=""
    for user in dict.keys():
        retstr+=user
        retstr+=","
        retstr+=str(dict[user])
        retstr+="\n"
    file = open("leaderboard.csv","w")
    file.write(retstr)
    file.close()
    #Kills a player
    file = open("list.csv","r")
    list=file.read()
    file.close()
    list=list.split(",")
    h=hashlib.md5()
    h.update(killer)
    killer=h.hexdigest()
    #Finds hash of killed player and kills it
    i =0
    while i < len(list):
        if killer == list[i]:
            if i==len(list)-1:
                list.pop(0)
                target=list[0]
                i=len(list)
            elif i==len(list)-2:
                list.pop(len(list)-1)
                target=list[0]
                i=len(list)
            else:
                list.pop(i+1)
                target=list[i+1]
                i=len(list)
        i+=1
    retstr=""
    for user in list:
        retstr+=user
        retstr+=","
    retstr=retstr[:-1]
    file = open("list.csv","w")
    file.write(retstr)
    file.close()

kill()
