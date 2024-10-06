import pyqrcode

s = "https://www.instagram.com/blendi.kqiiku/"

url = pyqrcode.create(s)

url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=4)