from palette_import_lib import *
import os
import math

my_dir = os.path.dirname(os.path.realpath(__file__))

palette_filename = 'CHROMA.MAP.csv'

palette_dict = read_palette_from_file(my_dir + '/' + palette_filename)

assigned_colors = dict()
filename = "C:/Users/01nevets/Documents/testPrjFolder/Palette_Import/saved_colors.csv"


def do_func(var_x, start_x):
	new_x = math.pow(var_x, 2) + start_x
	#print(new_x)
	return new_x
done = False

x_to_do = [1,0,-1,2,.5,-2,-3,-1.5,.25,-.5,.6,.4,.001,.8,1.001,3.14159,.12,.3,-.005,4]


with open (filename, 'w',newline='\n') as saved_colors:
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
		if(iterations > 499):
			iterations = 354
		string_written = f'{x},{palette_dict[iterations][0]},{palette_dict[iterations][1]},{palette_dict[iterations][2]}'
		saved_colors.write(string_written)
		print(string_written)
			

