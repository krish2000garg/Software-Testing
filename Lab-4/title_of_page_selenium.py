# importing webdriver from selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = input("Enter the URL: ") # https://stackoverflow.com/

# Here Chrome will be used
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of website
# url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print()
print("The title of the mentioned URL is:",get_title)
