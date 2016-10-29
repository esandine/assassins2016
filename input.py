def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    dict = {}
    for row in content:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(int)(row[1])
    return dict

def leaderboard():
    html = "<!DOCTYPEhtml><html> <head> <title> Assassins </title> </head> <body> <h1> Assassins Leaderboard </h1> "
    html+="<table border =1 width =600><thead> <tr> <th> Person </th> <th> Kills </th></tr></thead><tbody>"
    kills = importation("kills.csv");    
    for user in kills.keys():
        html+="<tr><td>"+user+"</td><td>"+str(kills[user])+"</td></tr>"
    html+="</tbody></table></body></html>"
    file = open("index.html", 'w')
    file.write(html)
    file.close()
    return 0

leaderboard()
