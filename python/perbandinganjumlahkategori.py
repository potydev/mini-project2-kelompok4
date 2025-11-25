import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap

FILE_PATH = "data/data-violent-sexual-crime.xlsx"

# Membaca dataset dari file
df = pd.read_excel(FILE_PATH, skiprows=2)

# Mengambil 7 kolom pertama dan mengganti nama kolom
df = df.iloc[:, :7]
df.columns = ['Iso3_code', 'Country', 'Region', 'Category', 'Sex', 'Year', 'VALUE']

# Membersihkan data: menghapus baris kosong dan mengubah VALUE menjadi angka
df.dropna(subset=['Category', 'VALUE'], inplace=True)
df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
df.dropna(subset=['VALUE'], inplace=True)

# Menghitung total korban per kategori dan mengambil 5 kategori tertinggi
category_totals = df.groupby('Category')['VALUE'].sum().sort_values(ascending=False).head(5)

# Mengubah angka korban menjadi satuan "juta" dan membulatkan
values_million = (category_totals / 1_000_000).round(0)
labels = values_million.index.tolist()

# Membuat teks kategori agar tidak menumpuk (dipotong menjadi beberapa baris)
wrapped_labels = [ "\n".join(textwrap.wrap(label, width=18)) for label in labels ]

# Membuat grafik batang
plt.figure(figsize=(16, 9))
bars = plt.bar(wrapped_labels, values_million.values, color='pink')

# Judul grafik
plt.title("Perbandingan jumlah kategori kejahatan terbanyak top 5 (2003 - 2023) ", fontsize=20, pad=20)

# Label sumbu X dan Y
plt.xlabel("Kategori Kejahatan", fontsize=14)
plt.ylabel("Jumlah Korban", fontsize=14)

# Menambahkan garis bantu horizontal
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Menampilkan angka di atas masing-masing batang
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        f"{int(height)} Juta",
        ha='center',
        fontsize=14
    )

# Pastikan tulisan kategori datar (tidak miring)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()