from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.set_window_size(1280,960)

test_site_name = "https://xymetrics.org/?cmp_bypass=5850c833d91a546efdf40c48323e3f14"

driver.get(test_site_name)

# п.1 -- "Contacts" -- находим полную ссылку на Контакты, и нажимаем её
full_xpath = "/html/body/div[1]/header[1]/div[1]/div/div/div[1]/nav/ul/li[3]/a/span" # по тексту Contact
link = driver.find_element(By.XPATH, full_xpath)
link.click()

# п.2 -- Попадаем на страницу КОНТАКТЫ. Сначала проверим что мы на ней.
test_contact_page = "Leave Us a Message"
header_name: WebElement = driver.find_element(By.TAG_NAME, 'h3')

if test_contact_page == header_name.text:
    print("Мы на странице КОНТАКТЫ")
else:
    print("Мы НЕ на странице КОНТАКТЫ")


# п.3 -- Вводим данные в форму.
# п.3.1 -- Вводим Your Name
your_name = driver.find_element(By.NAME, 'your-name')
your_name.send_keys("My Test Name")

# п.3.2 -- Вводим Your Email
your_email = driver.find_element(By.NAME, 'your-email')
your_email.send_keys("my_test_email@gmail.vt")

# п.3.3 -- Вводим Subject
your_subject = driver.find_element(By.NAME, 'your-subject')
your_subject.send_keys("My Test Subject")

# п.3.4 -- Вводим Your Message
your_message = driver.find_element(By.NAME, 'your-message')
your_message.send_keys("My testing message on this page. My testing message on this page. My testing message on this page.")

# п.3.5 Находим кнопку Submit и нажимаем её
button_submit = driver.find_element(By.CLASS_NAME, 'wpcf7-submit')
button_submit.click()

# п.3.6 Проверяем что сообщение отправилось
abc = "Thank you for your message. It has been sent."
response_message: WebElement = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
WebDriverWait(driver, 5).until(visibility_of(response_message))
response_text = response_message.text
if response_text == abc:
        print("ТЕСТ №02 прошёл успешно. Сообщение отправилось.")
else:
    print("Тест №02 Не прошел. Сообщение НЕ отправилось.")



driver.close()