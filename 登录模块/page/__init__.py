from selenium.webdriver.common.by import By

url = "http://test.zaitakugeek.cn:8080/home"

login_link = By.CSS_SELECTOR,'.el-button--mini > span'
login_input_username = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[1]/div/div/div[1]/input'
login_input_password = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[2]/div/div/div[1]/input'
login_btn = By.CSS_SELECTOR,'.el-button.el-button--primary'
login_err_text = By.CSS_SELECTOR,'.tips_icon_error'
