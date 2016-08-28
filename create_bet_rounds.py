import csv
import re

round_list = []
with open('output_data.csv', newline='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        temp_list = []
        for i in range(0,len(row)):
            if len(row[i]) != 0:
                temp_list.append(row[i])

        round_list.append(temp_list)

round_without_ans = []
for rounds in round_list:
    temp_rounds = []
    for ele in rounds:
        if len(ele) > 2:
            l = ele.replace('(','').replace(')','').replace('\'','').replace(' ','').split(',')
            temp_rounds.append(l)
        else:
            temp_rounds.append(ele)

    round_without_ans.append(temp_rounds)


final_rounds =[]
for r in round_without_ans:
    temp = []
    for x in r:
        flag = 0
        for y in x:
            if re.match('^answer.*',y):
                flag = 1
        if (flag ==0):
            temp.append(x)
    final_rounds.append(temp)


list_of_rounds = []
for r in final_rounds:
    flag = 0
    for v in r[1]:
        if re.match('bet.*',v):
            flag = 1
    if flag == 0:
        list_of_rounds.append(r)


final_list = []
for r in list_of_rounds:
    temp = []
    temp.append(r[0])
    temp.append(r[1])
    for i in range(2,len(r)):
        flag = 0
        for v in r[i]:
            if re.match('^card.*',v):
                flag = 1
        if flag == 0:
            temp.append(r[i])
    final_list.append(temp)

out_file = 'bet_info.csv'
out = open(out_file,"w")
for r in final_list:
    round_no = r[0]
    bet_number = 0
    s_id = r[1][0]
    opp_id = r[1][1]
    start = r[1][4]
    end = 0
    for i in range(2,len(r)):
        b_value = 0
        for value in r[i]:
            if re.match('bet.*',value):
                bet_number += 1
                b = value.split(':')
                b_value = b[1]

        out.write(s_id) #0
        out.write("\t")
        out.write(opp_id) #1
        out.write("\t")
        out.write(round_no) #2
        out.write("\t")
        out.write(str(bet_number)) #3
        out.write("\t")
        out.write(start) #4
        out.write("\t")
        out.write(r[i][4]) #5
        out.write("\t")
        out.write(b_value) #6
        out.write("\n")
        start = r[i][4]


out.close()
