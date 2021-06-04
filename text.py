import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as rs
def explore(url):
    page=rs.get(url)
    content=page.text
    global soup
    soup= bs(content, 'html.parser')
    for link in soup.find_all('pre'):
        print(link.text())
        
        
   
explore('https://www.tutorialspoint.com/sql/sql-syntax.htm')
  
