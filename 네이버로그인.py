#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


import pyperclip
import time


# In[3]:


from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/가족 통합/python/chromedriver.exe")

driver.get("http://naver.com")


# In[4]:


# button = driver.find_element_css_selector('#search_btn')
# button = WebdriverWait(driver, 5).until(EC.presence_of_elment_located((By.CSS_SELECTOR, '#search_btn'))
# button.click()
                                    
    


# In[5]:


xpath = '//*[@id="account"]/a'
driver.find_element_by_xpath(xpath).click()


# In[ ]:





# In[6]:


pyperclip.copy('2833612')
time.sleep(3)
xpath2 = '//*[@id="id"]'
driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v')


# In[7]:


pyperclip.copy('seller1004@')
time.sleep(3)
xpath3 = '//*[@id="pw"]'
driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v')


# In[8]:


xpath4 = '//*[@id="log.login"]'
time.sleep(3)
driver.find_element_by_xpath(xpath4).click()


# In[9]:


xpath5 = '//*[@id="new.save"]'
time.sleep(3)
driver.find_element_by_xpath(xpath5).click()

