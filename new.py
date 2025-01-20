from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
import time
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "only"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920, 1200")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def run_bot(data_account, recover=1):
    kw = data_account[0]

    driver = web_driver()
    driver.maximize_window()

    try:
        
        driver.get(kw)
        time.sleep(3)
        
        selector1 = 'body > div > div.gallery-grid > div:nth-child(1) > div.tg-channel-link > a > img'
        element1 = driver.find_element(By.CSS_SELECTOR, selector1)
        judul1 = element1.text

        selector2 = 'body > div > div.gallery-grid > div:nth-child(2) > div.tg-channel-link > a > img'
        element2 = driver.find_element(By.CSS_SELECTOR, selector2)
        judul2 = element2.text

        selector3 = 'body > div > div.gallery-grid > div:nth-child(3) > div.tg-channel-link > a > img'
        element3 = driver.find_element(By.CSS_SELECTOR, selector3)
        judul3 = element3.text

        selector4 = 'body > div > div.gallery-grid > div:nth-child(4) > div.tg-channel-link > a > img'
        element4 = driver.find_element(By.CSS_SELECTOR, selector4)
        judul4 = element4.text

        selector5 = 'body > div > div.gallery-grid > div:nth-child(5) > div.tg-channel-link > a > img'
        element5 = driver.find_element(By.CSS_SELECTOR, selector5)
        judul5 = element5.text

        selector6 = 'body > div > div.gallery-grid > div:nth-child(6) > div.tg-channel-link > a > img'
        element6 = driver.find_element(By.CSS_SELECTOR, selector6)
        judul6 = element6.text

        selector7 = 'body > div > div.gallery-grid > div:nth-child(7) > div.tg-channel-link > a > img'
        element7 = driver.find_element(By.CSS_SELECTOR, selector7)
        judul7 = element7.text

        selector8 = 'body > div > div.gallery-grid > div:nth-child(8) > div.tg-channel-link > a > img'
        element8 = driver.find_element(By.CSS_SELECTOR, selector8)
        judul8 = element8.text

        selector9 = 'body > div > div.gallery-grid > div:nth-child(9) > div.tg-channel-link > a > img'
        element9 = driver.find_element(By.CSS_SELECTOR, selector9)
        judul9 = element9.text

        selector10 = 'body > div > div.gallery-grid > div:nth-child(10) > div.tg-channel-link > a > img'
        element10 = driver.find_element(By.CSS_SELECTOR, selector10)
        judul10 = element10.text


        selector11 = 'body > div > div.gallery-grid > div:nth-child(11) > div.tg-channel-link > a > img'
        element11 = driver.find_element(By.CSS_SELECTOR, selector11)
        judul11 = element11.text

        selector12 = 'body > div > div.gallery-grid > div:nth-child(12) > div.tg-channel-link > a > img'
        element12 = driver.find_element(By.CSS_SELECTOR, selector12)
        judul12 = element12.text

        selector13 = 'body > div > div.gallery-grid > div:nth-child(13) > div.tg-channel-link > a > img'
        element13 = driver.find_element(By.CSS_SELECTOR, selector13)
        judul13 = element13.text

        selector14 = 'body > div > div.gallery-grid > div:nth-child(14) > div.tg-channel-link > a > img'
        element14 = driver.find_element(By.CSS_SELECTOR, selector14)
        judul14 = element14.text

        selector15 = 'body > div > div.gallery-grid > div:nth-child(15) > div.tg-channel-link > a > img'
        element15 = driver.find_element(By.CSS_SELECTOR, selector15)
        judul15 = element15.text

        selector16 = 'body > div > div.gallery-grid > div:nth-child(16) > div.tg-channel-link > a > img'
        element16 = driver.find_element(By.CSS_SELECTOR, selector16)
        judul16 = element16.text

        selector17 = 'body > div > div.gallery-grid > div:nth-child(17) > div.tg-channel-link > a > img'
        element17 = driver.find_element(By.CSS_SELECTOR, selector17)
        judul17 = element17.text

        selector18 = 'body > div > div.gallery-grid > div:nth-child(18) > div.tg-channel-link > a > img'
        element18 = driver.find_element(By.CSS_SELECTOR, selector18)
        judul18 = element18.text

        selector19 = 'body > div > div.gallery-grid > div:nth-child(19) > div.tg-channel-link > a > img'
        element19 = driver.find_element(By.CSS_SELECTOR, selector19)
        judul19 = element19.text

        selector20 = 'body > div > div.gallery-grid > div:nth-child(20) > div.tg-channel-link > a > img'
        element20 = driver.find_element(By.CSS_SELECTOR, selector20)
        judul20 = element20.text






        data_text = f"{judul1}\n{judul2}\n{judul3}\n{judul4}\n{judul5}\n{judul6}\n{judul7}\n{judul8}\n{judul9}\n{judul10}\n{judul11}\n{judul12}\n{judul13}\n{judul14}\n{judul15}\n{judul16}\n{judul17}\n{judul18}\n{judul19}\n{judul20}"



        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": data_text})
            .execute()
        )

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            #driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
