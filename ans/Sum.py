list = [1,'2',3,'5',8,13,21,'34',55,89,144,233]
sum = 0
for val in list:
	try:
		sum += val
	except:
		print('Error Data:',end=' ')
		print(val)

print('sum :',end=' ')
print(sum)
