import re
import csv

with open('raw.txt', 'r', encoding='utf-8') as file:
    text = file.read()

binPattern = re.search(r'.*БИН.*\s*(\d{12})', text)
bin = binPattern.group(1) if binPattern else "БИН не найден"
print(f"БИН: {bin}")

listPattern = re.findall(r'\d+\.\n(.+?)\n', text)
pricePattern = re.findall(r'Стоимость\n(.+?)\n', text)

csvFilename = "receipt.csv"
with open(csvFilename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Название", "Цена (KZT)"])

    for item, price in zip(listPattern, pricePattern):
        writer.writerow([item, price])

