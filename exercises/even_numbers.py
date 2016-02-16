def even_numbers(low, high):
	if type(low) != int or type(high) != int:
		print("Only Intergers are allowed as parameter")
		return
	if low > high :
		print("lower bound cannot be greater than the higher bound")
		return

	for i in range(low, high):
		if i%2 == 0 :
			print(i)

even_numbers(0, 10)
