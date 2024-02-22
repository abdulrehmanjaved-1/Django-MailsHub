from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_emails(search_query):
    opts = Options()
    opts.add_experimental_option("detach",True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)
    driver.get("https://www.google.com/")

    tb = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    tb.send_keys(search_query, Keys.ENTER)

    link = driver.find_element(By.CSS_SELECTOR,"div.yuRUbf > div > span > a[href]")
    link.click()
    page = driver.page_source
    email_format = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", re.I)
    emails = email_format.findall(page)

    driver.quit()  # Quit the driver to release resources
    return emails
