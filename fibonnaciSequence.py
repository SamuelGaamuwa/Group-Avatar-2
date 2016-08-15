def fibonnaci_sequence(num):
	numbers = [0,1]
	last = 1
	while(last != num):
		numbers.append(numbers[len(numbers)-1]+numbers[len(numbers)-2])
		last = numbers[len(numbers)-1]
	print(numbers)

fibonnaci_sequence(34)			