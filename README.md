# Web scraping

Web scraping scripts to extract financial data. In a nutshell, this method can help you to get any information that it's available on any website using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library and python. The idea is to use this library to parse any DOM and get the data that we are interested in. Getting data from a list for example is a very simple job. Things get more interesting when we want to download more complex data like a table.

## 1) Installing BeautifulSoup

```cmd
pip install beautifulsoup4
```

## 2) Simple Example

The following script example tries to generate random user names via web scraping. Firstly, we locate a website that contains a list of name that we can download and then we use this list to generate user names. To do this, we can browse for any of the top 1000 girl names and see any of the links available:

In our case, we found [this](https://family.disney.com/articles/1000-most-popular-girl-names/) url which seems pretty good for what we need. Upon inspecting the names, we can see that the DOM is pretty straightforward and each name is placed under 'li' tags and the whole group under an 'ol' tag:

![](https://github.com/JordiCorbilla/web-scraping/raw/master/baby-names.png)

To get the list of names on a usable format using python, we can use the BeautifulSoup library and locate the specific tags we want (ol and then li, and print the content of it). The code below shows how this can be done:

```python
# Let's create a random user name generator using web scraping.
# first we need to download a list of names to work on.
# the following url contains 1000 girl names and we will download them using web scraping.
url = 'https://family.disney.com/articles/1000-most-popular-girl-names/'
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, 'html.parser')

# Find the first 'ol' that contains the list of items
list = soup.find('ol')
# Each name in the list is stored under a 'li' item
list_names = list.find_all('li')
# Now print all the names that we have scraped from the web site
for name in list_names:
    print(name.get_text())
```

![](https://github.com/JordiCorbilla/web-scraping/raw/master/list-names-scraping.png)

With a little tweak, we can easily generate usernames based on this data or whatever you want to do with it.

```python
# Generate the following sequence 
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()@$^&*[]
chars = string.ascii_letters + string.digits + '!()@$^&*[]'
random.seed = (os.urandom(1024))

for name in list_names:
    extra_digits = ''.join(random.choice(string.digits))
    extra_chars = ''.join(random.choice(chars) for i in range(8))
    username = name.get_text().lower() + extra_digits + extra_chars
    print(username)
```

![](https://github.com/JordiCorbilla/web-scraping/raw/master/list-usernames-scraping.png)

## 3) Complex Example

One of the most interesting uses for this technology is the ability to download larges amounts of data that are table based. This example tries to download the balance sheet from one of the stocks in Yahoo Finance. Imagine that we want to download the balance sheet of TSLA (if you want to download the data, you need to become a premium subscriber and they have made it difficult to perform web scraping). To perform this operation, we need to look at the way the table is created (a bunch of div tags) and how each row is composed (classes, ids) so they are easily identifiable. 

Balance Sheet: https://www.marketwatch.com/investing/stock/tsla/financials/balance-sheet




