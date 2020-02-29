equation = 'y = -12x + 10.2'
x = int(input('Add x: '))

split_result = equation.split()
numberx = float(split_result[2].replace("x", '')) * x
y = numberx + float(split_result[4])
print(y)