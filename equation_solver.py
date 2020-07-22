import model_sym

if __name__ == '__main__':
	first = model_sym.equation()
	var = input("Add Variables name: ")
	first.add_variable(var)
	static_var = input("Add Static Variables name(if any): ")
	first.add_static_variable(static_var)
	try:
		assert len(var)>0 or len(static_var)>0
	except:
		print('Enter a valid input')

	n = int(input("Number of equations: "))
	count = n
	while(n>0):
		eq = input(f'Enter equation-{-n+count+1}: ')
		first.add_equation(eq)
		n -= 1
	
	print("Summary:-")
	print(first.summary())

	solution = first.solution()
	print("Solution is:")
	print(solution)


