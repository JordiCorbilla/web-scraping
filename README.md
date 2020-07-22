# Web scraping

Web scraping scripts to extract financial data. In a nutshell, this method can help you to get any information that it's available on any website using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library and python. The idea is to use this library to parse any DOM and get the data that we are interested in. Getting data from a list for example is a very simple job. Things get more interesting when we want to download more complex data like a table.

## 1) Installing BautifulSoup

```cmd
pip install beautifulsoup4
Requirement already satisfied: beautifulsoup4 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (4.9.1)
Requirement already satisfied: soupsieve>1.2 in c:\users\thund\anaconda3\envs\quant\lib\site-packages (from beautifulsoup4) (2.0.1)
```


## 2) Simple Example

The following script example tries to generate random user names via web scraping. Firstly, we locate a website that contains a list of name that we can download and then we use this list to generate user names. To do this, we can browse for any of the top 1000 girl names and see any of the links available:

In our case, we found [this](https://family.disney.com/articles/1000-most-popular-girl-names/) url which seems pretty good for what we need. Upon inspecting the names, we can see that the DOM is pretty straightforward and each name is placed under 'li' tags and the whole group under an 'ol' tag:



## 3) Complex Example








