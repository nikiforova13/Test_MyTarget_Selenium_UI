from selenium.webdriver.common.by import By


class ButtonForAuthorization:
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[class*=responseHead-module-button]")
    BUTTON_LOGIN_AFTER_INPUT_DATA = (By.CSS_SELECTOR, "[class*=authForm-module-button]")
    BUTTON_PROFILE = (By.CSS_SELECTOR, "[class*=right-module-userNameWrap]")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "[href='/logout']")


class FieldsForInputData:
    INPUT_EMAIL_FIELD = (By.NAME, "email")
    INPUT_PASSWORD_FIELD = (By.NAME, "password")
    INPUT_NAME_FIELD = (By.CSS_SELECTOR, "[data-name*='fio'] input")
    INPUT_INN_FIELD = (By.CSS_SELECTOR, "[data-name*='Inn'] input")
    INPUT_PHONE_FIELD = (By.CSS_SELECTOR, "[data-name*='phone'] input")


class ButtonForNavigatingPages:
    BUTTON_AUDIENCES = (
        By.CSS_SELECTOR,
        "[class*='center-module-button- center-module-segments']",
    )
    BUTTON_BALANCE = (By.CSS_SELECTOR, "[class*='center-module-billing']")
    BUTTON_STATISTICS = (By.CSS_SELECTOR, "[class*='center-module-statistics']")
    BUTTON_PROFILE = (By.CSS_SELECTOR, "[class*='center-module-profile']")
    BUTTON_TOOLS = (By.CSS_SELECTOR, "[class*='center-module-tools']")


class ButtonForSavingChanges:
    SAVE_CHANGE = (By.CSS_SELECTOR, "[class*='submit']")


class Check:
    CURRENT_USERNAME = (By.CSS_SELECTOR, "[class*='right-module-userNameWrap']")
    PAGE_AUDIENCES = (By.CSS_SELECTOR, "[data-class-name*='SegmentsList']")
    PAGE_BALANCE = (By.CSS_SELECTOR, "[class*='autodeposit']")
    PAGE_STATISTICS = (By.CSS_SELECTOR, "[class*=page_statistics]")
    PAGE_PROFILE = (By.CSS_SELECTOR, "[data-translated='Contact information']")
    PAGE_TOOLS = (By.CSS_SELECTOR, "[class*=feeds]")
    ERROR_LOGIN_WITH_INVALID_DATA = (By.CLASS_NAME, "formMsg_title")
    MENU_AUDIENCES = (By.CSS_SELECTOR, "[class*='instruction-module-title']")
