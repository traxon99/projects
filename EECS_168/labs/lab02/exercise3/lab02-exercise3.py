'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/16/2022
Lab: lab02
Last modified: 09/16/2022
Purpose: Restaurant that sells items and prints final price
'''
print('==========================')
print('WELCOME TO THE RESTAURANT')
print('==========================')
print('')
print('')

c_pp = 2.5
g_cp = 5.55
pp = 3.00
tax = 0.08

#cold pasta
c_p = input('Do you want Cold Pasta? (y/n): ')
if c_p.upper() == 'Y':
	c_p_ct =  int(input('How many?: '))
	if c_p_ct < 0:
		c_p_ct = 0
else:
        c_p_ct = 0

#grilled cheese
g_c = input('Do you want Grilled Cheese? (y/n): ')
if g_c.upper() == 'Y':
	g_c_ct = int(input('How many?: '))
	if g_c_ct < 0:
		g_c_ct = 0
else:
        g_c_ct = 0

#pie
p = input('Do you want Pie? (y/n): ')
if p.upper() == 'Y':
	p_ct = int(input('How many?: '))
	if p_ct < 0:
		p_ct = 0
else:
        p_ct = 0
#age - age checker
age = int(input('How old are you?: '))
a5discount = False
a55discount = False
if age >= 55:
	a55discount = True
elif age <= 5:
	a5discount = True
else:
	a55discount = False
	a5discount = False

#subtotal and tax calculation
if a55discount == False and a5discount == False:
	print(c_p_ct,f'Cold Pasta @ {c_pp:0.2f} ==>',(c_p_ct * c_pp))
	print(g_c_ct,f'Grilled Cheese @ {g_cp:0.2f} ==>',(g_c_ct * g_cp))
	print(p_ct,f'Pie @ {pp:0.2f} ==>',(p_ct * pp))
	sub = (c_p_ct * c_pp) + (g_c_ct * g_cp) + (p_ct * pp)
	print(f'Subtotal: ${sub:0.2f}')
	print(f'Tax: ${(sub * tax):0.2f}')
	print('Discount: 0.00')
	print('==========================')
	print(f'Total: {sub + (sub * tax):0.2f}')
	print('Please come again!')

elif a55discount == True:
	print(c_p_ct,f'Cold Pasta @ {c_pp:0.2f} ==>',(c_p_ct * c_pp))
	print(g_c_ct,f'Grilled Cheese @ {g_cp:0.2f} ==>',(g_c_ct * g_cp))
	print(p_ct,f'Pie @ {pp:0.2f} ==>',(p_ct * pp))
	sub = (c_p_ct * c_pp) + (g_c_ct * g_cp) + (p_ct * pp)
	print(f'Subtotal: ${sub:0.2f}')
	print(f'Tax: ${(sub * tax):0.2f}')
	print(f'Discount: {((sub + (sub * tax)) * 0.55):0.2f}')
	discount = ((sub + (sub * tax)) * 0.55)
	print('==========================')
	print(f'Total: {((sub + (sub * tax))-discount):0.2f}')
	print('Please come again!')

elif a5discount == True:
        pp = 0
        print(c_p_ct,f'Cold Pasta @ {c_pp:0.2f} ==>',f'{(c_p_ct * c_pp):0.2f}')
        print(g_c_ct,f'Grilled Cheese @ {g_cp:0.2f} ==>',f'{(g_c_ct * g_cp):0.2f}')
        print(p_ct,f'Pie @ {pp:0.2f} ==>',f'{(p_ct * pp):0.2f}')
        sub = (c_p_ct * c_pp) + (g_c_ct * g_cp) + (p_ct * pp)
        print(f'Subtotal: ${sub:0.2f}')
        print(f'Tax: ${(sub * tax):0.2f}')
        print('Discount: 0.00')
        print('==========================')
        print(f'Total: {sub + (sub * tax):0.2f}')
        print('Please come again!')
        

