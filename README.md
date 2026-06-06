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
