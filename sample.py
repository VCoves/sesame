from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from undetected_chromedriver import Chrome, ChromeOptions
import time

def main():
    print("Success before anything")
    sleep_secs = 8
    print(f"Sleeping {sleep_secs}")
    time.sleep(sleep_secs)
    print(f"Wake after {sleep_secs}")
    
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox') # An error will occur without this line
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    #driver = webdriver.Chrome(options=options)
    url1 = 'http://172.17.0.2:4444/'
    url2 = 'http://localhost:4444/wd/hub'
    driver = webdriver.Remote(
        command_executor=url2,
        options=options
        )

    print("Success Remote ")
    
    try:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

        print("Test Success!")
        time.sleep(3)
        print("Ending...!")
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    main()