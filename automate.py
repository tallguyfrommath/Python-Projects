import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
web = webdriver.Edge(EdgeChromiumDriverManager().install())
web.get('url')
time.sleep(7)


LastName = "Test"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = "Test"
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
RadioButtonPeriod.click()

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Thank you for attending"):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")