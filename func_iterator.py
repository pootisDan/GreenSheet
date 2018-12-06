import math
def do_func(var_x, start_x):
	new_x = math.pow(var_x, 2) + start_x
	#print(new_x)
	return new_x
done = False

x_to_do = [1,0,-1,2,.5,-2,-3,-1.5,.25,-.5,.6,.4,.001,.8,1.001,3.14159,.12,.3,-.005,4]



for x in x_to_do:
	done = False
	x = float(x)
	iterations = 0
	begin_x = x
	going_x = x
	while(done == False and iterations < 500):
		going_x = do_func(going_x, begin_x)
		iterations = iterations + 1
		if(going_x>3):
			done = True
	print(x, iterations)
