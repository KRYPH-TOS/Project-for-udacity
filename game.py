import random
import time 
import os
import sys
drink1 = 'D1'
drink2 = 'D2'
drink3 = 'D3'
drinks = [drink1,drink2,drink3]



hammer = True
HP = 100
HP = max(HP, 0)
	
Gangmembers= 4
def intro():
	print("Hello, player")
	time.sleep(0.2)
	print("Enter your national ID here :")
	cmd = input("> ")
	time.sleep(0.2)
	print("I'm kidding!!")
	time.sleep(1)
	print("You are 3 years old...")
	time.sleep(1)
	print("You are dreaming of being a warior")
	time.sleep(1)
	print("But you can't be a one...")
	time.sleep(1)
	print("Thats right!")
	time.sleep(1)
	print("You are a child!")
	time.sleep(1)
	print("But you can when you are 18.")
	time.sleep(1)
	print("Enter 18!")
	time.sleep(1)
	cmd = input("> ")
	if cmd == "18" :
		print("Hooray!, You are 18")
	else:
		print("Nah, that's not 18")
	time.sleep(1)
def weapon_pick():	
	print("Now you are in Weapons shop.")
	time.sleep(1)
	print("You are ordered to choose a weapon.")
	time.sleep(1)
	print("1. a Sledgehammer")
	print("2. Suppressed M4 Carbine with Red Dot, Angled grip and Laser sight.")
	print("3. a banana")
	time.sleep(1)
	print("What weapon would you choose? Enter the number.") 
	while True:
		cmd = input("> ")
		if cmd == "1":
			print("That is the one you need, This is an adveture game.")
			break
		elif cmd == "2":
			print("Not today, We are not in Call Of Duty.")
		elif cmd == "3":
			print("It has much potassium, But, Not a smart choice, else if you were fighting Hypertension.")
		else:
			print("That is not a choice.")
def fight():
	print("Now, due to world peace and less of wars and fights...")
	time.sleep(1)
	print("You have three left enemies to purge: ")
	time.sleep(1)
	print("1. boredom")
	print("2. Street gangs")
	print("3. Sewer rats")
	while True:
		cmd = input("> ") 
		if cmd == "1":
			print("You are!, But not always the meant fight.")
		elif cmd == "2":
			print("Ok, at least you are doing a good thing to society.")
			break
		elif cmd == "3":
			print("Stinky, Choose again.")
		else:
			print("That is not a choice.")
	print("You are in gang zone now.")
	time.sleep(1)
	print("Now you are in a dangerous situation!")
	time.sleep(1)
	print("There are 4 gang members surrounding you!")
	time.sleep(5)
	os.system('clear')
	print(f"{HP}")
	print("Your health is 100, One of them is going to attack!")
	time.sleep(1)
	print("You have 5 choices, What should you do!")
	print("1. Run away 'Not recommended'.")
	print("2. Get any bottle on the ground and break it from it's base, so it can be sharp enough to stab.")
	print("3. Use your hammer.")
	print("4. Call for help.")
	print("5. Use your fighting skill to fight them ONE by ONE.")
	
	while True:
		cmd = input("> ")
		if cmd == "1":
			print("Quack!, Quack!")
			time.sleep(1)
			HP -= 80
			print(f"One of them has stabbed you, your HP = {HP}, you are critically injured.")
		elif cmd =="2":
			print("Give it a try...")
			time.sleep(1)
			HP -=20
			print (f"You cut your hand:HP = {HP}, You should accquire egyptian baltagy skill to be able to do this.")
		elif cmd == "3":
			if hammer == True:
				print("You have used your hammer.")
				hammer = False
				time.sleep(1)
				Gangmembers -=1
				print(f"Great!, You have squeezed 1 gang member,{Gangmembers} are remaining ")
			elif hammer == False:
				print("Your hammer is not effective right now, You can't use it.")		
		elif cmd == "4":
			print("You called for help.")
			time.sleep(1)
			print("No one heard you.")
		elif cmd == "5":
			print("Now you are unleashing your inner beast!")
			time.sleep(2)
			Gangmembers -=3
			print("You have kicked one in his.....brutally!")
			time.sleep(1)
			print("You have snapped your fingers in one's nose, Til he chocked to Death!")
			time.sleep(1)
			print("The last one ran away from fear.")
			time.sleep(1)
			
		else:
			print("That's not a choice.")
		if HP == 0:
			print("YOU LOSE !!!")
			if input("Play again ? -y/n").lower() == "y":
				os.execl(sys.executable, sys.executable, *sys.argv)
			
		if Gangmembers == 0:
			break
			print("Congrats!, You won your first fight!")
time.sleep(1)
def finale():
	print("Now you are in a bar.")
	time.sleep(1)
	print("You have asked the barman to serve you a drink.")
	time.sleep(1)
	print("But wait..")
	time.sleep(1)
	print("Here is the TWIST.")
	time.sleep(3)
	print("The barman obviously appeared to be the last gang member you let!")
	time.sleep(1)
	print("The bar is crowded with gang members surrounding you!")
	time.sleep(1)
	print("And you don't have energy to fight them all.")
	time.sleep(1)
	print("He promised to let you go in one condition: ")
	time.sleep(1)
	os.system('clear')
	print("He is serving 3 drinks, 2 are poisoned, 1 is not.")
	time.sleep(1)
	print("He will swap the 3 drinks, so you can't know where the safe one is.")
	time.sleep(1)
	print("You have chance of 33% to survive")
	time.sleep(1)
	print("Pick a one :")
	print("1. Drink 1")
	print("2. Drink 2")	
	print("3. Drink 3")	
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	random.shuffle(drinks)
	choice = [drinks]
	choose = random.choice(drinks)
	while True:
		cmd = input("> ")
		if cmd == '1':
			print("You Lose !!!")
			sys.exit()
		elif cmd == '2':
			print("You have chosen the not poisoned one, and also gained energy!")
			break
		elif cmd == '3':
			print("You Lose !!!")
			sys.exit()
		else:
			print("Wrong choice.")
	time.sleep(2)
	print("Now you have two choices :")
	time.sleep(2)
	print("1. Either you destroy the bar and everyone inside")
	time.sleep(2)
	print("2. Or you just forgive and leave.")
	while True:
		cmd = input("> ")
		if cmd == "1":
			print("Now you are unleashing your inner beast!")
			time.sleep(1)
			print("You have Erased the bar and everyone inside from the existence!")
			time.sleep(2)
			print("Now, you are officially a WARIOR!")
			print("Goodbye.")
			sys.exit()
		elif cmd == "2":
			print("You did a nice thing, But, your main objective is to fight gangs,")
			time.sleep(2)
			print("And which place is better than a bar filled with gangs to fight :).")
			time.sleep(2)
			print("You went inside, Again.")
			time.sleep(2)
			print("Now you are unleashing your inner beast!")
			time.sleep(1)
			print("You have Erased the bar and everyone inside from the existence!")
			time.sleep(2)
			print("Now, you are officially a WARIOR!")
			print("Goodbye.")
			sys.exit()
			
while True:
	intro()
	weapon_pick()
	fight()
	finale()
	break		
	














