import qrcode

features = qrcode.QRCode(version=1,box_size=20,border=2)

features.add_data("HI_BEWEB LEVEL 2 LEARNING")
features.make(fit=True)
generate = features.make_image(fill_color="black",back_color="white")
generate.save('pngwing1.png')
