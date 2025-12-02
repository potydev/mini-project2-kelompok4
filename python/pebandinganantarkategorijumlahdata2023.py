import pandas as pd
import matplotlib.pyplot as plt

# Baca file
file_path = "data/data-violent-sexual-crime.xlsx"
df = pd.read_excel(file_path, skiprows=2)

# --- Perbaikan penting: Hapus spasi pada nama kolom ---
df.columns = df.columns.str.strip()

# Cek nama kolom
print("Kolom setelah diperbaiki:", df.columns)

# Ubah nama kolom agar seragam
df.columns = ['Iso3_code', 'Country', 'Region', 'Category', 'Sex', 'Year', 'VALUE']

# Filter data untuk tahun 2023
df_2023 = df[df['Year'] == 2023]

# Kategori seksual
sexual_crime_categories = [
    'Sexual violence',
    'Rape',
    'Sexual assault',
    'Sexual exploitation of children and trafficking for sexual exploitation',
    'Procuration and pimping',
    'Sexual violence: Total',
    'Rape: Total',
    'Sexual violence: Sexual assault',
    'Sexual violence: Sexual exploitation',
    'Sexual violence: Rape',
    'Sexual exploitation of children'
]

# Filter kategori
df_sexual_2023 = df_2023[df_2023['Category'].isin(sexual_crime_categories)]

# Total kasus per kategori
category_totals = df_sexual_2023.groupby('Category')['VALUE'].sum().reset_index()

# Urutkan
category_totals = category_totals.sort_values('VALUE', ascending=False)

# Pie Chart
plt.figure(figsize=(12, 10))
plt.pie(
    category_totals['VALUE'],
    labels=category_totals['Category'],
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Proporsi Kasus Seksual per Kategori (2023)")
plt.tight_layout()
plt.savefig('perbandingan antar Kategori.png')
plt.show()
