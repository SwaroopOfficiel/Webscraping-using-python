import requests
from bs4 import BeautifulSoup
import smtplib


url="https://www.amazon.in/Think-Like-Monk-Jay-Shetty/dp/0008386595/ref=sr_1_2?crid=1HZ1CIU2BYY4G&dchild=1&keywords=think+like+a+monk+by+jay+shetty&qid=1601193915&sprefix=think%2Caps%2C628&sr=8-2"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

 

def check_price():
    page= requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="soldByThirdParty").get_text()
    converted_price = float(price[3:-2])

    if converted_price < 350:
        send_mail()
        print(converted_price)
        print(title.strip())
        print("Email is sent")

    else:
        print(converted_price)
        print(title.strip())
        print("Email is not sent")


    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttIs()
        server.ehlo()


        server.login('vankarchaitanyaswaroop@gmail.com','')
        subject = "price is afforable"
        body = "Buy now", "https://www.amazon.in/Think-Like-Monk-Jay-Shetty/dp/0008386595/ref=sr_1_2?crid=1HZ1CIU2BYY4G&dchild=1&keywords=think+like+a+monk+by+jay+shetty&qid=1601193915&sprefix=think%2Caps%2C628&sr=8-2"

        msg = f"subject: {subject}\n\n{body}"

        server.sendmail(
            "vankarchaitanyaswaroop@gmail.com",
            "vankarchaitanyaswaroop@gmail.com",
            msg
            )
check_price()
