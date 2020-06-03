import requests
import os
from bs4 import BeautifulSoup

result = requests.get(
    "https://www.google.com/search?q=models&sxsrf=ALeKk02Rqoewsr0iQ5erEKP5lYeK4xv6tg:1591181498606&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi1jv3_vOXpAhX8lEsFHe8TAy4Q_AUoAXoECA8QAw")
soup = BeautifulSoup(result.content, 'html.parser')
links = soup.find_all("img")

if not os.path.exists('models'):
    os.makedirs('models')

os.chdir('models')

x = 0

for image in links:
    try:
        url = image['src']
        source = requests.get(url)

        if source.status_code == 200:

            with open('model-'+str(x)+'.jpg', 'wb')as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
                if(x == 10):
                    break
    except:

        pass
