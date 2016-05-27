from random import randint
def game():
	trials=input("Enter the number of trails you want in the game: ")
	x=['rock','paper','sci']
	win=0
	lost=0
	for i in range(trials):
		user_input=raw_input("Rock, Paper or Sci: ").lower()
		user_input=validate_input(user_input)
		#print user_output
		comp_output=randint(0,2)
		comp_output=x[comp_output]
		print "Computer puts a "+comp_output
		result=compare(user_input,comp_output)
		if result=='w':
			win+=1
		elif result=='l':
			lost+=1
	if win>lost:
		print "You win"
	elif win==lost:
		print "Tie"
	else:
		print "You lost, better luck next time."
		
def validate_input(user_input):
	while user_input!='rock' and user_input!='paper' and user_input!='sci' :
		user_input=raw_input("Enter a valid input: ").lower()
		if user_input!='rock':
			print user_input
	return user_input

def play_again():
	answer=raw_input("Wanna play again? [Y/n]: ").lower()
	if answer=='yes' or answer=='y':
		game()
	elif answer=='no' or answer=='n':
		return
	else:
		play_again()
def compare(x,y):
	if (x=='rock' and y=='sci') or (x=='sci' and y=='paper') or (x=='paper' and y=='rock'):
		return 'w'
	elif x==y:
		return 't'
	else: 
		return 'l'
	
game()
play_again()
