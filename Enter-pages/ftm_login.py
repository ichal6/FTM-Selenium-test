import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FollowTheMoneyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_with_correct_credentials(self):
        driver = self.driver
        driver.get("https://ftm-client.herokuapp.com/login")

        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "password")
        email.send_keys("user@user.pl")
        password.send_keys("user1")
        password.send_keys(Keys.RETURN)

        user_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//header/div[1]/a[1]/p'))).text

        self.assertEqual("User Userowy", user_name)

    def test_login_with_wrong_credentials(self):
        driver = self.driver
        driver.get("https://ftm-client.herokuapp.com/login")

        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "password")
        email.send_keys("bad@user.pl")
        password.send_keys("bad2")
        password.send_keys(Keys.RETURN)

        warning = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'warning'))).text

        self.assertEqual("Your username or password was not recognised - try again.", warning)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
