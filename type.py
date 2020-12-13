from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from prettytable import PrettyTable
import time
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    
    elif os.name == "nt":
        os.system("cls")
    
    else:
        try:
            os.system("clear")
        except:
            pass

def logo():
    
    clear()
    table = PrettyTable(["Option","Website"])
    table.add_row(["1.","Live Chat"])
    table.add_row(["2.","Typing Test"])
    table.add_row(["3.","TenFastFingers"])
    table.add_row(["9.","Exit"])
    print(table)


def main():
    while True:
        logo()
        cho = int(input("Select : "))
        if cho == 1:
            main_1()

        elif cho == 2:
            main_2()

        elif cho == 3:
            main_3()

        elif cho == 9:
            exit()

        else:
            print("Please select something on the board !")    
        
def main_1():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\walri\AppData\Local\Google\Chrome\User Data\Default")
    browser = webdriver.Chrome(options=options)
    url = r"https://www.livechat.com/typing-speed-test/#/"
    browser.get(url=url)
    word = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]')
    keyboard = browser.find_element_by_xpath('//*[@id="test-input"]')
    while True:
        try:
            time.sleep(0.1)
            keyboard.send_keys(word.text)
            keyboard.send_keys(Keys.SPACE)
        except Exception as error:
            print("Hata !\n{}".format(error))
            browser.close()
            exit()

def main_2():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\walri\AppData\Local\Google\Chrome\User Data\Default")
    browser = webdriver.Chrome(options=options)
    url = r"https://www.typingtest.com/test.html?minutes=1&textfile=difficultText.txt&mode=sent&result_url=%2Fresult.html&bt=0"
    browser.get(url=url)
    input("Click me...")

    words = browser.find_element_by_xpath('//*[@id="test-container"]/div[2]')
    keyboard = browser.find_element_by_xpath('//*[@id="test-edit-area"]')
    try:
        for word in words.text:
            keyboard.send_keys(word)
    except Exception as error:
        print("Hata !\n{}".format(error))
        browser.close()
        exit()

def main_3():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\walri\AppData\Local\Google\Chrome\User Data\Default")
    browser = webdriver.Chrome(options=options)
    url = "https://10fastfingers.com/advanced-typing-test/turkish"
    browser.get(url)
    a = input("Başla ...")
    time.sleep(5)
    try:    
        while True:
        
            word = browser.find_element_by_class_name('highlight')
            yazi = browser.find_element_by_xpath("//*[@id='inputfield']")
            yazi.send_keys(word.text)
            yazi.send_keys(Keys.SPACE)

        
    except Exception as error:
        print("Hata !\n{}".format(error))
        browser.close()
        exit()


if __name__ == '__main__':
    main()
