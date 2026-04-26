import qrcode
import os

base_url = "https://coastal-weather-teller.vercel.app"

locations = [
    "kanyakumari",
    "muttom",
    "sothavilai",
    "vivekananda",
    "thengapattinam"
]

output_folder = "static"
os.makedirs(output_folder, exist_ok=True)

for place in locations:
    url = f"{base_url}/{place}"
    img = qrcode.make(url)
    img.save(os.path.join(output_folder, f"{place}_qr.png"))
    print(f"{place}_qr.png generated successfully!")