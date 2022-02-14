import datetime
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
name = "My Second Number"


# To get a new date and time stamp for every new message, I have converted message as a function.
def message():
    return "Hi.. I am a simple python script..I here to tell you the current  date and time.. Date :- " \
           + str(datetime.datetime.now().date()) + " Time :- " + str(datetime.datetime.now().time()) + "\n"


# Open the whatsapp website
driver.get("https://web.whatsapp.com/")

# Check for login and wait for login
a = input("Press enter after you login.")

# Search For Name
driver.find_element(by='xpath', value='//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(name)
time.sleep(3)
driver.find_element(by='xpath',
                    value='//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div[1]/span/span').click()

# Enter the message
driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') \
    .send_keys(message())

# send the message in repeat
if input("Type 'Y' to send 10 more message.") == "Y":
    for i in range(10):
        time.sleep(2)
        driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') \
            .send_keys(message())

# Logout WhatsApp from the device
driver.find_element(by='xpath',
                    value='//*[@id="side"]/header/div[2]/div/span/div[3]/div/span').click()
time.sleep(1)
driver.find_element(by='xpath',
                    value='//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]').click()

# Wait for sometime then close the browser
time.sleep(5)
driver.quit()

# Created in 14-02-2022
