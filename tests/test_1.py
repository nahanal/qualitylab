import pytest
from selenium import webdriver

from configs.email_config import cfg
from pages.Mail import Helper


@pytest.fixture(scope="session")
def fxt():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, domain", [(cfg["USERNAME"], cfg["PASSWORD"], cfg["DOMAIN"])])
@pytest.mark.parametrize("receiver, subject, text", [(cfg["RECEIVER"], "Test_subject", "Test text")])
def test_send_simple_mail_message(fxt, username, password, domain, receiver, subject, text):
    """
    Цель: убедиться в том, что отправка письма работает
    1. Открыть главную страницу mail.ru
    2. Войти в аккаунт
    3. Задать тему, получателя, и текст письма
    4. Отправить письмо
    5. Убедиться что после отправки письма появляется окно с ожидаемым сообщением
    """
    expected = "Письмо отправлено"
    main_page = Helper(fxt)
    main_page.go_to_site()  # Открывает главную страницу mail.ru
    main_page.login(email_username=username, email_password=password, domain=domain)    # Вход в аккаунт
    main_page.send_simple_new_message(receiver=receiver, text=text, subject=subject)    # Отправка письма
    mail_sent = main_page.check_mail_sent()  # Текст из окна появляющегося после отправки письма
    assert mail_sent == expected
