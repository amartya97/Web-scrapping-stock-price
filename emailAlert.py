import smtplib

mailObject = smtplib.SMTP("smtp.gmail.com",587)

mailObject.starttls()

mailObject.login("pythonautomation02@gmail.com","pythonautomation1234")

subject="Stock Price"
body="Current stock price : 1234"
message="Subject:{}\n\n{}".format(subject,body)

mailObject.sendmail("pythonautomation02@gmail.com", "amartya0936@gmail.com",message)