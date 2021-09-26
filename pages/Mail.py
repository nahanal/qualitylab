from time import sleep

from pages.Base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MailPage:
    # login objects
    mail_username_field = (By.CSS_SELECTOR, ".email-input")
    domain_selector_button = (By.CSS_SELECTOR, ".domain-select")
    enter_password_button = (By.CSS_SELECTOR, ".button")
    mail_password_field = (By.CSS_SELECTOR, ".password-input")
    login_button = (By.CSS_SELECTOR, ".second-button")

    # email message creation objects
    create_message_button = (By.CSS_SELECTOR, ".compose-button")
    subject_field = (By.CSS_SELECTOR, ".container--3QXHv > div:nth-child(1) > input:nth-child(1)")
    message_text_field = (By.XPATH, "/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]")
    receiver_field = (By.CSS_SELECTOR, ".container--ItIg4 > div:nth-child(1) > input:nth-child(1)")
    send_message_button = (By.CSS_SELECTOR, "span.button2_base:nth-child(1)")
    sent_message_window = (By.CSS_SELECTOR, ".layer__link")


class Helper(BasePage):

    def login(self, email_username, email_password, domain):
        login_input = self.find_element(MailPage.mail_username_field)
        login_input.send_keys(email_username)
        choose_domain = Select(self.find_element(MailPage.domain_selector_button))
        choose_domain.select_by_value(domain)
        enter_password = self.find_element(MailPage.enter_password_button).click()
        sleep(0.5)
        password_input = self.find_element(MailPage.mail_password_field)
        password_input.send_keys(email_password)
        login_to_mail = self.find_element(MailPage.login_button).click()
        sleep(5)

    def send_simple_new_message(self, subject, receiver, text):
        start_message_creation = self.find_element(MailPage.create_message_button).click()
        sleep(3)
        receiver_field = self.find_element(MailPage.receiver_field)
        enter_receiver = receiver_field.send_keys(receiver)
        subject_field = self.find_element(MailPage.subject_field)
        enter_message_subject = subject_field.send_keys(subject)
        message_text_field = self.find_element(MailPage.message_text_field)
        enter_message_text = message_text_field.send_keys(text)
        send_message = self.find_element(MailPage.send_message_button).click()
        sleep(3)

    def check_mail_sent(self):
        message_sent = self.find_element(MailPage.sent_message_window).text
        return message_sent
