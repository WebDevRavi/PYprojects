import qrcode
img = qrcode.make('https://www.youtube.com/')
type(img)
img.save("some_file.png")