import csv
import re
import sqlite3
import datetime


root_path = "C:\\USC\\CS-534 Affective Computing\\PokerDataFACET\\PokerDataFACET"

conn = sqlite3.connect('facet.db')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
result_set = c.fetchall()

data = []
with open('bet_info.csv', "r") as csv_file:
    read = csv.reader(csv_file, delimiter="\t")
    for row in read:
        s = 'session' + row[0]
        start = int(row[4])
        end = int(row[5])
        start /= 1000
        end /= 1000
        c.execute("WITH subset (average) AS ( SELECT AVG(positiveIntensity) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end) +" and positiveEvidence > 0.0 ) SELECT avg(100*positiveIntensity* positiveIntensity * (positiveIntensity - (SELECT average FROM subset)) * (positiveIntensity - (SELECT average FROM subset)) * (positiveIntensity - (SELECT average FROM subset)) * (positiveIntensity - (SELECT average FROM subset))) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end))
        pos = c.fetchall()
        row.append(pos[0][0])
        c.execute("WITH subset (average) AS ( SELECT AVG(negativeIntensity) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end) +" and negativeEvidence > 0.0 ) SELECT avg(100*negativeIntensity* negativeIntensity * (negativeIntensity - (SELECT average FROM subset)) * (negativeIntensity - (SELECT average FROM subset)) * (negativeIntensity - (SELECT average FROM subset)) * (negativeIntensity - (SELECT average FROM subset))) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end))
        neg = c.fetchall()
        row.append(neg[0][0])
        c.execute("WITH subset (average) AS ( SELECT AVG(neutralIntensity) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end) +" and neutralEvidence > 0.0 ) SELECT avg(100*neutralIntensity* neutralIntensity * (neutralIntensity - (SELECT average FROM subset)) * (neutralIntensity - (SELECT average FROM subset)) * (neutralIntensity - (SELECT average FROM subset)) * (neutralIntensity - (SELECT average FROM subset))) FROM " + s +"  where Frametime >= "+str(start)+" and Frametime <= "+ str(end))
        neu = c.fetchall()
        row.append(neu[0][0])
        data.append(row)
        

out = open('player_face_data.csv', "w")
for d in data:
    for val in d:
        out.write(str(val))
        out.write(",")
    out.write("\n")
