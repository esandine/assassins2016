def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    dict = {}
    for row in content:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(int)(row[1])
    return dict

def sortDict(dict):
    max = -1
    players = []
    kills = []
    while len(dict)>0:
        for user in dict.keys():
            if dict[user]>max:
                currentuser = user
                max = dict[user]
        players.append(currentuser)
        kills.append(max)
        dict.pop(currentuser)
        max = -1
        #print dict.keys()
    return players,kills
def leaderboard():
    html = "<!DOCTYPEhtml><html> <head> <title> Assassins </title> </head> <body> <h1> Assassins Leaderboard </h1> "
    html+="<table border =1 width =600><thead> <tr> <th> Person </th> <th> Kills </th></tr></thead><tbody>"
    kills = importation("leaderboard.csv")
    ret=sortDict(kills)
    users=ret[0]
    kill=ret[1]
    i=0
    while i < len(users):
        html+="<tr><td>"+users[i]+"</td><td>"+str(kill[i])+"</td></tr>"
        i+=1;
    html+="</tbody></table></body></html>"
    file = open("index.html", 'w')
    file.write(html)
    file.close()
    return 0

leaderboard()

