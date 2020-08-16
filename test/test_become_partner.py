# -*- coding: utf-8 -*-
import pytest
from model.partner import Partner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import testdata

@pytest.mark.parametrize('partner', testdata, ids=[repr(x) for x in testdata])
def test_send_partner(app, partner):
    #открываем начальную страницу
    app.open_partner_page()
    #заполняем форму "стать партнером"
    app.add_partner_information(partner)
    #отправляем форму
    app.send_partner_information()
    app.wd.implicitly_wait(20)
    #проверяем, что форма отправлена
    assert_element = WebDriverWait(app.wd, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".iziAlert")))
    value = u"Специалист Clover Group свяжется с вами в рабочее время."
    assert assert_element.text == value

def test_send_empty_partner(app):
    #открываем начальную страницу
    app.open_partner_page()
    #отправляем пустую форму
    app.add_partner_information(Partner(phone='', email='', name='', question=''))
    result = app.send_partner_information()
    #проверяем, что пустую форму невозможно отправить
    assert result == "element is not clickable"

