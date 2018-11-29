"""
functions to read the a CSV file
and put it into a dictionary
"""
import csv

def read_palette_from_file(palette_filename):
	palette = dict()

	with open(palette_filename) as palette_csv:
		palette_reader = csv.reader(palette_csv)
		for color in palette_reader:
			# color0 = color[0]
			# color1 = color[1]
			# color2 = color[2]
			# color3 = color[3]
			#print(color0,color1,color2,color3)
			palette[int(color[0])] = (int(color[1]),int(color[2]),int(color[3]))
	return(palette)

