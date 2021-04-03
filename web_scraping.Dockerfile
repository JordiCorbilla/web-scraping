# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY web_scraping_packages.txt .

# install dependencies
RUN pip install -r web_scraping_packages.txt

# copy the script to the working directory
COPY web_scraping_yahoo_finance_balance_sheet_server.py .

# command to run on container start
CMD [ "python", "./web_scraping_yahoo_finance_balance_sheet_server.py" ]