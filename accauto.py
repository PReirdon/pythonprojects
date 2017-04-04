print('Howdy! , this program uses information from a companys variable costing income statments.')
print('This program can be used for two different products to find...')
print('Sales mix and contriution martion ratio.')
print('Weighted-average contribution margin ratio. ')
print('Break even point in dollars.')
print('Sales dollars at break even point for each products.')

#next will begin the part where users enter needed values
print('To start, please enter the coresponding values when promted')

#user will start entering values here for product A
asale = int(input("Please enter product A's sales here: "))
acontri = int(input("Please enter product A's contribution margin here: "))

#users will start entering values here for produt B
bsale = int(input("Please enter product B's sales here: "))
bcontri = int(input("Please enter product B's contribution margin here: "))

#the last needed value
fixedcost = int(input('Please enter the companys fixed cost here: '))

#values needed that this program will compute
totalsales = (asale + bsale)
print('The total sales is...')
print(totalsales)
totalcontri = (acontri + bcontri)
print('The total contribution margin is...')
print(totalcontri)

#calculating sales mix for product A and B
salesmixa = (asale / totalsales)
print("The sales mix for product A is...")
print(salesmixa)
salesmixb = (bsale / totalsales)
print("The sales mix for product B is...")
print(salesmixb)

#calculating contribution margin for product A and B
acontrir = (acontri / asale)
print("The contribution margin ratio for product A is...")
print(acontrir)
bcontrir = (bcontri / bsale)
print('The contribution margin ratio for product B is...')
print(bcontrir)

#calculating the wieghted average contribution margin ratio
wacontrir = (totalcontri / totalsales)
print("The wighted average contribution margin ratio is...")
print(wacontrir)

#calculating break even point in dollars
breakevp = (fixedcost / wacontrir)
print("The break even point in dollars is...")
print(breakevp)

#calculating sales dollars at break even point
sdbreakepa = (breakevp * salesmixa)
print("The sales dollar at break even point for product A is...")
print(sdbreakepa)
sdbreakepb = (breakevp * salesmixb)
print("The sales dollar at break even point for product B is...")
print(sdbreakepb)
