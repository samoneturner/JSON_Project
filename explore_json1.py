import json 

infile = open('eq_data_1_day_m1.json','r')
outfile = open('readable_eq_data.json','w')

eq_data = json.load(infile) #python recogonozes it as a dictionary and put it in the outfile as a dictionary

json.dump(eq_data, outfile, indent = 5) #indient 4 means it indents 4 times in the outfile 



