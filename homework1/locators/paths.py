from selenium.webdriver.common.by import By

BUTTON_LOGIN = (By.CSS_SELECTOR, "[class*=responseHead-module-button]")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
BUTTON_LOGIN_AFTER_INPUT_DATA= (By.CLASS_NAME, "authForm-module-button-1u2DYF")
BUTTON_LOGOUT = (By.CLASS_NAME, "right-module-userNameWrap-3Odw2D")
LOGOUT = (By.CSS_SELECTOR, "[href='/logout']")

ERROR_PASSWORD_OR_LOGIN = (By.CLASS_NAME, "formMsg_title")
BUTTON_PROFILE = (By.CSS_SELECTOR, "[data-gtm-id='pageview_profile']")
INPUT_NAME = (By.CSS_SELECTOR, "[data-name*='fio'] input")
SAVE_CHANGE = (By.CSS_SELECTOR, "[class*='submit']")
GET_CURRENT_NAME = (By.CSS_SELECTOR, "[class*='right-module-userNameWrap']")
