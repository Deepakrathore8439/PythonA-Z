import qrcode as qr
img = qr.make("https://www.mycamu.co.in/")
img.save("mycamu.png") 