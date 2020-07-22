# -*- coding: utf-8 -*-
# Created on Wed Jul 22 19:35:09 2020
# 
# Copyright 2020 Jordi Corbilla. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import requests
import os
import random
import string
from bs4 import BeautifulSoup

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
    
chars = string.ascii_letters + string.digits + '!()@$^&*[]'
random.seed = (os.urandom(1024))

for name in list_names:
    extra_digits = ''.join(random.choice(string.digits))
    extra_chars = ''.join(random.choice(chars) for i in range(8))
    username = name.get_text().lower() + extra_digits + extra_chars
    print(username)
    
