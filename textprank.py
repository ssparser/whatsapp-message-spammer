from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def msgs():
    f=open('shreak.rtf','r')
    for line in f:
        for words in line.split():

             msg_box.send_keys(words)
             button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
             button.click()



driver = webdriver.Chrome(ChromeDriverManager().install()) # diver
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for i in range(count):
    msg_box.send_keys(msg())
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    button.click()

#msgs()

print('ok')




