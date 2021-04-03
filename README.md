# Web scraping

Web scraping scripts to extract financial data. In a nutshell, this method can help you to get any information that it's available on any website using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library and python. The idea is to use this library to parse any DOM and get the data that we are interested in. Getting data from a list for example is a very simple job. Things get more interesting when we want to download more complex data like a table.

## 1) Installing BeautifulSoup

```cmd
pip install beautifulsoup4
or
python -m pip install beautifulsoup4
```

Output:

```bash
python -m pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.9.3-py3-none-any.whl (115 kB)
     |████████████████████████████████| 115 kB 3.3 MB/s
Collecting soupsieve>1.2; python_version >= "3.0"
  Downloading soupsieve-2.2-py3-none-any.whl (33 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.9.3 soupsieve-2.2
```

## 2) Simple Example (scraping names)

The following script example tries to generate random user names via web scraping. Firstly, we locate a website that contains a list of name that we can download and then we use this list to generate user names. To do this, we can browse for any of the top 1000 girl names and see any of the links available:

In our case, we found [this](https://family.disney.com/articles/1000-most-popular-girl-names/) url which seems pretty good for what we need. Upon inspecting the names, we can see that the DOM is pretty straightforward and each name is placed under 'li' tags and the whole group under an 'ol' tag:

![](baby-names.png)

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

![](list-names-scraping.png)

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

![](list-usernames-scraping.png)

## 3) Complex Example (scraping financial information)

One of the most interesting uses for this technology is the ability to download larges amounts of data that are table based. This example tries to download the balance sheet from one of the stocks in Yahoo Finance. Imagine that we want to download the balance sheet of TSLA (if you want to download the data, you need to become a premium subscriber and they have made it difficult to perform web scraping). To perform this operation, we need to look at the way the table is created (a bunch of div tags) and how each row is composed (classes, ids) so they are easily identifiable. 

Balance Sheet: https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA&_guc_consent_skip=1596652371

![](balancesheet.png)

```python
import requests
from bs4 import BeautifulSoup

# Download Balance Sheet table from TSLA
url = 'https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA'
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, 'html.parser')

cash_balance = {}

# Search for the main DIV that encloses the balance sheet table
main_content = soup.find_all('div', class_='M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)')
for div in main_content:
    # Look for each DIV that encloses every single row
    sub_div = div.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    for sub in sub_div:
        # Select the first column as the index of our dictionary and select the second column as the data to store (2019)
        cash_balance[sub.get_text(separator="|").split("|")[0]] = sub.get_text(separator="|").split("|")[1]
        #print(sub.get_text())
```

The final result of the execution of the code above lets us produce the desired output, scraping the data from the Yahoo Finance page for the TSLA ticker:

![](balancesheetdictionary.png)

# Containeraizing the script

In order to make the script easily deployable, we'll create a Flask service that will host the retrieval of the cash balances and it will be all contained into a docker image. 

## Create the Flask service

```python
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
server = Flask(__name__)

@server.route("/")
def cash_balance_get():
     # Download Balance Sheet table from TSLA
    url = 'https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA'
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    
    cash_balance = {}
    
    # Search for the main DIV that encloses the balance sheet table
    main_content = soup.find_all('div', class_='M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)')
    for div in main_content:
        # Look for each DIV that encloses every single row
        sub_div = div.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
        for sub in sub_div:
            # Select the first column as the index of our dictionary and select the second column as the data to store (2019)
            cash_balance[sub.get_text(separator="|").split("|")[0]] = sub.get_text(separator="|").split("|")[1]
            #print(sub.get_text())
            
    return jsonify(cash_balance)

if __name__ == "__main__":
   server.run(host='0.0.0.0')
```

If we run this code and try to get to `http://localhost:500`, we'll get the following response:

```json
{"Capital Lease Obligations":"1,540,000","Common Stock Equity":"22,225,000","Invested Capital":"33,964,000","Net Debt":"-","Net Tangible Assets":"21,705,000","Ordinary Shares Number":"960,000","Share Issued":"960,000","Tangible Book Value":"21,705,000","Total Assets":"52,148,000","Total Capitalization":"31,832,000","Total Debt":"13,279,000","Total Equity Gross Minority Interest":"23,075,000","Total Liabilities Net Minority Interest":"29,073,000","Working Capital":"12,469,000"}
```

The output of the execution can be seen below:

```bash
runfile('C:/Users/thund/Source/Repos/web-scraping/web_scraping_yahoo_finance_balance_sheet_server.py', wdir='C:/Users/thund/Source/Repos/web-scraping')
 * Serving Flask app "web_scraping_yahoo_finance_balance_sheet_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [03/Apr/2021 16:00:03] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Apr/2021 16:00:03] "GET /favicon.ico HTTP/1.1" 404 -
```

