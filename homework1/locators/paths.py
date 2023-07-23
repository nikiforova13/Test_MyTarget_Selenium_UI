from selenium.webdriver.common.by import By

BUTTON_LOGIN = (By.CSS_SELECTOR, "[class*=responseHead-module-button]")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
BUTTON_LOGIN_AFTER_INPUT_DATA = (By.CLASS_NAME, "authForm-module-button-1u2DYF")
BUTTON_LOGOUT = (By.CLASS_NAME, "right-module-userNameWrap-3Odw2D")
LOGOUT = (By.CSS_SELECTOR, "[href='/logout']")

ERROR_PASSWORD_OR_LOGIN = (By.CLASS_NAME, "formMsg_title")
INPUT_NAME = (By.CSS_SELECTOR, "[data-name*='fio'] input")
INPUT_INN = (By.CSS_SELECTOR, "[data-name*='Inn'] input")
INPUT_PHONE = (By.CSS_SELECTOR, "[data-name*='phone'] input")
SAVE_CHANGE = (By.CSS_SELECTOR, "[class*='submit']")
GET_CURRENT_NAME = (By.CSS_SELECTOR, "[class*='right-module-userNameWrap']")
BUTTON_AUDIENCES = (
    By.CSS_SELECTOR,
    "[class*='center-module-button-14O4yB center-module-segments']",
)
CHECK_AUDIENCES = (By.CSS_SELECTOR, "[data-class-name*='SegmentsList']")

BUTTON_BALANCE = (By.CSS_SELECTOR, "[class*=' center-module-billing-1cIfj4']")
CHECK_BALANCE = (By.CSS_SELECTOR, "[class*='autodeposit']")

BUTTON_STATISTICS = (By.CSS_SELECTOR, "[class*='center-module-statistics-2Wbrwh']")
CHECK_STATISTICS = (By.CSS_SELECTOR, "[class*=page_statistics]")

BUTTON_PROFILE = (By.CSS_SELECTOR, "[class*='center-module-profile']")
CHECK_PROFILE = (By.CSS_SELECTOR, "[data-translated='Contact information']")

BUTTON_TOOLS = (By.CSS_SELECTOR, "[class*='center-module-tools']")
CHECK_TOOLS = (By.CSS_SELECTOR, "[class*=feeds]")
