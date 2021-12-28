import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import io
from PIL import Image

initiate = input("Would you like to activate the FIFA Mobile Database scraper?: ")


if initiate == "YES":

    search_term = input("What key word are you trying to look for?: ")

    url = "https://sappurit.github.io/s5art/"

    endings = []
    urls = []
    try:
        driver = webdriver.Chrome("C:/Users/mbah2/Downloads/chromedriver.exe")
        driver.get(url)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup)

        classes = soup.find_all('img')

        for img in classes:
            if search_term in img['src']:
                icon = img['src']
                endings.append(icon)



    except:
        print("driver not found")

    image_url = f"https://sappurit.github.io/s5art/{img['src']}"

    for ending in endings:
        iconurl = f"https://sappurit.github.io/s5art/{ending}"
        urls.append(iconurl)


    def download_image(download_path, url, file_name):
        try:
            image_content = requests.get(url).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)
            file_path = download_path + file_name

            with open(file_path, "wb") as f:
                image.save(f, "PNG")

            print(f"Successfully added {url} to the directory of {download_path}")

        except Exception as e:
            print('FAILED -', e)


    n = 1
    try:
        for i in urls:
            print(f"downloading {i}")
            download_image("imgs/", i, f'logo{n}.png')
            n += 1
        print(f'Successfully scraped! {url} ')
    except:
        print('couldnt download image')


elif initiate == "NO":
    print("Ok")
    exit()

else:
    print('Did not understand what you said, please repeat')
