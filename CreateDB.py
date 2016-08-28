import csv
import sqlite3
import glob
import os

root_path = "C:\\USC\\CS-534 Affective Computing\\PokerDataFACET\\PokerDataFACET"

conn = sqlite3.connect('facet.db')
c = conn.cursor()
"""
c.execute("CREATE TABLE facetdata (frametime REAL, face_X INTEGER,face_Y INTEGER,face_width INTEGER,face_height INTEGER, angerEvidence REAL, contemptEvidence REAL, disgustEvidence REAL, joyEvidence REAL, fearEvidence REAL, negativeEvidence REAL, neutralEvidence REAL, positiveEvidence REAL, sadnessEvidence REAL, surpriseEvidence REAL, confusionEvidence REAL, frustrationEvidence REAL, angerIntensity REAL, contemptIntensity REAL, disgustIntensity REAL, joyIntensity REAL, fearIntensity REAL, negativeIntensity REAL, neutralIntensity REAL, positiveIntensity REAL, sadnessIntensity REAL, surpriseIntensity REAL, confusionIntensity REAL, frustrationIntensity REAL, AU1Evidence REAL, AU2Evidence REAL, AU4Evidence REAL, AU5Evidence REAL, AU6Evidence REAL, AU7Evidence REAL, AU9Evidence REAL, AU10Evidence REAL, AU12Evidence REAL, AU14Evidence REAL, AU15Evidence REAL, AU17Evidence REAL, AU18Evidence REAL, AU20Evidence REAL, AU23Evidence REAL, AU24Evidence REAL, AU25Evidence REAL, AU26Evidence REAL, AU28Evidence REAL)")

"""
dirs = os.listdir(root_path)
count = 0
check_file = "java_framedata.txt"
read_file = "FACET_emotient_new.csv"
for files in dirs:
    path = os.path.join(root_path,files)
    print(path)
    if check_file in os.listdir(path):
        with open(os.path.join(path,check_file), 'r') as check:
            for line in check:
                l = line.strip().split(',')
                if len(l) > 3 and l[3] == 'poker':
                    t = 1
                    with open(os.path.join(path,read_file), 'r') as read:
                        print("Reading poker file")
                        reader = csv.reader(read,delimiter=',')
                        for row in reader:
                            if t == 1:
                                t = 0
                                continue
                            to_db = []
                            for element in row:
                                to_db.append(element)
                            stmt = "INSERT INTO facetdata VALUES(%s);" % ','.join('?' * len(to_db))
                            print(to_db)
                            print(stmt)
                            c.executemany(stmt, to_db)

                count += 1




print(count)
