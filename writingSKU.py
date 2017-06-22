#read input test.csv, keyset.csv
#parse data in keyset and set up hashmap
#search test.csv for keys
#replace values
import sys

if len(sys.argv) != 2:
	print("Bad input file provided")
	sys.exit(0)
else:
	name = str(sys.argv[1])

map = {}
keySet = open("keySet.csv", "r")
#0 index is key, 1 index is value

for line in keySet:
	line = line.replace(" ", "")
	data = line.split(',')
	map[data[0]] = data[1]
	
keySet.close()

rawSKU = []
inputFile = open(name, "r")
for line in inputFile:
	val = line.strip()
	val = val.replace(",", "")
	rawSKU.append(val)

inputFile.close()


with open("out.csv", "w") as output:
	for item in rawSKU:
		if item in map:
			output.write(map[item] + ",\n")
		else:
			output.write(item + ",\n")

output.close()