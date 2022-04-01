# importing webdriver from selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

print("Selenium Features:")
print("1. For Selecting from dropdown demo, press 1.")
print("2. For Writing dynamic XPath for lists demo, press 2.")
print("3. For Iterating lists demo, press 3.")
print("4. For invoking JavaScript demo, press 4.")

num = int(input("Enter command number: "))

if num == 1:

    url = "https://demoqa.com/select-menu"

    # Here Chrome will be used
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Opening the website
    driver.get(url)
    print("Opened website")
    sleep(1)

    # Getting current URL source code
    dropdown_box = driver.find_element_by_xpath("//select[@id='oldSelectMenu']/option[text()='Green']")
    dropdown_select = dropdown_box.click()

    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")

elif num == 2:
    url = "https://www.amazon.in/"
    
    #search = input("Enter item to be searched (Eg. Shoes,etc): ") # Shoes
    #filters = input("Enter filter brand (Eg. Adidas, Puma, Nike, BATA,etc): ") # Adidas, Puma, Nike, BATA
    search = "Shoes"
    filters = "Adidas"

    # Here Chrome will be used
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Opening the website
    driver.get(url)
    print("Opened website")
    sleep(1)
    
    search_box = driver.find_element_by_id('twotabsearchtextbox')
    search_box.send_keys(search)
    print ("Item entered")
    sleep(1)
    
    click_box = driver.find_element_by_id('nav-search-submit-button')
    click_box.click()
    print ("Button Clicked")
    sleep(1)
    
    filter_box = driver.find_element(By.XPATH, "//li[@id='p_89/Adidas']/span/a/div/label/i")
    filter_box.click()
    
    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")
    
# amazon search
# button click
# apply filter
        
elif num == 3:
    url = "https://demoqa.com/select-menu"
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    # Opening the website
    driver.get(url)
    print("Opened website")
    sleep(1)
    
    PlajePariuri = driver.find_elements_by_xpath("//*[@id='oldSelectMenu']")
    
    print()
    print("The List has the following elements:")
    for items in PlajePariuri:
        print (items.text)
        
elif num == 4:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get("https://google.com")
    
    js = '''
    var name = prompt("This is invoked Javascript. What's your name:")
    alert("Hey " + name)
    '''
    driver.execute_script(js)
    
    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")
else:
    print("Invalid Command number")