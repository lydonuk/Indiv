#Login System (v1.0)
import os
import stdiomask
import platform

title = 'Login System'
OS = platform.system()
UN = 'root'
PW = 'root'
x = 3

while x > 0:

	username = input('Username: ')
	password = input('Password: ')
	x = x - 1
	
	if username != UN or password != PW:
		print('Login incorrect! Attempts left: ' + str(x))
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