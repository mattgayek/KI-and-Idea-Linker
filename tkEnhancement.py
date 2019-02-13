
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import  ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
import xlrd
from pymongo import MongoClient
#need dictionary of all TSI client logins then iterate through for loop setting username.send_keys and password.send_keys to dictionary values and keys put all others inside loop add descriptive errors if failured
def upvote_idea(idea_value):
	client = MongoClient("mongodb+srv://admin:GoHeels97@watchdogcluster-b81ng.mongodb.net/test?retryWrites=true")
	db =client.tsi
	col =client.tsi.tsilogins
	driver = webdriver.Firefox(executable_path=r'C:\Users\MGayek\Downloads\geckodriver-v0.23.0-win64\geckodriver')
	driver.get("https://www.community.nextgen.com/SuccessCommunityLogin?startURL=%2Fapex%2FSplashPage")

	logins = {}

#should I just make this a mongodb collection?
	user_rows = db.tsilogins.find({}, { '_id': 0})
	
        #complete_val = 0
 		#error is in here
	complete_val = 0
	val = 0
	for row in user_rows:
		#logins = {'mgayek@tsihealthcare.com.nextgen': 'Skand1a1@',}
		for key, value, in row.items():
			login_key = value
			login_value = "GoHeels97"
		try:
			username = driver.find_element_by_id("loginPage:loginForm:username")
			password = driver.find_element_by_id("loginPage:loginForm:password")
		#add try catch in case there is an incorrect login 
			username.send_keys(login_key)
			password.send_keys(login_value)

			driver.find_element_by_name("loginPage:loginForm:loginButton").click()
			
			driver.implicitly_wait(10)

			#idea_text = ["Alert or message of failed Portal message"]
			
		#Will become a for loop to loop over every KI and make the variable the current KI
			idea = idea_value
			
			driver.find_element_by_class_name("brandPrimaryFgr").click()#switch to by title
			driver.implicitly_wait(6)
			search = driver.find_element_by_class_name("form-control")
			#search.send_keys(idea_text[j])
			search.send_keys(idea)
			search.submit()

			driver.implicitly_wait(5)
			#text = idea_text[j]
			text = idea
			driver.find_element_by_link_text(text).click()
			j = j + 1 
			driver.implicitly_wait(2)
			try:
				driver.implicitly_wait(3)
				driver.find_element_by_class_name("voteUp").click()
				driver.implicitly_wait(2)
				#should I find a way to see if it actually executed correctly?
			except NoSuchElementException:
				continue
		
			driver.find_element_by_link_text("Log Out").click()
			
			
		except NoSuchElementException:
			error_log = open("C:/Users/MGayek/error_log.txt", "a")
			error_log.write("Incorrect Username or Password: " + key + ' ' + value +"\n")
			error_log.close()
			driver.get("https://www.community.nextgen.com/SuccessCommunityLogin?startURL=%2Fapex%2FSplashPage")
			continue
		except ElementNotInteractableException: 
			error_log = open("C:/Users/MGayek/error_log.txt", "a")
			error_log.write("Account cannot attach itself to KIs: " + key + ' ' + value +"\n")
			error_log.close()
			driver.find_element_by_link_text("Log Out").click()
			continue
		
		## add in something for if the link text is not there need 1 more exception handler cant search for IDEAS corerctly 
		