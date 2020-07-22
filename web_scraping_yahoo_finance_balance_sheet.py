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

main_content = soup.find_all('div', class_='W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)')
for div in main_content:
    #print(div)
    sub_div = div.find_all('div', class_='D(tbc) Ta(start) Pend(15px)--mv2 Pend(10px) Bxz(bb) Py(8px) Bdends(s) Bdbs(s) Bdstarts(s) Bdstartw(1px) Bdbw(1px) Bdendw(1px) Bdc($seperatorColor) Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pstart(15px)--mv2 Pstart(10px)')
    for sub in sub_div:
        print(sub.get_text())