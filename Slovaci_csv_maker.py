import csv

text = """,,,,,Scoring,Scoring,Scoring,,,Goals,Goals,Goals,Goals,Assists,Assists,Assists,Shots,Shots,Shots,,,,,,,,,,
Name,Season,Age,Tm,Lg,GP,G,A,PTS,+/-,PIM,EV,PPG,SHG,GWG,EV,PP,SH,SOG,SPCT,TSA,TOI,ATOI,FOW,FOL,FO%,BLK,HIT,TK,GV,Awards
Slafkovsky,2022-23,18,MTL,NHL,39,4,6,10,-13,33,3,1,0,0,5,1,0,42,9.5,92,476,12:13,5,5,50.0,24,53,12,13,
Slafkovsky,2023-24,19,MTL,NHL,82,20,30,50,-19,55,14,6,0,2,22,8,0,152,13.2,314,1471,17:56,10,10,50.0,71,152,34,42,
Demitra,1993-94,19,OTT,NHL,12,1,1,2,-7,4,0,1,0,0,1,0,0,10,10.0,,,,,,,,,,,
Demitra,1994-95,20,OTT,NHL,16,4,3,7,-4,0,3,1,0,0,2,1,0,21,19.0,,,,,,,,,,,
Stastny,1980-81,24,QUE,NHL,77,39,70,109,10,37,26,11,2,4,48,22,0,232,16.8,,,AS-6Byng-16Calder-1Hart-11
Stastny,1981-82,25,QUE,NHL,80,46,93,139,-10,91,27,16,3,3,59,33,1,227,20.3,,,AS-3Hart-4
Hossa,1997-98,19,OTT,NHL,7,0,1,1,-1,0,0,0,0,0,0,1,0,10,0.0,,107,15:14,,,,,,,,
Hossa,1998-99,20,OTT,NHL,60,15,15,30,18,37,14,1,0,2,13,2,0,124,12.1,,839,13:59,,,,,,,,AR-1Calder-2
Gaborik,2000-01,18,MIN,NHL,71,18,18,36,-6,32,12,6,0,3,12,6,0,179,10.1,,1096,15:26,,,,,,,,Calder-7
Gaborik,2001-02,19,MIN,NHL,78,30,37,67,0,34,20,10,0,4,21,16,0,221,13.6,,1308,16:47,,,,,,,,AS-13
Satan,1995-96,21,EDM,NHL,62,18,17,35,0,22,12,6,0,4,12,5,0,113,15.9,,,,,,,,,,,Calder-11
Satan,1996-97,22,TOT,NHL,76,25,13,38,-3,26,18,7,0,3,9,4,0,119,21.0,,,,,,,,,,,"""
lines = text.split("\n")

csv_filename = "utocnici_stats.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    headers = lines[1].split(',')
    writer.writerow(headers)

    for line in lines[2:]:
        writer.writerow(line.split(','))

text = """,,,,,Scoring,Scoring,Scoring,,,Goals,Goals,Goals,Goals,Assists,Assists,Assists,Shots,Shots,Shots,,,,,,,,,,
Name,Season,Age,Tm,Lg,GP,G,A,PTS,+/-,PIM,EV,PPG,SHG,GWG,EV,PP,SH,SOG,SPCT,TSA,TOI,ATOI,FOW,FOL,FO%,BLK,HIT,TK,GV,Awards
Fehervary,2019-20,20,WSH,NHL,6,0,1,1,-2,6,0,0,0,0,1,0,0,7,0.0,16,96,15:59,0,0,,2,14,2,2,
Fehervary,2021-22,22,WSH,NHL,79,8,9,17,15,26,7,0,1,2,8,0,1,96,8.3,181,1553,19:39,0,0,,117,251,14,36,Calder-14
Chara,1997-98,20,NYI,NHL,25,0,1,1,1,50,0,0,0,0,1,0,0,10,0.0,,278,11:07,,,,,,,,
Chara,1998-99,21,NYI,NHL,59,2,6,8,-8,83,1,0,1,0,6,0,0,56,3.6,,1115,18:54,,,,,,,,
Sekera,2006-07,20,BUF,NHL,2,0,0,0,1,2,0,0,0,0,0,0,0,0,,,15,7:31,,,,,,,,
Sekera,2007-08,21,BUF,NHL,37,2,6,8,5,16,2,0,0,1,3,3,0,28,7.1,72,726,19:37,0,0,,50,19,14,14,
Cernak,2018-19,21,TBL,NHL,58,5,11,16,25,58,4,1,0,1,11,0,0,107,4.7,186,1117,19:15,0,0,,79,198,11,19,
Cernak,2019-20,22,TBL,NHL,67,5,7,12,11,59,5,0,0,1,7,0,0,125,4.0,206,1270,18:57,0,0,,97,172,18,28,
Visnovsky,2000-01,24,LAK,NHL,81,7,32,39,16,36,4,3,0,3,21,11,0,105,6.7,,1375,16:58,,,,,,,,AR-1AS-18Calder-4
Visnovsky,2001-02,25,LAK,NHL,72,4,17,21,-5,14,3,1,0,2,12,5,0,95,4.2,,1170,16:15,,,,,,,,
Nemec,2023-24,19,NJD,NHL,60,3,16,19,-7,33,3,0,0,1,14,2,0,73,4.1,201,1192,19:52,0,0,,105,22,18,25,"""
lines = text.split("\n")

csv_filename = "obrancovia_stats.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    headers = lines[1].split(',')
    writer.writerow(headers)

    for line in lines[2:]:
        writer.writerow(line.split(','))