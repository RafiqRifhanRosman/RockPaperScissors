import random

rocpapsci_gen = ['rock', 'paper', 'scissors']

user_name = input('Please enter your name: ')

com_points = 0
user_points = 0

round = 0
decision = input ('Are you ready?>')
if decision == 'yes':
	while round != 3:
		rocpapsci_user = input('Please enter rock, paper or scissors: \n You: ')
		computer = (random.choice(rocpapsci_gen))
		print ('computer:' + computer + '\n')
		
		if rocpapsci_user == computer :
			round += 1
			continue
		
		elif rocpapsci_user == 'rock' :
			if computer == 'paper' :
				com_points += 1
			else :
				user_points += 1
				
		elif rocpapsci_user == 'paper':
			if computer == 'scissors':
				com_points += 1
			else:
				user_points += 1
				
		elif rocpapsci_user == 'scissors':
			if computer == 'rock':
				com_points += 1
			else :
				user_points += 1
		round += 1
		print ('You:' + str(user_points) + ' Computer:' + str(com_points))
		
				
if user_points > com_points: 
	print ('Congrats! You have beaten the computer!')
	print ('You:' + str(user_points) + ' Computer:' + str(com_points))
	
elif user_points < com_points:
	print ('You lose!')
	print ('You:' + str(user_points) + ' Computer:' + str(com_points))
	
else : 
	print ('Its a Draw! ')





