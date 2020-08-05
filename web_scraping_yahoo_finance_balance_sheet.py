# -*- coding: utf-8 -*-
# Created on Wed Jul 22 21:43:55 2020
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
from bs4 import BeautifulSoup

# Download Balance Sheet table from TSLA
url = 'https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA'
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, 'html.parser')

cash_balance = {}

main_content = soup.find_all('div', class_='M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)')
for div in main_content:
    #print(div)
    sub_div = div.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    for sub in sub_div:
        cash_balance[sub.get_text(separator="|").split("|")[0]] = sub.get_text(separator="|").split("|")[1]
        print(sub.get_text())
       
      