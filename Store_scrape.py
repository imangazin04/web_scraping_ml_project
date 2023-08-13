# Импортируем нужные для работы библиотеки
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import logging

# Настройка логирования
logging.basicConfig(filename='data_scraper_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Запуск браузера в фоновом режиме
driver = webdriver.Chrome(options=options)
logging.info('Запуск скрапера')

# Создаем DataFrame с нужными колонами
df = pd.DataFrame(columns=['product', 'price', 'rating', 'recall', 'instalment', 'instalment_price', 'instalment_time'])

try:
    # Ожидаем, пока страница загрузится
    driver.get('https://kaspi.kz/shop/c/notebooks/')
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(2)

    # Ожидаем, пока появится элементы, чтобы кликнуть на них
    city_to_click = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dialogService"]/div/div[1]/div[1]/div/ul[1]/li[10]/a')))
    city_to_click.click()
    driver.implicitly_wait(2)
    category_to_click = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/nav/div/ul/li[5]/a/span')))
    category_to_click.click()
    driver.implicitly_wait(2)
    subcategory_click = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scroll-to"]/div[1]/div[1]/div/ul/li/ul/li[3]/span[1]')))
    subcategory_click.click()
    driver.implicitly_wait(2)
    select_product_click = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="scroll-to"]/div[1]/div[1]/div/ul/li/ul/li/ul/li[1]/span[1]')))
    select_product_click.click()
    driver.implicitly_wait(2)

    # Передаем в объект soup данные текущей страницы
    soup = bs(driver.page_source, 'html.parser')

    page_value = 1
    #######################           Запускаем цикл сбора данных                   ######################
    while True:
        # Ждём появления и находим список элементов пагинации
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'pagination')))
        pagination = driver.find_element(By.CLASS_NAME, 'pagination')
        pagination_elements = pagination.find_elements(By.CLASS_NAME, 'pagination__el')

        # Пытаемся найти и нажать кнопку "Следующая", если она доступна
        try:
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'item-card__info')))
            driver.implicitly_wait(60)
            requiredHtml = driver.page_source
            soup = bs(requiredHtml, 'html.parser')

            # Извлекаем нужные данные из элемента
            for cur in soup.find_all('div', class_='item-card__info'):
                now_rating = re.findall("[0-9]+", str(cur.select('span')[0]))
                now_rating = int(now_rating[0])

                now_price = cur.select('.item-card__prices-price')[0].getText().strip()
                now_price = int("".join(now_price[:-1].split()))

                now_recall = cur.select('.item-card__rating')[0].getText().strip()

                instalment = cur.select_one('.item-card__instalment .item-card__prices-title').get_text(strip=True)
                instalment_price = cur.select_one('.item-card__instalment .item-card__prices-price').get_text(
                    strip=True)
                instalment_time = cur.select_one('.item-card__instalment .item-card__add-info').get_text(strip=True)

                now_product = cur.select('a')[0].getText().strip()

                df.loc[len(df.index)] = [now_product, now_price, now_rating, now_recall, instalment, instalment_price,
                                         instalment_time]
                logging.info('Данные успешно сохранены в файл scraped_product_data_almaty.csv')

            # Проверяем активность кнопки переключения страниц
            next_button = pagination_elements[-1]
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            driver.implicitly_wait(60)
            page_value += 1
            print('Done: ' + str(page_value))

        # Если кнопка "Следующая" не найдена, переходим к следующей итерации
        except Exception as e:
            logging.error('Произошла ошибка в области pagination: ' + str(e))
            continue

# Обрабатываем ошибки и сохраняем лог ошибок
except Exception as e:
    logging.error('Произошла ошибка: ' + str(e))
    df.to_csv('./Data/scraped_product_data_almaty.csv', sep=';', index=False, encoding='utf-8')
# После завершения работа, закрываем браузер, сохраняем данные и записываем логи о завершении работы
finally:
    driver.quit()
    df.to_csv('./Data/scraped_product_data_almaty.csv', sep=';', index=False, encoding='utf-8')
    logging.info('Скрапер завершил работу')
