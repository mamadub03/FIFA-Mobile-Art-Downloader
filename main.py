import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import io
from PIL import Image
import os
from tqdm import tqdm
import time



directory = "BeautifulSoup"
parent_dir = "C:/Users/mbah2/PycharmProjects"

PATH = os.path.join(parent_dir,directory)

initiate = input("Would you like to activate the FIFA Mobile Database scraper?: ")


def progress_bar(iterable):
    for i in tqdm(iterable):
        time.sleep(2)


if initiate == "YES":

    search_term = input("What key word are you trying to look for?: ")

    folder_name = input("What will you like to name your folder?: ")

    file_name = input("What will you like to name your file?: ")

    url = "https://sappurit.github.io/s5art/"

    endings = []
    urls = []
    try:
        driver = webdriver.Chrome("C:/Users/****/Downloads/chromedriver.exe")
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
        os.mkdir(folder_name)

        for i in urls:
            download_image(f"{folder_name}/", i, f'{file_name}{n}.png')
            n += 1
        print(f'Successfully scraped! {url} ')
    except:
        print('couldnt download image')


elif initiate == "NO":
    print("Ok")
    exit()

else:
    print('Did not understand what you said, please repeat')
