

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import tiktok.constants as const


class TikTok(webdriver.Chrome):
    def __init__(self):
        self.service=ChromeService(ChromeDriverManager().install())
        super(TikTok,self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()
               
    def __exit__(self, exc_type, exc,traceback):
        self.quit()

    def getBaseUrl(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(5)
    
    def register(self):
        try: 
            # click "Giriş Yap"          
            WebDriverWait(self,30).until(EC.presence_of_element_located((By.XPATH,"//button[@data-e2e='top-login-button']"))).click()
            print("Click 'Giriş Yap' Button")             
            
            #click "Kaydol"
            WebDriverWait(self,30).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Kaydol']"))).click()
            #self.find_element(By.XPATH,"//a[normalize-space()='Kaydol']").click()      
            print("Click 'Kaydol' Button")
            
            #click "telefon-email kullan"
            WebDriverWait(self,30).until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Telefon veya eposta kullan']"))).click()
            #self.find_element(By.XPATH,"//a[normalize-space()='Telefon veya eposta kullan']").click() 
            print("Click 'Kullanıcı Adı/E-Posta Kullan' Button")    
            self.implicitly_wait(3)
            
            #select Month     
            WebDriverWait(self,30).until(EC.presence_of_element_located((By.XPATH,"//div[normalize-space()='Ay']"))).click()
            self.implicitly_wait(3)              
            self.find_element(By.XPATH,"//div[normalize-space()='Ocak']").click() 
            print("Select Month")    
            
            #select day     
            WebDriverWait(self,30).until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Gün']"))).click()
            self.implicitly_wait(3)  
            self.find_element(By.XPATH,"//div[normalize-space()='10']").click() 
            print("Select Day")    
            
            #select year     
            WebDriverWait(self,30).until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Yıl']"))).click()
            self.implicitly_wait(3)  
            self.find_element(By.XPATH,"//div[normalize-space()='2000']").click() 
            print("Select Year")    
            
            #click "Eposta ile kaydol"     
            self.find_element(By.XPATH,"//a[@href='/signup/phone-or-email/email']").click() 
            print("Click 'Kullanıcı Adı/E-Posta Kullan' Button")    
            self.implicitly_wait(3)       
            
            #open temp-mail       
            eposta = self.open_temp_mail()
            self.implicitly_wait(5)
            self.switch_to.window(self.window_handles[0])
            
            email_element = self.find_element(By.NAME,"email")
            self.execute_script(f"document.getElementsByName('email').value = '{eposta}')")
            
            



           
        except TimeoutException:
            print("Timeoutexception")
            self.close
            self.quit
        finally:
            input("Press any key for exit...")
    
    def open_temp_mail(self):
        self.execute_script("window.open('');")
        self.switch_to.window(self.window_handles[1])
        self.get(const.TEMP_MAIL_URL)
        eposta = WebDriverWait(self,30).until(EC.element_to_be_clickable((By.ID,"eposta_adres"))).get_attribute("value")
        #eposta = self.find_element(By.ID,"eposta_adres").get_attribute("value")
        print(eposta)
        return eposta
    
        
