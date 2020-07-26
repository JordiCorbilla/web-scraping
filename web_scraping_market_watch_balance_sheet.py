# -*- coding: utf-8 -*-
# Created on Sat Jul 25 09:49:41 2020
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
import pandas as pd

ticker = 'tsla'

# Download Balance Sheet table from TSLA
url = 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/balance-sheet'
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, 'html.parser')

main_content = soup.find_all('table', class_='crDataTable')
for table in main_content:
    rows = table.find_all("tr")
    for row in rows:
        print(row.get_text(separator='|').split('|')[1])
        print(row.get_text(separator='|').split('|')[6])
        cells = row.find_all("td")
        #for cell in cells:
            #print(cell.get_text())
