'''import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get('http://demo-store.seleniumacademy.com/')

	def test_new_user(self):
		driver = self.driver
		driver.find_element_by_xpath('/html/body/div[1]/div[2]/header/div/div[2]/div/a/span[2]/font/font').click()
		driver.find_element_by_xpath('Log In').click()

		create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span/font/font')
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
		create_account_button.click()

		self.assertEqual('Create New Customer Account', driver.title)

		first_name = driver.find_element_by_id('firstname')
		middle_name = driver.find_element_by_id('middlename')
		last_name = driver.find_element_by_id('lastname')
		email_address = driver.find_element_by_id('email_address')
		news_letter_subscription = driver.find_element_by_id('is_subscribed')
		password = driver.find_element_by_id('password')
		confirm_password = driver.find_element_by_id('confirmation')
		submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

		self.assertTrue(first_name.is_enabled()
			and middle_name.is_enabled()
			and last_name.is_enabled()
			and email_address.is_enabled()
			and news_letter_subscription.is_enabled()
			and password.is_enabled()
			and confirm_password.is_enabled()
			and submit_button.is_enabled())

		first_name.send_keys('Test')
		driver.implicitly_wait(3)
		middle_name.send_keys('Test')
		driver.implicitly_wait(3)
		last_name.send_keys('Test')
		driver.implicitly_wait(3)
		email_address.send_keys('Test@testingmail.com')
		driver.implicitly_wait(3)
		password.send_keys('Test')
		driver.implicitly_wait(3)
		confirm_password.send_keys('Test')
		driver.implicitly_wait(3)
		submit_button.click()

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)'''

import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")
	
	def test_new_user(self):
		driver = self.driver
		#le decimos al driver que encuentre la opci??n de cuenta por su Xpath y le haga click para desplegar el menu
		driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
		#el driver va a buscar el enlace por su texto y haga click
		driver.find_element_by_link_text('Log In').click()
		#creo una variable asociada al bot??n de crear cuenta
		create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
		
		#validamos que el bot??n est?? visible y habilitado
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
		create_account_button.click()

		#comprueba que estamos en el sitio de crear cuenta
		self.assertEqual('Create New Customer Account', driver.title)

		#creaci??n de variables con el nombre del selector correspondiente
		first_name = driver.find_element_by_id('firstname')
		last_name = driver.find_element_by_id('lastname')
		email_address = driver.find_element_by_id('email_address')
		password = driver.find_element_by_id('password')
		confirm_password = driver.find_element_by_id('confirmation')
		news_letter_subscription = driver.find_element_by_id('is_subscribed')
		submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

		#veremos si los elementos est??n habilitados
		self.assertTrue(first_name.is_enabled() 
		and last_name.is_enabled()
		and email_address.is_enabled()
		and password.is_enabled()
		and confirm_password.is_enabled()
		and news_letter_subscription.is_enabled()
		and submit_button.is_enabled())

		#mandamos los datos al formulario
		first_name.send_keys('Test')
		last_name.send_keys('Test')
		email_address.send_keys('Test@testingmail.com') #sacado de 10-minute mail
		password.send_keys('Test')
		confirm_password.send_keys('Test')
		submit_button.click()

	def tearDown(self):
		self.driver.implicitly_wait(30)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)