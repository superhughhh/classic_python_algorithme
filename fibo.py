#this algorithm calculates the sequence of Fibonacci numbers.
#0-1-1-3-5-8-13-21-34-55-89-144-...

def fibo(n): #n for number of loop turn 
	a,b = 0,1
	print(a)
	for i in range(1, n):
		c = a + b
		print(b)
		a = b
		b = c


number_of_loop_turn = int(input("How many number of the sequence of fibonacci dou you want ? "))
fibo(number_of_loop_turn)
				
