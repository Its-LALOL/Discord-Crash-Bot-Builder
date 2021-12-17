import requests
from colorama import init, Fore; init()
import os
from time import sleep
import random

clear=lambda: os.system('cls && title Crash bot Builder By LALOL' if os.name == 'nt' else 'clear')

LALOL=Fore.RED +"""
██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
███████╗██║░░██║███████╗╚█████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
"""
if not os.path.isdir("Data"):
	while True:
		clear()
		language=input("[1] Русский\n[2] English\n\nPlease select a language: ")
		if language=="1":
			language="ru"
			break
		elif language=="2":
			language="en"
			break
		else:
			pass
	clear()
	os.mkdir("Data")
	with open("Data/language", 'w') as f:
		f.write(language)
with open("Data/language") as f:
	language=f.read()
def Menu():
	clear()
	print(LALOL)
	print(Fore.GREEN + "\nCrash bot Builder By LALOL")
	sleep(3)
	print(Fore.MAGENTA)
	clear()
	if language=="ru":
		Intro="""[1] Обычный Краш-бот
[2] Авто Краш-бот
[3] Анти-Лаван
""" + Fore.WHITE
	if language=="en":
		Intro="""[1] Common Crash-bot
[2] Auto Crash-bot
[3] Anti-Lavan
""" + Fore.WHITE
	print(Intro)
	if language=="ru":
		option=input("Выберите бота которого хотите создать: ")
	if language=="en":
		option=input("Select the bot you want to create: ")
	if option=="1":
		print(Fore.YELLOW)
		clear()
		if language=="ru":
			Intro="Введите сообщение которое будет отправлятся при спаме: "
		if language=="en":
			Intro="Enter the message to be sent in case of spam: "
		spammessage=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите название спам каналов: "
		if language=="en":
			Intro="Enter the name of the spam channels: "
		channelname=input(Intro)
		channelname=channelname.replace(" ", "-")
		clear()
		if language=="ru":
			Intro="Введите причину бана: "
		if language=="en":
			Intro="Enter the reason for the ban: "
		banreason=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите количество сообщений при спаме: "
		if language=="en":
			Intro="Enter the amount of spam messages: "
		intmessages=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите название сервера которое будет изменятся при краше: "
		if language=="en":
			Intro="Enter the name of the server that will change on crash: "
		guildname=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите название спам ролей: "
		if language=="en":
			Intro="Enter the name of the spam roles: "
		rolename=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите префикс: "
		if language=="en":
			Intro="Enter prefix: "
		botprefix=input(Intro)
		clear()
		if language=="ru":
			Intro="Введите токен бота: "
		if language=="en":
			Intro="Enter bot token: "
		token=input(Intro)
		clear()
		if language=="ru":
			Intro="Нажмите Enter чтобы начать создание бота"
		if language=="en":
			Intro="Press Enter to start creating the bot"
		input(Intro)
		script=requests.get('https://raw.githubusercontent.com/Its-LALOL/Discord-Crash-Bot-Builder/main/CrashBot/main').text
		script=script.replace("spammessage", spammessage)
		script=script.replace("intmessages", intmessages)
		script=script.replace("channelname", channelname)
		script=script.replace("banreason", banreason)
		script=script.replace("guildname", guildname)
		script=script.replace("rolename", rolename)
		script=script.replace("botprefix", botprefix)
		script=script.replace("token", token)
		number=random.randint(00000, 99999)
		os.mkdir(f"Crashbot_{number}")
		with open(f'Crashbot_{number}/main.py', 'w', encoding="utf-8") as f:
			f.write(script)
		if language=="ru":
			Intro=f"Бот был успешно создан по путю: Crashbot_{number}/main.py"
		if language=="en":
			Intro=f"The bot was successfully created along the path: Crashbot_{number}/main.py"
		clear()
		print(Fore.GREEN + Intro)
		sleep(10)
		Menu()
	elif option=="2" or option=="3":
		if language=="ru":
			print(Fore.RED + "Скоро...")
		if language=="en":
			print(Fore.RED + "Soon...")
		sleep(3)
		Menu()
	else:
		if language=="ru":
			print(Fore.RED + "Такой функции не существует!")
		if language=="en":
			print(Fore.RED + "There is no such function!")
		sleep(3)
		Menu()
Menu()
