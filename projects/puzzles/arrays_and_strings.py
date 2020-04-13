print('===CHECK DUPES===')
def checkIfDuplicates(string):
	for i in range(len(string)):
		print(i, string[i])
		for ii in range(i+1,len(string)):
			if string[i] == string[ii]:
				print('duplicate!')

checkIfDuplicates('yesthisiskendra')

print('===REVERSE STRING===')
def reverseString(string):
	for i in range(len(string)):
		print(string[len(string)-1-i])

reverseString('yesthisiskendra')

print('===REMOVE DUPES===')
def removeDupes(string):
	nodupes = []
	for letter in string:
		if letter not in nodupes:
			nodupes.append(letter)
	
	print(nodupes)

removeDupes('yesthisiskendra')

print('===ARE ANAGRAMS===')
def k_sort(string):
	for i in range(len(string)):
		for j in range(0, len(string)-1-i):
			if string[j] > string[j+1]:
				string[j+1], string[j] = string[j], string[j+1]
	return string

def are_anagrams(string1, string2):
	if k_sort(string1) == k_sort(string2):
		print('yes! anagrams!')
	else:
		print('sadly, not anagrams')

are_anagrams(list('angered'), list('enraged'))
are_anagrams(list('enraged'), list('cattaco'))