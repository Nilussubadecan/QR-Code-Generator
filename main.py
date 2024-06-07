import qrcode

# QR kodunu oluşturmak istediğiniz URL
url = input("Enter URL:")

# QR kodu oluştur
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# URL'yi QR koduna ekle
qr.add_data(url)
qr.make(fit=True)

# QR kodunu bir görüntü olarak oluştur
img = qr.make_image(fill='black', back_color='white')

# QR kodunu bir dosya olarak kaydet
img.save("qrcode.png")

print("QR kodu başarıyla oluşturuldu ve 'qrcode.png' dosyasına kaydedildi.")
