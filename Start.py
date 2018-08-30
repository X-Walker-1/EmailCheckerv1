import requests
import json
from os import path
import os

if __name__ == '__main__':
	EmailType = str(raw_input("1 @outlook.com/2 @hotmail.com: "))
	EmailsList = str(raw_input("Emails list file: "))
	if os.path.isfile(EmailsList) == True:
		print "File exist"
	else:
		print "File does not exist"
		exit()
	if EmailType == "1" or EmailType == "@outlook.com" or EmailType == "outlook.com":
		EmailType = "1"
	elif EmailType == "2" or EmailType == "@hotmail.com" or EmailType == "hotmail.com":
		EmailType = "2"
	else:
		print "Try again"
		exit()
	os.system('cls' if os.name=='nt' else 'clear')
	cookie = {'amsc': 'aQScn9xQEYSK/b6D+KxdWl3/Tl3YZtIxlVgNooLvFkpOqu0Lm88HYo4f2ChITM8hltSpchOcE2a0RzAWOGrDcjsmxmthZZR6Zg2JKNA/IxbqR9ga5P2GhUGW95G2OpoWYlKMymu9a+IJyjsVmZLW2bgU8/bXo3rdJiyiuMUw1oAv7S95FzWwYjshb+aN/0dlZM+9QFj4+mlDxEtMX4dlMlffbOwI+9xrH616+mniIDj2vT1vICxBR5ZB+c41wYzZ:2:3c'}
	fp = open(EmailsList, 'r')
	line = fp.readline()
	while line:
		line = line.split("@")[0].strip().replace(" ","").replace("+","").replace("/","").replace("\\","")
		if EmailType == "1":
			line = line + "@outlook.com"
			data = {"signInName":line,"uaid":"d12e2c00f5c5430cbb22518966082efa","includeSuggestions":True,"uiflvr":1001,"scid":100118,"hpgid":"Signup_MemberNamePage_Client"}
			headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json', 'Accept-Language': 'en-GB,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'canary': 'HzMHYWr5eU5K3z4GzyG82aj96/GQjOQhpz/N/P5lvLjrFSKoh58k56USCG2wQJ1Hqcjt+r/1hzSj8rsVDrqSfY+/vN2PaZrPnwYVEx58mzuthtz2RS1z7bhlQmynddVo6nNLeCQoj+yHtf/crWw1DHXXyfhM55csWy4YVtqfrMkAcmKPPg2LZWiNAlnRQCQ3OBe3zCuMfhENqwfFp+CYLSrqt1sOktlt5x+z87O7UuWPniWMflRg0QGiX2aAMjgh:2:3c', 'X-Requested-With': 'XMLHttpRequest', 'Content-Length': str(len(json.dumps(data))), 'Connection': 'close'}
		elif EmailType == "2":
			line = line + "@hotmail.com"
			data = {"signInName":line,"uaid":"d12e2c00f5c5430cbb22518966082efa","includeSuggestions":True,"uiflvr":1001,"scid":100118,"hpgid":"Signup_MemberNamePage_Client"}
			headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json', 'Accept-Language': 'en-GB,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'canary': 'HzMHYWr5eU5K3z4GzyG82aj96/GQjOQhpz/N/P5lvLjrFSKoh58k56USCG2wQJ1Hqcjt+r/1hzSj8rsVDrqSfY+/vN2PaZrPnwYVEx58mzuthtz2RS1z7bhlQmynddVo6nNLeCQoj+yHtf/crWw1DHXXyfhM55csWy4YVtqfrMkAcmKPPg2LZWiNAlnRQCQ3OBe3zCuMfhENqwfFp+CYLSrqt1sOktlt5x+z87O7UuWPniWMflRg0QGiX2aAMjgh:2:3c', 'X-Requested-With': 'XMLHttpRequest', 'Content-Length': str(len(json.dumps(data))), 'Connection': 'close'}
		PREmail = requests.post("https://signup.live.com/API/CheckAvailableSigninNames",data=json.dumps(data), headers=headers, cookies=cookie)
		PREmailJson = PREmail.json()
		if str(PREmailJson['isAvailable']) == "False":
			print line + "|" + "Not found"
		elif str(PREmailJson['isAvailable']) == "True":
			print line + "|" + "Found"
		else:
			print "Somthing is wrong"
		line = fp.readline()