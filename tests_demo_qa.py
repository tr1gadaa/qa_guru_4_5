import pytest
from selene import be, have
from selene.support.shared import browser
import os


def test_positive_case(browser_settings):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('input[id=firstName]').should(be.blank).type('Mariia')
    browser.element('input[id=lastName]').should(be.blank).type('Levchenko')
    browser.element('input[id=userEmail]').should(be.blank).type('emailfortest@mail.com')
    browser.element('[for=gender-radio-2]').should(be.clickable).click()
    browser.element('input[id=userNumber]').should(be.blank).type('0123456789')
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('input[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('textarea[id=currentAddress]').should(be.blank).type('Russia, Moscow, Bolshaya st., 5')
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('.css-tlfecz-indicatorContainer').click()
    browser.element('[id=react-select-3-option-0]').click()
    browser.element('.css-tlfecz-indicatorContainer').click()
    browser.element('[id=react-select-4-option-1]').click()
    browser.element('button[id=submit]').click()
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('[id=closeLargeModal]').click()


def test_negative_case(browser_settings):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('input[id=firstName]').should(be.blank).type('Mariia')
    browser.element('input[id=lastName]').should(be.blank).type('Levchenko')
    browser.element('input[id=userEmail]').should(be.blank)
    browser.element('[for=gender-radio-2]').should(be.clickable).click()
    browser.element('input[id=userNumber]').should(be.blank).type('0123456789')
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('input[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('textarea[id=currentAddress]').should(be.blank).type('Russia, Moscow, Bolshaya st., 5')
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('.css-tlfecz-indicatorContainer').click()
    browser.element('[id=react-select-3-option-0]').click()
    browser.element('.css-tlfecz-indicatorContainer').click()
    browser.element('[id=react-select-4-option-1]').click()
    browser.element('button[id=submit]').click()
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.element('[id=closeLargeModal]').click()