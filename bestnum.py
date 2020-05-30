from decimal import Decimal

outcomes = [0]*1000
for x in range(1000):
	cookies =0
	positionsbuying = [[1110,200],[1110,260],[1110,310],[1110,370],[1110,430],[1110,490],[1110,550]] #positions of stuff to buy

	#clicker, farm, mine, factory, bank, temple, wizard tower, shipment, alchemy lab,portal
	buildings = [0]*len(positionsbuying)
	cookierate = [0.1,1,8,47,260,1400,7800,44000,260000,1600000,10000000]
	cps =0;
	prices = [15,100,1100,12000,130000,1400000,20000000,330000000,5100000000,75000000000,1000000000000]

	i=0 #index for loop in time
	p=0 #index for item in question

	while(i < 10000):
		cookies +=1 #add cookie from click
		cookies += cps #add current cps
		
		if((buildings[p] < x) & (cookies >=prices[p])):
			cookies -=prices[p] #buy item
			buildings[p] += 1 #add to buildings count
			prices[p] *= 1.15 #increase item price
			cps += cookierate[p] #increase cps
			if(buildings[p]==x): #if our max count is done, move on
				p+=1
		i+=1
		"""print("Time: {}".format(i))
		if(cookies < 10000): 
			print("Cookies: {}".format(cookies))
		else:
			print('Cookies: %.2E' % Decimal(cookies))
		print("CPS: {}".format(cps))
		print("Buildings: {}".format(buildings))
		print("Prices: {}".format(prices))
		print("Cookie Rate: {}".format(cookierate))
		print("################")"""
	print("Cookies @ x = {} : {} ".format(x,cookies))
	outcomes[x] = cookies
maxoutcome = max(outcomes)
print("Max cookies index: {}".format(outcomes.index(maxoutcome)))


