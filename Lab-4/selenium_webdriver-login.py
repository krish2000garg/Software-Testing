#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#
#print('Enter the gmailid and password')
#gmailId, passWord = map(str, input().split())
#try:
#	driver = webdriver.Chrome(ChromeDriverManager().install())
#	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
#	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
#	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
#	driver.implicitly_wait(15)
#
#	loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
#	loginBox.send_keys(gmailId)
#
#	nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
#	nextButton[0].click()
#
#	passWordBox = driver.find_element_by_xpath(
#		'//*[@id ="password"]/div[1]/div / div[1]/input')
#	passWordBox.send_keys(passWord)
#
#	nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
#	nextButton[0].click()
#
#	print('Login Successful...!!')
#except:
#	print('Login Failed')

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#
#print('Enter the gmailid and password')
#gmailId, passWord = map(str, input().split())
#try:
#    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#    driver.get(r'https://www.facebook.com/')
#    driver.implicitly_wait(15)
#    
#    loginBox = driver.find_element_by_xpath('//*[@id ="email"]')
#    loginBox.send_keys(gmailId)
#    
##    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
##    nextButton[0].click()
#    
#    passWordBox = driver.find_element_by_xpath('//*[@id ="pass"]')
#    
#    passWordBox.send_keys(passWord)
#    
#    nextButton = driver.find_elements_by_xpath('//*[@id ="loginbutton"]')
#    print(nextButton)
#    nextButton[0].click()
#    
#    print('Login Successful...!!')
#except Exception as e:
#	print('Login Failed:', e)


from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

usr=input('Enter Email Id:')
pwd=input('Enter Password:')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")

#login_box = driver.find_element_by_id('u_0_d_/m')
#login_box = driver.findElement(By.name("login"));
login_box = driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")
login_box.click()

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
