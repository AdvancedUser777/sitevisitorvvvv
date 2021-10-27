import selenium
import webdriver
from selenium 
from webdriver_manager.chrome import ChromeDriverManager
browser  = webdriver.Chrome(ChromeDriverManager().install())
# ======= Setting =============
# Your Facebook credentials
fb_name = "Your Facebook Email (or phone)"
fb_pass = "Your Facebook pass"
# =============================
# Open the Website
browser.get('https://www.instagram.com/')
# click on Log in with Facebook
browser.find_element_by_class_name('KPnG0').click();
# =============================
# Filling in the Facebook Credentials
browser.find_element_by_name("email").send_keys(fb_name)
browser.find_element_by_name("pass").send_keys(fb_pass)
# Click on the facebook log-in button
browser.find_element_by_id('loginbutton').click();
# =============================
# Notification Box pop up => Click on "Not Now"
browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click();
# ... Continue ...
