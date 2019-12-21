from selenium import webdriver
import time

SCROLL_PAUSE_TIME = 1.0

browser = webdriver.Chrome()

# todo, change username and password before running
username = ''
password = ''

browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(password)
browser.find_element_by_class_name('login__form_action_container ').click()
time.sleep(50)
browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections")

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

cards = browser.find_elements_by_class_name('mn-connection-card__link')

txt = open('connections.txt', 'w')
for card in cards:
    href = card.get_attribute('href')
    txt.write(href + '\n')

txt.close()
browser.quit()
