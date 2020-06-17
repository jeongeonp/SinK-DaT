from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def iterate_all_occurences(home_url):
    driver = webdriver.Chrome('chromedriver.exe')
    # driver.get("https://ko.dict.naver.com/#/search?query=%EC%8B%9C%EC%9C%84")
    driver.get(home_url)


    elems = driver.find_elements_by_css_selector('.highlight')[0]

    for elem in elems:
        time.sleep(0.5)
        elem.click()

        time.sleep(0.5)
        #INSERT PARSING HERE
        time.sleep(0.5)

        driver.execute_script("window.history.go(-1)")
        time.sleep(0.5)



#BELOW IS GARBAGE
# elem.send_keys("hello")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# new_elem = driver.find_element_by_id("result-stats")

# print((new_elem.text).split("약")[1].split("개")[0].replace(",",""))
# # driver.close()