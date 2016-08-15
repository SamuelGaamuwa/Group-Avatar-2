def prime_number(num):
	if (num == 1):
		print (1) 
	elif (num == 0):
		print ("input a number larger than 0")
	else:
		primes = [1]
		for i in range(2, num):
			for d in range(2, i):
				if((i%d) == 0):
					break
				else:
					if(d == (i-1)):
						primes.append(i)
						print(primes)
prime_number(20)
			