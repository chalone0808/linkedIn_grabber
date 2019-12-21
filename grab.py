from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, csv, getpass

SCROLL_PAUSE_TIME = 1.0

browser = webdriver.Chrome()

# todo, change username and password before running
username = ''
password = ''

browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(password)
browser.find_element_by_class_name('login__form_action_container ').click()

links = open('connections.txt').readlines()
detail_page = 'detail/contact-info/'

with open("connections.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=['Name', 'Occupation', 'Location', 'Website', 'Phone', 'Address', 'E-mail',
                                        'IM', 'Birthday', 'Date Connected'])
    writer.writeheader()

    for link in links:

        browser.get(link)

        # name
        try:
            name = browser.find_element_by_class_name('mr5').find_element_by_class_name(
                'pv-top-card-v3--list').find_element_by_class_name('break-words').text
        except NoSuchElementException:
            name = ''

        # occupation
        try:
            occupation = browser.find_element_by_class_name('mr5').find_element_by_class_name('mt1').text
        except NoSuchElementException:
            occupation = ''

        # location
        try:
            location = browser.find_element_by_class_name('mr5').find_element_by_xpath(
                '//*[@id="ember45"]/div[2]/div[2]/div[1]/ul[2]/li[1]').text
        except NoSuchElementException:
            location = ''

        # go to detail page
        browser.get(link + detail_page)
        # website
        try:
            website = browser.find_element_by_class_name('ci-websites').find_element_by_class_name(
                'pv-contact-info__contact-link').text
        except NoSuchElementException:
            website = ''

        # phone
        try:
            phone = browser.find_element_by_class_name('ci-phone').find_element_by_class_name(
                'pv-contact-info__ci-container').text
        except NoSuchElementException:
            phone = ''

        # address
        try:
            address = browser.find_element_by_class_name('ci-address').find_element_by_class_name(
                'pv-contact-info__contact-link').text
        except NoSuchElementException:
            address = ''

        # email
        try:
            email = browser.find_element_by_class_name('ci-email').find_element_by_class_name(
                'pv-contact-info__contact-link').text
        except NoSuchElementException:
            email = ''

        # im
        try:
            ims = browser.find_element_by_class_name('ci-ims').find_elements_by_class_name('t-14')
            im = ' '.join([x.text for x in ims])
        except NoSuchElementException:
            im = ''

        # birthday
        try:
            birthday = browser.find_element_by_class_name('ci-birthday').find_element_by_class_name(
                'pv-contact-info__contact-item').text
        except NoSuchElementException:
            birthday = ''

        # date connected
        try:
            date_connected = browser.find_element_by_class_name('ci-connected').find_element_by_class_name(
                'pv-contact-info__contact-item').text
        except NoSuchElementException:
            date_connected = ''

        writer.writerow(
            {'Name': name,
             'Occupation': occupation,
             'Location': location,
             'Website': website,
             'Phone': phone,
             'Address': address,
             'E-mail': email,
             'IM': im,
             'Birthday': birthday,
             'Date Connected': date_connected})

        time.sleep(0.2)

browser.quit()
