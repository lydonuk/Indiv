#Key System (v1.0)
import os
import stdiomask
import platform

OS = platform.system()
K = 'root' #default key
x = 3

while x > 0:
	key = stdiomask.getpass('Key: ')
	x = x - 1
	
	if key != K:
		print('Key incorrect! Attempts left: ' + str(x))
		
		if x <= 0:
			input()
			quit()
			
		else:
			input('Press enter to retry...')
		
			if OS == 'Windows':
				os.system('cls')
			
			elif OS == 'Linux' or 'Darwin':
				os.system('clear')
				
	else:
			if OS == 'Windows':
				os.system('cls')
			
			elif OS == 'Linux' or 'Darwin':
				os.system('clear')
			
				break
				
#Add code
