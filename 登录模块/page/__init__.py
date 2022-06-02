from selenium.webdriver.common.by import By

url = "http://test.zaitakugeek.cn:8080/login"

login_link = By.CSS_SELECTOR,'.el-button--mini > span'
login_input_username = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[1]/div/div/div[1]/input'
login_input_password = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[2]/div/div/div[1]/input'
login_btn = By.CSS_SELECTOR,'.el-button.el-button--primary'
login_err_text = By.CSS_SELECTOR,'.el-form-item__error'
login_err_up_text = By.CSS_SELECTOR,'.el-message__content'
