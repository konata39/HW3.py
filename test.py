file = open(sys.argv[2], 'r')
result = {}
found_1 = 0
found_2 = 0
for line in file:
	spilt_pair = line.split("\twikiPageRedirects\t")
	spilt_pair[1] = spilt_pair[1].split("\n")
	if spilt_pair[0] in result.keys():
		result[spilt_pair[0]] = result[spilt_pair[0]] + 1
	else:
		result[spilt_pair[0]]=1
	if spilt_pair[1][0] in result.keys():
		result[spilt_pair[1][0]] = result[spilt_pair[0]] + 1
	else:
		result[spilt_pair[1][0]]=1
