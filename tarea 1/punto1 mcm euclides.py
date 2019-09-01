import sys
import time

# https://www.iteramos.com/pregunta/81246/el-tiempo-de-complejidad-del-algoritmo-de-euclides
# The most complexity cases for mcm is calculation of fibonacci numbers
# https://catonmat.net/tools/generate-fibonacci-numbers
# The profiling does with 20 to 40 fibonacci

"""
# http://aprendeenlinea.udea.edu.co/boa/contenidos.php/8b077438024e1bddfbc83706da8049f2/138/1/contenido/contenido/alg_euclides.html
# Euclides
"""
"""
# Euclides algorithm 
"""
def mcd_euclides(divider, dividend):
	while True: 				# Max of iterations is number of
								# divisions where complexity is O(log_dividend(divider))
								# n is 4,4 * 10**-9 percentaje from
								# dividier + dividend
		# get mod x/y, next cases is y/modR_1, modR_1/modR_2 ... 
		# modR_n/modR_n+1
		modR=divider%dividend	# O(1)
		if(modR==0):			# O(1)
			return dividend		# O(1)
		divider=dividend		# O(1)
		dividend=modR			# O(1)
"""
# https://thales.cica.es/rd/Recursos/rd98/Matematicas/07/mcdmcm.html
# a*b = M.C.D.(a,b)*M.C.M.(a,b)
# a*b = M.C.M.(a,b)
# M.C.M.(a,b)=(a*b)/M.C.D.(a,b)
# cases of algorithm is, if maximun of iterations for hard way is x+y 
# iterations then:
# 2*x <= y
# 2*y <= x
# 2*x > y but x < y
# 2*y > x but y < x
# x == y
# whit the before rules the max of iterations for each 2 divisions is 
# reduced 25%, if thius is True must be satisfy 1.25^S <= A+B
# the complexity is:
# (5/4)^S <= A+B 
# S <= lg[5/4](A+B) 
# S is O(lg[5/4](A+B)) 
# S is O(lg(A+B)) 
# S is O(lg(A*B)) //because A*B asymptotically greater than A+B 
# S is O(lg(A)+lg(B)) 
# //Input size N is lg(A) + lg(B) 
# S is O(N)

Fuente: https://www.iteramos.com/pregunta/81246/el-tiempo-de-complejidad-del-algoritmo-de-euclides
# https://www.iteramos.com/pregunta/81246/el-tiempo-de-complejidad-del-algoritmo-de-euclides
"""
def mcm_with_mcd(x,y,mcd):	
	return (x*y)/mcd		# O(1)


if __name__ == "__main__":
	# Instance variable for file control
	fileProfiling=open("mcm euclides profile2.csv", "a", encoding="utf-8")

	# Get start time to get lapse time execution
	start = time.time()

	# start to get python memory allocations
	#tracemalloc.start()

	mcdValue=mcd_euclides(int(sys.argv[1]), int(sys.argv[2]))
	mcm_with_mcd(int(sys.argv[1]), int(sys.argv[2]),mcdValue)

	# Get end time to get lapsed
	end = time.time()

	# Write in file the result of time and memory profiling
	# fileProfiling.write("{},{},{}\n".format(len(array), tracemalloc.get_traced_memory()[1], end-start))
	fileProfiling.write("{},{}\n".format(str(sys.argv[1])+"."+str(sys.argv[2]), end-start))
	fileProfiling.close()

	# stop get python memory allocations
	#tracemalloc.stop()

	
	
	