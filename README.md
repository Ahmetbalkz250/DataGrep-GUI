# 🔍 OmniSearch: Dinamik Veri Arama Motoru

OmniSearch, devasa veri setleri (Excel, CSV) ve ilişkisel veritabanları (SQLite) üzerinde saniyeler içinde anlık arama yapmanızı sağlayan, olay yönelimli (event-driven) bir masaüstü arama motorudur. 

Hantal veritabanı görüntüleyicileri veya yavaş e-tablo programları yerine; veriyi doğrudan RAM'e (Pandas DataFrame) alarak, kullanıcı klavyeye her dokunduğunda (`<KeyRelease>`) tüm sütunlarda ve satırlarda anlık filtreleme (Ctrl+F mantığı) yapar.

## 🚀 Öne Çıkan Özellikler

* **Dinamik Tetikleme (Real-Time Search):** Arama işlemi bir butona basarak değil, arama kutusuna yazılan her harfte anlık olarak gerçekleşir.
* **Çoklu Format Desteği:** `.csv` ve `.xlsx` gibi düz dosyaların yanı sıra, `.db` ve `.sqlite` veritabanı dosyalarını okuyabilir. Veritabanı bağlandığında sistem `sqlite_master` üzerinden tabloları otomatik tespit eder.
* **Performans Optimizasyonu:** Kullanıcı arayüzünün (GUI) donmasını engellemek için, filtrelenen sonuçların yalnızca ilk 100 satırı (head) ekrana (Treeview) render edilir. Arka planda veri kaybı yaşanmaz.
* **Modern Arayüz:** CustomTkinter altyapısı ile karanlık mod (dark mode) destekli, minimalist ve kullanıcı dostu bir deneyim sunar.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **CustomTkinter:** Modern arayüz tasarımı.
* **Pandas:** Bellek içi (in-memory) veri manipülasyonu ve hızlı filtreleme.
* **SQLite3:** Veritabanı bağlantısı ve sorgulama (Built-in).

---

## 💻 Kurulum ve Çalıştırma (Geliştiriciler İçin)

Projeyi kendi bilgisayarınızda (local machine) kaynak kodundan çalıştırmak için öncelikle gerekli kütüphaneleri kurun:

```bash
pip install -r requirements.txt
```

(Not: requirements.txt dosyası projede bulunmuyorsa pip install customtkinter pandas openpyxl komutu ile temel bağımlılıkları kurabilirsiniz.)

Ardından ana betiği (script) çalıştırın:
```bash
python main.py
```
## 📖 Nasıl Kullanılır?
* Uygulama açıldığında sol menüden "Select a file" butonuna tıklayın.

* Bilgisayarınızdan incelemek istediğiniz dosyayı seçin (.csv, .xlsx, veya .db).

* Veri yüklendiğinde tablonun ilk 100 satırı sağ ekranda belirecektir.

* Alt kısımdaki arama çubuğuna filtrelemek istediğiniz metni veya sayıyı yazmaya başlayın. Tablo, siz yazdıkça (büyük/küçük harf duyarlılığı olmadan) tüm sütunlarda otomatik olarak güncellenecektir.

## 📦 Masaüstü Uygulaması (EXE) Haline Getirme
Bu programı Python yüklü olmayan herhangi bir Windows bilgisayarda bağımsız (standalone) bir program gibi çalıştırmak isterseniz, tek tıklamalı bir .exe dosyasına dönüştürebilirsiniz.
* PyInstaller'ı Yükleyin: Terminalinizi açıp aşağıdaki komutu girin:
```bash
pip install pyinstaller
```
* EXE Dosyasını Oluşturun: Proje klasörünüzün içinde terminali açın ve şu komutu çalıştırın:
```bash
pyinstaller --noconsole --onefile main.py
```
Not: --noconsole parametresi (flag), program çalışırken arkada siyah CMD penceresinin açılmasını engeller, yalnızca modern arayüz (GUI) görünür.
* Programı Çalıştırın: İşlem bittiğinde proje klasörünüzde dist adında yeni bir klasör oluşacak. Bu klasörün içindeki main.exe dosyasını bilgisayarınızın herhangi bir konumuna taşıyıp kullanabilirsiniz.
