import pandas as pd 

veri=pd.read_excel("C:\\Users\\Dell\\Desktop\\Phyton Projeler\\doviz_veri_calismasi\\2000_2024_dolar_ verileri.xlsx")

tarih_sutunu = 'Tarih'
veri[tarih_sutunu] = pd.to_datetime(veri[tarih_sutunu])

girilen_tarih = input("aradiginiz tarihi (yyyy-mm-gg) formatında giriniz: ") 
sonuc = veri[veri[tarih_sutunu] == girilen_tarih]

if not sonuc.empty:
  print(sonuc)
else:
  print(f'{girilen_tarih} tarih gösterilememektedir. Lütfen bilgileri kontrol ediniz')