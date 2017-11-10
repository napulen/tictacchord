import math

transitions = {
	'null':['I','vi'],
	'I':['IV','vi','V'],
	'IV':['V','I','vi'],
	'vi':['ii','IV','V/vi'],
	'V':['I','vi'],
	'ii':['vi','V','V/vi'],
	'V/V':['V'],
	'V7/IV':['IV'],
	'V/vi':['vi'],
	'V7':['I']
}

travelled=[]

def recurseKey(key, indent=0):
	for x in transitions[key]:
		print('{}{}'.format('\t'*indent,x))
		if x not in travelled:
			travelled.append(x)
			recurseKey(x, indent+1)

recurseKey('null')

