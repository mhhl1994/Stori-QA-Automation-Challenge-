from time import sleep
import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select



import time


class TestStori():

    def setup_class(self):
        param = conftest.option
        if param == "chrome":
            self.driver = webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")
        if param == "firefox": 
            self.driver = webdriver.Firefox(executable_path="./Drivers/geckodriver.exe")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        

    def teardown_class(self):
        driver = self.driver
        sleep(1)
        driver.close()
        driver.quit()
        
        

    def test_1_goTo_rahulshettyacademy(self):
        driver = self.driver
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")   

    def test_2_SuggestionClass(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id=\'select-class-example\']/fieldset/input").click()
        driver.find_element_by_xpath("//div[@id=\'select-class-example\']/fieldset/input").send_keys("Me")
        self.driver.find_element_by_xpath("//ul[@id=\'ui-id-1\']/li[6]/div").click()

    def test_3_DropdownExample(self):
        driver = self.driver
        driver.find_element_by_xpath("//select").click()
        driver.find_element_by_xpath("//*[@id='dropdown-class-example']/option[3]").click()
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='dropdown-class-example']/option[4]").click()

    def test_4_SwitchWindow(self):
        driver = self.driver
        driver.find_element_by_id("openwindow").click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath("//*[@id='homepage']/div[4]/div[2]/div/div/div/span/div/div[7]/div/div/div[2]").click()
        driver.switch_to.window(driver.window_handles[1])
        moneyBack_Text = driver.find_element_by_xpath("//*[@id='welcome']/div/div/div/div[5]/div/div[2]/div/div[2]/p").text
        correctText = "We would never want you to be unhappy! If you are unsatisfied with your purchase, contact us in the first 30 days and we will give you a full refund."
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        assert moneyBack_Text == correctText
        
        

    def test_5_SwitchTab(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='opentab']").click()
        if conftest.option == "chrome":
            driver.switch_to.window(driver.window_handles[1])
        element = driver.find_element_by_css_selector(".btn-primary")
        actions = ActionChains(driver)
        sleep(2)
        actions.move_to_element(element).perform()
        driver.save_screenshot("./Screenshots/MainPage_ViewAllCourses.png")

    def test_6_AlertExample(self):
        driver = self.driver
        driver.switch_to.window(driver.window_handles[0])
        alert_Text = driver.find_element_by_xpath("//input[@id='name']")
        alert_Text.send_keys("Stori Card")
        driver.find_element_by_css_selector("#alertbtn").click()
        alert = Alert(driver)
        print(alert.text)
        alert.accept()

        alert_Text.send_keys("Stori Card")
        driver.find_element_by_css_selector("#confirmbtn").click()
        
        assert driver.switch_to.alert.text == "Hello Stori Card, Are you sure you want to confirm?"
        alert.accept()

    def test_7_WebTable(self):
        driver = self.driver
        table = driver.find_element_by_css_selector("#product tbody")
        priceColumn = table.find_elements_by_css_selector(" tr > td:nth-child(3)")
        courseColumn = table.find_elements_by_css_selector(" tr > td:nth-child(2)")

        numberOfCourses = 0
        iteration = 0
        courseNames = ""
        for row in priceColumn:
            if row.text == "25":
                numberOfCourses += 1
                courseNames = courseNames + courseColumn[iteration].text + ", "
            iteration =+ 1

        print('Number of courses that are $25 = ', numberOfCourses)
        print('Courses that are $25 = ', courseNames)


    def test_8_WebTableFixedHeader(self):
        driver = self.driver
        positionColumn = driver.find_elements_by_css_selector("tbody:nth-child(2) > tr > td:nth-child(2)")
        namesColumn = driver.find_elements_by_css_selector("tbody:nth-child(2) > tr > td:nth-child(1)")

        numberOfEngineers = 0
        iteration = 0
        engineerNames = ""
        for row in positionColumn:
            if row.text == "Engineer":
                numberOfEngineers += 1
                engineerNames = engineerNames + namesColumn[iteration].text + ", "
            iteration =+ 1
        print('Name of the engineers = ', engineerNames)


    def test_9_iFrameText(self):
        driver = self.driver
        driver.switch_to.frame(0)
        textInFrame = driver.find_elements_by_xpath("//ul[@class='list-style-two']/li")
        for textNumber in range(len(textInFrame)):
            if (textNumber % 2) == 0 :
                print(textInFrame[textNumber].text)