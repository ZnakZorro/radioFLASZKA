import RPi.GPIO as GPIO
import threading
from time import sleep

Enc_A = 11
Enc_B = 12
Enc_C = 13

Rotary_counter = 0
Current_A = 1
Current_B = 1
Current_C = 0

LockRotary = threading.Lock()
	

def init():
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Enc_A, GPIO.IN) 				
	GPIO.setup(Enc_B, GPIO.IN)
	GPIO.setup(Enc_C, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   
	GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotary_interrupt)
	GPIO.add_event_detect(Enc_B, GPIO.RISING, callback=rotary_interrupt)
	#GPIO.add_event_detect(Enc_C, GPIO.FALLING, callback=rotary_resetF)
	GPIO.add_event_detect(Enc_C, GPIO.RISING, callback=rotary_resetR)
#GPIO.FALLING  #GPIO.RISING   #GPIO.BOTH   
	return


def rotary_resetF(C):
	global licznik
	print('klik Fall')
	#licznik=0

def rotary_resetR(C):
	global licznik
	print('klik Rising button')
	print(licznik)
	licznik=0
	print(licznik)
	return

def rotary_interrupt(A_or_B):
	global Rotary_counter, Current_A, Current_B, LockRotary
	Switch_A = GPIO.input(Enc_A)
	Switch_B = GPIO.input(Enc_B)
	#print(Switch_A,Switch_B)
	if Current_A == Switch_A and Current_B == Switch_B:
		return
	Current_A = Switch_A
	Current_B = Switch_B

	if (Switch_A and Switch_B):
		LockRotary.acquire()
		if A_or_B == Enc_B:
			Rotary_counter -= 1
		else:
			Rotary_counter += 1
		LockRotary.release()
	return


def main():
	global Rotary_counter, LockRotary
	global licznik
	licznik=0
	Volume = 0
	NewCounter = 0
	init()	
	while True :
		sleep(0.1)
		LockRotary.acquire()
		NewCounter = Rotary_counter
		licznik+=NewCounter*10
		Rotary_counter = 0
		LockRotary.release()					
		if (NewCounter !=0):
			Volume = Volume + NewCounter*abs(NewCounter)
			if Volume < 0:
				Volume = 0
			if Volume > 100:
				Volume = 100
			print(NewCounter, Volume,licznik)

main()
