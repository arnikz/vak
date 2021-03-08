#!/usr/bin/env python

import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def main():
    url = "https://www.old.korona.gov.sk/covid-19-vaccination-form.php"
    expr = "/html/body/div[5]/form/div[1]/div[4]/button"
    exit_code = 0
    duration = 30
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")  
    with webdriver.Firefox(options=options) as driver:
        driver.get(url)
        driver.implicitly_wait(duration)
        elem = driver.find_element_by_xpath(expr)
        reg,n = elem.text.split("\n")
        if int(n) != 0:
            exit_code = 1
        print("{}: {}".format(reg, n))
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
