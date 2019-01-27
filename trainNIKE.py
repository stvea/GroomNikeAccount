# -*- coding: utf-8 -*-
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def getAccounts():
	accounts = []
	file = open("setting.txt",'r')
	line = file.readline()
	line = line[:-1]
	delay_time = float(line.split(':')[1])
	while line:
		line = file.readline()
		line = line[:-1]
		if line != '':
			accounts.append(line.split(' '))
	print 'console>Get '+str(len(accounts))+' accounts'
	return delay_time,accounts


def printRights():
	print "                                        ,----,                                   "
	print "                                     ,/   .`|                                    "
	print "                      .--.--.      ,`   .'  :              ,---,.   ,---,        "
	print "  ,---,              /  /    '.  ;    ;     /     ,---.  ,'  .' |  '  .' \       "
	print ",---.'|             |  :  /`. /.'___,/    ,'     /__./|,---.'   | /  ;    '.     "
	print "|   | :             ;  |  |--` |    :     | ,---.;  ; ||   |   .':  :       \    "
	print ":   : :         .--,|  :  ;_   ;    |.';  ;/___/ \  | |:   :  |-,:  |   /\   \   "
	print ":     |,-.    /_ ./| \  \    `.`----'  |  |\   ;  \ ' |:   |  ;/||  :  ' ;.   :  "
	print "|   : '  | , ' , ' :  `----.   \   '   :  ; \   \  \: ||   :   .'|  |  ;/  \   \ "
	print "|   |  / :/___/ \: |  __ \  \  |   |   |  '  ;   \  ' .|   |  |-,'  :  | \  \ ,' "
	print "'   : |: | .  \  ' | /  /`--'  /   '   :  |   \   \   ''   :  ;/||  |  '  '--'   "
	print "|   | '/ :  \  ;   :'--'.     /    ;   |.'     \   `  ;|   |    \|  :  :         "
	print "|   :    |   \  \  ;  `--'---'     '---'        :   \ ||   :   .'|  | ,'         "
	print "/    \  /     :  \  \                            '---'' |   | ,'  `--''           "
	print "`-'----'       \  ' ;                                  `----'                    "
	print "                `--`                                                  "
	print "#################################################################################"
	print ""
	print "Please fill in your account info and browsing time for each item in setting.txt"    
	print "More in STVEA.cn"    
	print ""
	print "#################################################################################"
# print "please input username:"
# username = raw_input()
# print "please input password:"
# password = raw_input()

printRights()
delay_time,accounts = getAccounts()

for accounts_num in range(len(accounts)):

	username = accounts[accounts_num][0]
	password = accounts[accounts_num][1]
	isEmail = not username.isdigit()

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get("https://store.nike.com/cn/zh_cn/pw/mens-shoes/7puZoi3")

	login_href = driver.find_element_by_css_selector("[class='js-rootItem js-navItem']")
	login_href.click()

	if isEmail:
		print "console>A new account username:"+username+" using Email"
		driver.find_element_by_link_text('使用电子邮件登录。').click()
		login_username = "emailAddress"
	else:
		print "console>A new account username:"+username+" using Mobile"
		login_username = "verifyMobileNumber"

	driver.find_element_by_name(login_username).send_keys(username)
	driver.find_element_by_name("password").send_keys(password)
	driver.find_element_by_css_selector("[value='登录']").click()

	time.sleep(10)

	new_shoes = driver.find_elements_by_css_selector("[class='grid-item-image-wrapper sprite-sheet sprite-index-0']")
	random.shuffle(new_shoes)

	for i in range(len(new_shoes)):
		href = new_shoes[i].find_element_by_tag_name('a').get_attribute("href")
		js='window.open("'+href+'");'
		driver.execute_script(js)
		windows = driver.window_handles
		driver.switch_to.window(windows[1])
		print username+">Browse shoes:"+driver.title.replace(u'\xa0', u'')
		time.sleep(delay_time)
		driver.close()
		driver.switch_to.window(windows[0])

	driver.quite()