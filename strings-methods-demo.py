website = 'http://www.ibrhmies.com'
konuAdi = "Python'da Strings Metotları Uygulama."

# 1-' Hello World ' karakter dizisinin başındaki ve sonundaki boşlukları silin.
#CEVAP
#sonuc = ' Hello World '.strip()
#print(sonuc)


#2-'www.ibrhmies.com' içindeki ibrhmies dışındaki her şeyi silin.
#CEVAP
#sonuc = website.strip('htp:/w..com')
#print(sonuc)


#3-'konuAdi' karakter dizisinin bütün karakterlerini küçük harf yapın.
#CEVAP
#sonuc = konuAdi.lower()
#print(sonuc)


#4-'website' içinde kaç tane i karakteri vardır.
#CEVAP
#sonuc = website.count('i')
#print(sonuc)


#5-'website' "www" ile başlayıp ".com" ile bitiyor mu?
#CEVAP
#sonuc = website.startswith('www')
#print(sonuc)
#sonuc = website.endswith('.com')
#print(sonuc)


#6-'website'  içinde '.com' ifadesi var mı?
#CEVAP
#sonuc = website.find('.com') find komutu bize aradığımız karakterin kaçıncı indexten itibaren başladığını söyler.
#print(sonuc)


#7-'konuAdi' içindeki karakterlerin hepsi alfabetik mi?
#CEVAP
#sonuc = konuAdi.isalpha() isalpha komutu değişkendeki karakterlerin hepsinin alfabede olup olmadığını kontrol eder true veya false olarak yanıtlar.
# isdigit komutu da değişkende bütün karakterler rakam mı bunu kontrol eder.
#print(sonuc)


#8-'contents' ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna * karakteri yerleştiriniz.
#CEVAP
#sonuc = 'contents'.center(50,'*') center komutunda kaç karakterlik satır olacaksa merkezine yazdığın kelimeyi yerleştirir boşluklara ne yazacağını da sen belirlersin.
#print(sonuc)


#9-'konuAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştir.
#CEVAP
#sonuc = konuAdi.split()
#sonuc = "-".join(sonuc)
#print(sonuc)


#10-'Hello World' karakter dizisindeki 'World' ü 'there' olarak değiştirin.
#CEVAP
#sonuc = 'Hello World'.replace('World','There')
#print(sonuc)


#11-'konuAdi' karakter dizisini boşluklardan ayır.
#CEVAP
#sonuc = konuAdi.split()
#print(sonuc)

