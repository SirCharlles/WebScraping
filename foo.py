import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ('C:/Users/USER//WebDriver/chromedriver.exe')
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get('https://oxylabs.io/blog')

results = []
other_results = []
counter = 0

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()



for a in soup.findAll(attrs='css-9issdx esl9i4u1'):
    name = a.find('h5')
    date = a.find(attrs='css-1uydhl8 e15x7lld2')
    if name and date:
        results.append(name.text)
        other_results.append(date.text)
        counter += 1
    if counter >= 19:
        break

df = pd.DataFrame({'Names': results, 'Dates': other_results})



df = pd.DataFrame({'Names:':results, 'Dates':other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
