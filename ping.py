#!/usr/bin/env python

import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():
    url = "https://www.old.korona.gov.sk/covid-19-vaccination-form.php"
    xpath = "/html/body/div[5]/form/div[1]/div[4]/button"
    exit_code = 0
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")  
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    driver.get(url)
    driver.refresh()
    elem = driver.find_element_by_xpath(xpath)
    reg,n = elem.text.split("\n")
    if int(n) != 0:
        exit_code = 1
    print("{}: {}".format(reg, n))
    driver.quit()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
