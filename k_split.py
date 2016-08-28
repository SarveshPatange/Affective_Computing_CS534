import csv

read_file = "D:\\USC\\CS-534 Affective Computing\\PokerDataFACET\\DB_data_scaled_100.csv"


with(open(read_file,"r")) as ip:
	reader = csv.reader(ip, delimiter=',')
	data = list(reader)
	row_count = len(data)
	rows_in_file = row_count//10
	count = 0
	for i in range(0,10):
		for j in range(0,rows_in_file):
			out_file = str(i) + "fold.csv"
			out = open(out_file, "w")
			for x in range(0,len(data[0])):
				if(x == len(data[0])-1):
					out.write(data[count][x])
					out.write("\n")
				else:
					out.write(data[count][x])
					out.write(",")
				
			count += 1
			print(count)
		print(out_file)
	
		
	