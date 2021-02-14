# check_gov_ua #check.gov.ua

API for state check receipt service

My version of Rest API for bank or other financial organisations to connect reciept check on state service check.gov.ua
Using Python3.7 and Django ver. 3.0

For update static do not forget use python3 manage.py collectstatic

##### API #####

You can run this service as standalone or as docker. In docker image I'm using PostgreSQL as DB and Nginx as web server. On my own it's working fine with it.

For productions deployment you need to create two (or more) separate .env files with environment variables for production and development use.

Actually you can use update endpoint for load receipts via API. For more flexibility you may setup permissions on your own. For example used an IP check, but you can setup permission as API_KEY or JWT and whatever you want.

#### RECEIPT SETTINGS ####

For creating a receipt, you need to:

1. Fill information about the Bank
2. Add images with signature and logo on admin page

Note! This version of reportlab supports .jpg files for creating pdf.
In creating pdf module, you can change template for receipt on your own. 

For support cyrillic I am using the DejaVuSerif font, but you can add another one.

It's just example. For more information check the documentation https://www.reportlab.com/docs/reportlab-userguide.pdf

##################
