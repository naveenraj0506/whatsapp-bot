from selenium import webdriver
import  time
import scrappy
driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com')
input('Press anything.')
sent = ""
flag = True
def send_msg(mymsg):
    global sent
    global flag
    time.sleep(2)
    msg = driver.find_element_by_class_name('_1Plpp')
    msg.send_keys(mymsg)
    time.sleep(2)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    time.sleep(2)
    sent = mymsg
    flag = False

while True:
    time.sleep(2)
    msgelements = driver.find_elements_by_class_name('_3zb-j')
    lastelement = msgelements[len(msgelements) - 1]
    amsg = lastelement.text
    if amsg != sent:
        flag = True

    if flag == True:
        output = scrappy.ai_reply(amsg)
        send_msg(output)















