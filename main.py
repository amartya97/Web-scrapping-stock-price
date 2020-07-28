import sys
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

stockSymbol=input("Please enter the stock code to see the price : ")
modifiedSymbol=''
if(stockSymbol.find('NS')):
    #print("success")
    pass
else:
    modifiedSymbol+='%5E'
    #print(modifiedSymbol)

def fetch_NSE_stock_price():
    #stockSymbol=input("Please enter a stock code you want to fetch : ")
    #print(stockSymbol)
    stockUrl='https://in.finance.yahoo.com/quote/'+str(modifiedSymbol)+str(stockSymbol)+'?p=^'+str(stockSymbol)+'&.tsrc=fin-srch'
    print(stockUrl)
    response=requests.get(stockUrl)
    soup=BeautifulSoup(response.text,'html.parser')
    dataArray=soup.find(class_="My(6px) Pos(r) smartphone_Mt(6px)")
    stockValue=dataArray.text.split('+')
    return stockValue[0]


#data_file = open(stockSymbol+'_NSE_stock.csv','w') 


# iteration = 0
# while iteration < 2:
#     c_date = date.today().strftime("%B %d, %Y")
#     c_time = datetime.now().strftime("%H:%M:%S")
#     current_stock_price = fetch_NSE_stock_price()
#     print (stockSymbol + ',' + c_date + ','  + c_time + ',' + str(current_stock_price) )
#     print(stockSymbol + ',' + c_date + ','  + c_time + ',' + str(current_stock_price), file=data_file)
#     time.sleep(2)
#     iteration = iteration + 1



def writeInFIle():
    data_file = open(stockSymbol+'_NSE_stock.csv','w') 
    iteration = 0
    while iteration < 2:
        c_date = date.today().strftime("%B %d, %Y")
        c_time = datetime.now().strftime("%H:%M:%S")
        current_stock_price = fetch_NSE_stock_price()
        print (stockSymbol + ',' + c_date + ','  + c_time + ',' + str(current_stock_price) )
        print(stockSymbol + ',' + c_date + ','  + c_time + ',' + str(current_stock_price), file=data_file)
        time.sleep(2)
        iteration = iteration + 1
    data_file.close()
        

    
def sendEmail():
    mailObject = smtplib.SMTP("smtp.gmail.com",587)
    mailObject.starttls()
    mailObject.login("pythonautomation02@gmail.com","pythonautomation1234")

    fromAddr='pythonautomation02@gmail.com'
    toAddr='amartya0936@gmail.com'
    toCC='1602218@kiit.ac.in'

    finalStockPrice=fetch_NSE_stock_price()

    message=MIMEMultipart()
    message['From']=fromAddr
    message['To']=toAddr
    message['CC']=toCC
    message['Subject']="Stock Price of : "+stockSymbol
    body="Current stock price : "+finalStockPrice
    message.attach(MIMEText(body,'plain'))

    text=message.as_string()
    mailObject.sendmail(fromAddr,toAddr,text)

    mailObject.quit()

writeInFIle()
sendEmail()
# #sending mail
# mailObject = smtplib.SMTP("smtp.gmail.com",587)
# mailObject.starttls()
# mailObject.login("pythonautomation02@gmail.com","pythonautomation1234")

# fromAddr='pythonautomation02@gmail.com'
# toAddr='amartya0936@gmail.com'
# toCC='1602218@kiit.ac.in,amartyaroy510@gmail.com'
# toAddrs=[toAddr]+toCC.split(',')

# finalStockPrice=fetch_NSE_stock_price()

# message=MIMEMultipart()
# message['From']=fromAddr
# message['To']=toAddr
# message['CC']=toCC
# message['Subject']="Stock Price of : "+stockSymbol
# body="Current stock price : "+finalStockPrice
# message.attach(MIMEText(body,'plain'))
# # #message="Subject:{}\n\n{}".format(subject,body)
# # message.attach(MIMEText(body,'plain'))

# # filename=open(stockSymbol+'_NSE_stock.csv','r')
# # part=MIMEBase('application','octet-stream')
# # part.set_payload(filename.read())
# # #encoders.encode_base64(part)
# # part.add_header('Content-Disposition','attachment',filname=filename)
# # message.attach(part)

# # filename=open(stockSymbol+'_NSE_stock.csv','r')
# # attachment=MIMEText(filename.readlines())
# # attachment.add_header('Content-Disposition','attachment',filname=filename)
# # message.attach(attachment)

# text=message.as_string()
# mailObject.sendmail(fromAddr,toAddr,text)

# mailObject.quit()