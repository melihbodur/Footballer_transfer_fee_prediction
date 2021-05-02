#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium. common. exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

listem=[]
sy=1
while sy<30000:
    browser=webdriver.Chrome("C:\Selenium\chromedriver",options=chrome_options) 
    browser.get("https://sofifa.com/?offset="+str(sy)+"")
    n=1
    time.sleep(0.2)
    while n<61:
        browser=webdriver.Chrome("C:\Selenium\chromedriver",options=chrome_options) 
        browser.get("https://sofifa.com/?offset="+str(sy)+"")
       
        gir=browser.find_element_by_xpath("//*[@id='adjust']/div/div[1]/div/table/tbody/tr["+str(n)+"]/td[2]/a[1]/div")
        
        time.sleep(1)
        gir.click()
        
        try:
            ismi=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[1]/div[1]/div[1]/div/div/h1").text
            print(ismi)
            pozisyon=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[2]/div[1]/ul/li[1]/span").text
            puanı=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[1]/div/span").text
            değeri=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[3]/div").text
            maaşı=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[1]/div[1]/div[1]/div/section/div/div[4]/div").text
            serbest_kalma_fiyatı=browser.find_element_by_xpath("//*[@id='list']/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/ul/li[8]/span").text
        except:
            pass
        try:
            yine_gir=browser.find_element_by_xpath("//*[@id='list']/header/div[3]/div/div/div/a[2]")
        except:
            pass
        time.sleep(0.3)
        yine_gir.click()
        
        time.sleep(1)
       
        
        try:
            yaşı=browser.find_element_by_xpath("//*[@id='list']/div[1]/div/div/div[2]/div[1]/ul[1]/li[1]").text
        except:
            yaşı="nan"
        try:
            kilo=browser.find_element_by_xpath("//*[@id='list']/div[1]/div/div/div[2]/div[1]/ul[1]/li[3]").text
        except:
            kilo="nan"
        try:
            ülke=browser.find_element_by_xpath("//*[@id='list']/div[1]/div/div/div[2]/div[1]/ul[2]/li[1]/a").get_attribute("title")
        except:
            ülke="nan"
        time.sleep(0.3)
       
        x=1
        bilgileri=[]
        while x<10:
            
            bunda=browser.find_elements_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]")
            
            for i in bunda:
                sezon=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[1]").text
                takım=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[2]").text
                lig=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[3]").text
                oynadıgı_süre=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[4]").text
                appearance=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[5]").text
                lineup=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[6]").text
                substitute_in=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[7]").text
                substitute_out=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[8]").text
                substitute_on_bench=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[9]").text
                goal=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[10]").text
                yellow=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[10]").text
                yellow_2nd=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[10]").text
                red=i.find_element_by_xpath("//*[@id='page_player_1_block_player_career_6_table']/tbody/tr["+str(x)+"]/td[10]").text
                bilgileri.append([sezon,takım,lig,lineup,oynadıgı_süre,appearance,lineup,substitute_in,substitute_out,substitute_on_bench,goal,yellow,yellow_2nd,red])
            
            x+=1
           
        browser.quit()
        
        n+=1
        listem.append([ismi,pozisyon,ülke,puanı,değeri,maaşı,serbest_kalma_fiyatı,yaşı,kilo,bilgileri])
        print(listem)
    sy+=60   

