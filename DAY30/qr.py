import qrcode

link = qrcode.make("https://nikhil-dev.onrender.com/")

link.save("first.png")

print("Qrcode generation is successful")
