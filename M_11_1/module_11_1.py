# pip install beautifulsoup4
# pip install lxml
# pip install requests
# pip install googletrans
from bs4 import BeautifulSoup
from googletrans import Translator
from requests import get, ConnectionError, RequestException, HTTPError, ConnectTimeout

# Константы с адресом сайта и количеством его страниц, для постраничного запроса
URL = 'https://quotes.toscrape.com/'  # Сайт с цитатами
PAGE_COUNT = 10


# Функция переводчик
def translater(text, in_lang='en', out_lang='ru'):
    translation = tr.translate(text, src=in_lang, dest=out_lang)
    return translation.text


# Создание списка URL-адресов для запроса по каждому
url_pages = [f'{URL}page/{num}/' for num in range(1, PAGE_COUNT + 1)]

# Определение объекта класса переводчика
tr = Translator()

# Цикл в котором обрабатывается каждая страница по отдельности
for url_ in url_pages:
    # Отлов ошибок при URL-запросе
    try:
        # Считывание сырой информации со страницы сайта
        response = get(url_)
    except ConnectionError:
        print('Проверьте подключение к интернету.')
    except RequestException:
        print('Произошло неоднозначное исключение, которое произошло при обработке вашего запроса.')
    except HTTPError:
        print('Произошла ошибка HTTP.')
    except ConnectTimeout:
        print('Вышло время ожидания ответа. Производится повторная попытка')
        response = get(url_)
        print('Повторная попытка провалена, переход к следующему запросу')

    # Создание обьекта анализатора со считанной сырой инфой
    soup = BeautifulSoup(response.text, 'lxml')
    # Фильтрация нужной инфы по ключам (Фильтруются цитаты)
    quotes = soup.find_all('span', class_='text')
    # Фильтруются авторы цитат так же по ключам
    authors = soup.find_all('small', class_='author')
    # Создание словаря где ключ=автор, а значение=цитата (Каждая цитата ещё переводится)
    zipped_quotes_author = zip([author.text for author in authors],
                               [translater(quote.text) for quote in quotes])
    # Вывод цитат и их аторов на странице
    for author, quote in zipped_quotes_author:
        print(quote, f'©️{author}', '\n', sep='\n')
