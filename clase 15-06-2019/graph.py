import sys
import os


import pandas as pd
import numpy as np
import pylab

# Latex languague in python
# from sympy import S, symbols
import sympy as sym

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


if __name__ == "__main__":
	if(".csv" in sys.argv[1]):
		data = pd.read_csv(sys.argv[1])

	# Replace All space in column headers
	data.rename(columns=lambda name: name.replace(" ", "_"), inplace=True)

	# get column headers such as [keyX1, keyX2, keyX3, ..., keyY]
	keyList=data.columns.values

	print("Tabla de datos leido\n{}\n".format(data))

	fig=plt.figure(1)
	fig.suptitle("Grafico {}".format(1), fontsize=16)

	x=data[keyList[0]]
	y=data[keyList[1]]

	# Set scatter points
	plt.scatter(x,y)

	# calc the trendline
	z = np.polyfit(x, y, 2)
	p = np.poly1d(z)
	pylab.plot(x,p(x),"r--")
	# print("y={0:.6f}x+({1:.6f})".format(z[0],z[1]))
	# print(z[0], z[1])
	
	
	# normal way
	for enum, v in enumerate(z[::-1]):
		if((v>0 and enum==0) or v<0):
			print("{:6.2f}*x^{}".format(v,enum), end='')
		elif(v>0):
			print("+{:6.2f}*x^{}".format(v,enum), end='')

		if(enum==len(z)-1):
			print("")

	# sympy way
	# x = sym.symbols("x")
	# poly = sum(sym.S("{:6.2f}".format(v))*x**i for i, v in enumerate(z[::-1]))
	# eq_latex = sym.printing.latex(poly)
	# print(eq_latex)


	plt.show()

