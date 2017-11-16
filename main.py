import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import config


number_of_times = 100
message = "SPAM"



driver = None
options = Options()
options.add_argument(config.driver_argument)  # used for preserving account information so you can stay logged in


def wait(web_opening_time=0.1):  # hardcoded waiting intervals, currently not looking for document.ready
    time.sleep(web_opening_time)


def web_driver_load():
    global driver
    driver = webdriver.Chrome(config.driver_location, chrome_options=options)


def web_driver_quit():
    driver.quit()


def messenger_login():
    driver.get('https://web.whatsapp.com/')
    wait(5)

def send_message(iter, msg, obj) :

    obj.send_keys("#{}:{}".format(iter, msg))
    obj.send_keys(Keys.RETURN)

if __name__ == '__main__':
    web_driver_load()
    messenger_login()
    wait()
    find_person = driver.find_element_by_xpath("//span[@title = '{}']".format(config.group_chat))
    find_person.click()
    web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
    for i in range(number_of_times):

        send_message(str(i+1), message, web_obj)
    print("\nProcess completed successfully")

    wait()

