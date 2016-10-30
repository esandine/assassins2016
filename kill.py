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
    #Loads Users into file
    file = open("list.csv","r")
    list=file.read()
    file.close()
    list=list.split(",")

    h=hashlib.md5()
    h.update(killer)
    killer=h.hexdigest()
    for user in list:
        if killer == user:
            killed=list.pop(list.index(user)+1)
    
kill()
