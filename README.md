# FiveExamplePythonProject_FromBroCode
 
Python Tkinter Uygulamaları
Bu depo, Python'un Tkinter kütüphanesini kullanarak oluşturduğum beş farklı uygulamayı içermektedir. Bu projeler, Hesap Makinesi, Saat, Mail Gönderme, Yılan Oyunu ve Tic Tac Toe oyunundan oluşmaktadır. Kod örneklerini Bro Code videolarını inceleyerek oluşturduğumu belirtmek isterim.

İçindekiler
Özellikler
Uygulama Açıklamaları
Kurulum
Kullanım
Katkıda Bulunma
Lisans
Özellikler
Hesap Makinesi: Temel matematiksel işlemleri gerçekleştiren bir hesap makinesi.
Saat: Gerçek zamanlı olarak saat ve tarih bilgilerini gösteren bir saat uygulaması.
Mail Gönderme: Kullanıcıların e-posta göndermesini sağlayan basit bir arayüz.
Yılan Oyunu: Klasik yılan oyununun Tkinter ile yeniden oluşturulmuş versiyonu.
Tic Tac Toe: İki oyunculu strateji oyunu olan Tic Tac Toe'nun Tkinter ile yazılmış hali.
Uygulama Açıklamaları
1. Hesap Makinesi
Bu uygulama, temel aritmetik işlemleri (toplama, çıkarma, çarpma, bölme) gerçekleştiren bir hesap makinesidir. Kullanıcı, arayüzdeki butonlar yardımıyla işlemlerini gerçekleştirebilir ve sonucu anında görebilir.

2. Saat
Bu uygulama, gerçek zamanlı olarak saat ve tarih bilgilerini gösterir. Tkinter arayüzü ile oluşturulan saat, sistem saati ile senkronize çalışarak güncel bilgileri kullanıcıya sunar.

3. Mail Gönderme
Bu uygulama, kullanıcıların basit bir arayüz aracılığıyla e-posta göndermelerini sağlar. Kullanıcı, göndermek istediği e-postanın alıcısını, konusunu ve içeriğini girerek hızlı bir şekilde mail gönderme işlemi gerçekleştirebilir.

4. Yılan Oyunu
Klasik yılan oyununun Tkinter ile yeniden oluşturulmuş versiyonudur. Oyuncu, klavye ok tuşları yardımıyla yılanı kontrol ederek yiyecekleri toplar ve yılanın büyümesini sağlar. Yılan duvara veya kendi gövdesine çarptığında oyun sona erer.

5. Tic Tac Toe
İki oyunculu strateji oyunu olan Tic Tac Toe'nun Tkinter ile yazılmış hali. Oyuncular sırasıyla "X" ve "O" işaretlerini 3x3'lük bir ızgaraya yerleştirirler. Amaç, yatay, dikey veya çaprazda üçlü bir sıra oluşturmaktır.

Kurulum
Bu projeleri çalıştırmak için aşağıdaki adımları izleyin:

Python'u İndirin ve Kurun: Proje Python 3 gerektirir. Python web sitesinden en son sürümü indirin ve kurun.

Proje Dosyalarını İndirin: Bu projeyi kendi bilgisayarınıza klonlayın veya indirin.
git clone https://github.com/kullanici_adiniz/tkinter-uygulamalari.git

Gerekli Kütüphaneleri Kurun: Tkinter Python'un standart kütüphanesi olarak gelir, ancak mail gönderme uygulaması için smtplib ve diğer gerekli kütüphaneleri kurmanız gerekebilir. Aşağıdaki komutu kullanarak gerekli kütüphaneleri kurun:
pip install tk
pip install smtplib
