# Описание проекта

Данный репозиторий содержит проект, связанный с анализом данных, парсингом веб-сайта и построением модели машинного обучения. Проект выполнен с использованием Python и его библиотек для работы с данными, веб-парсинга и машинного обучения.

## Основные компоненты проекта:

- Парсинг данных: Используя библиотеки BeautifulSoup и Selenium, производится сбор информации с веб-сайта. В данном случае, собираются данные о продуктах с онлайн-магазина.
- Анализ данных: После сбора данных производится их анализ и подготовка к дальнейшей обработке.
- Построение модели машинного обучения: Применяется библиотека Scikit-learn для построения регрессионных моделей машинного обучения, таких как GradientBoostingRegressor и XGBRegressor, для предсказания рейтинга продуктов на основе полученных данных.

## Структура репозитория:

- `Store_scrape.py`: Код для парсинга данных с веб-сайта с использованием BeautifulSoup и Selenium.
- `Gradient_boosting_model.ipynb`: Jupyter Notebook с анализом данных, предварительной обработкой и визуализацией, а так же построением и оценкой моделей машинного обучения.
- `web_scraper_draft.ipynb`: Jupyter Notebook использованный в качестве черновика во время написания основного блока.
- `requirements.txt`: Список всех необходимых библиотек и их версий для воспроизведения окружения.
- `data_scraper_log.txt`: Файл с логами которые записываются в ходе сбора данных (оставил для примера).
- `Data`: Папка хранит в себе собранные данные, а так же обработанные данные.
- `models`: Папка с файлами сохраненных моделей для дальнейшего использования.

--------------------------------------------------------------------------------------------------
## Проект "Парсер данных и прогнозирование рейтинга товаров"
Я реализовал проект, включающий в себя несколько ключевых этапов:

### 1. Парсинг данных
Для начала, я разработал парсер, который собирает информацию о товарах с веб-сайта интернет-магазина. Этот парсер позволяет получать данные о ценах, рейтингах, отзывах и других характеристиках товаров. Используя библиотеки `requests` и `BeautifulSoup`, я успешно извлек данные и сохранял их в структурированный DataFrame.

### 2. Подготовка данных и EDA
Полученные данные были очищены и преобразованы для анализа и обучения модели. Я провел Exploratory Data Analysis (EDA), чтобы понять распределение данных, выявить корреляции между характеристиками и подготовить данные для дальнейшего обучения модели.

### 3. Построение модели машинного обучения
С использованием библиотеки `scikit-learn`, я построил регрессионную модель Gradient Boosting, которая прогнозирует рейтинг товаров на основе их характеристик. Модель обучалась на подготовленных данных и показала хорошие результаты в предсказаниях.

### 4. Применение LightGBM
Для расширения опыта работы с разными библиотеками, я переписал модель на библиотеку XGBRegressor. Это позволило мне ознакомиться с другим алгоритмом машинного обучения и сравнить результаты с предыдущей моделью.

### 5. Оптимизация и сохранение модели
Я провел оптимизацию моделей, настроил гиперпараметры и получил удовлетворительные значения среднеквадратичной ошибки. Затем я сохранил обе модели – Gradient Boosting и XGBRegressor – в файлы формата `.pkl` и `sav`, чтобы иметь возможность легко загрузить их для дальнейшего использования.

## Заключение
В определенный момент моей жизни я столкнулся с точкой застоя и, проведя некоторое время в размышлениях, осознал, что все мои предыдущие проекты, которые я выкладывал на GitHub, были созданы исключительно с коммерческой целью. Обладая опытом, но лишенный наглядного портфолио, я осознал, что часто бывает сложно продемонстрировать свой потенциал при поиске работы. В данный момент я решил исправить эту ситуацию и представить небольшой проект (несмотря на его скромность, прошу не судить строго). Я надеюсь, что моя работа покажется вам интересной и, возможно, вдохновит вас на великие свершения. Со временем я планирую улучшать свой профиль на GitHub, стремясь к своему общему развитию.

Данный проект отражает мои навыки в области парсинга данных, предварительной обработки, EDA и построения моделей машинного обучения. Моя цель – использовать эти навыки для извлечения ценных инсайтов из данных и создания моделей, которые помогут принимать более обоснованные решения и достигать успеха.

*Проект выполнен с использованием инструментов Python, библиотек pandas, scikit-learn, XGBRegressor и различных технологий для анализа данных.
Проект создан с целью демонстрации навыков работы с данными, веб-парсингом и машинным обучением. Здесь вы найдете исходный код, Jupyter Notebook с объяснением процесса и результата работы.*

## О себе
Я – опытный Data Analyst, в настоящее время работающий в fintech компании. Моя цель – стать специалистом Data Science и углубить свои знания в использовании технологий машинного обучения. В ходе сегодняшнего проекта я продемонстрировал свои навыки в области анализа данных и построении модели машинного обучения.

## Contacts
- LinkedIn: [@almat_orynbassarov](https://kz.linkedin.com/in/almat-orynbassarov-566352237)
- Email: almat.imangazin@gmail.com
