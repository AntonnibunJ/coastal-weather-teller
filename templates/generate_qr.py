import qrcode

# Your deployed website base URL
base_url = "https://yourwebsite.vercel.app"

# Coastal locations
locations = [
    "kanyakumari",
    "muttom",
    "sothavilai",
    "vivekananda",
    "thengapattinam"
]

# Generate QR codes
for place in locations:
    url = f"{base_url}/{place}"
    img = qrcode.make(url)
    img.save(f"{place}_qr.png")
    print(f"{place}_qr.png generated successfully!")