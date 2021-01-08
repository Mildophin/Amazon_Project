import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.fr/Sony-Appareil-orientable-directionnel-Capsules/dp/B088S2CNFC/ref=sr_1_9?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=appareil+photo+cher&qid=1610059161&sr=8-9"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if(converted_price < 799):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 799):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('viricel.milan@gmail.com', 'lkuylutbikvndcvi')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "viricel.milan@gmail.com",
        "test@gmail.com",
        msg
    )
    print("Email envoyé !")

    server.quit()


while(True):
    check_price()
    time.sleep(500 * 60)
