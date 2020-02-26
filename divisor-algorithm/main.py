def check_prime(num, prime,primesquare, a): 
	for i in range(2,num + 1): 
		prime[i] = True
	for i in range((num * num + 1)+1): 
		primesquare[i] = False

	prime[1] = False

	pnum = 2
	while(pnum * pnum <= num): 
		if (prime[pnum] == True): 
			i = pnum * 2
			while(i <= num): 
				prime[i] = False
				i += pnum 
		pnum+=1
	
	f = 0
	for pnum in range(2,num+1): 
		if (prime[pnum]==True): 
			a[f] = pnum 
			primesquare[pnum * pnum] = True
			f+=1

def main(num): 
	if (num == 1): 
		return 1

	prime = [False]*(num + 2) 
	primesquare = [False]*(num * num + 2) 

	a = [0]*num 

	check_prime(num, prime, primesquare, a) 

	divisors = 1

	i=0
	while(1): 
		if(a[i] * a[i] * a[i] > num): 
			break
 
		count = 1  
		while (num % a[i] == 0):
			num = num / a[i] 
			count = count + 1

		divisors = divisors * count 
		i+=1
	
	num = int(num) 

	if (prime[num] == True): 
		divisors = divisors * 2

	elif (primesquare[num] == True): 
		divisors = divisors * 3
 
	elif (num != 1): 
		divisors = divisors * 4

	return divisors


again = True
while again is True:
    try:
        number = int(input("[?] Enter any number: ")) 
    except ValueError:
        print("[-] Please input only integer value!")
        exit()
    
    total = main(number)
    print(f"Total numbers of divisors for {number} are {total}")
    x = input("\n[?] Do you want to try again? [y/n] ")
    print()
    if x.lower() == "y":
        again = True
    else:
        again = False