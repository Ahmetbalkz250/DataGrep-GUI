import customtkinter as ctk
from tkinter import ttk, filedialog
import pandas as pd
import sqlite3

class DataSearchEngine(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dinamik Veri Arama Motoru")
        self.geometry("1000x600")

        # Orijinal veriyi hafızada tutacağımız değişken
        self.df = None

        # --- 1. ARAYÜZ TASARIMI (GUI) ---

        # Sol Menü (Dosya Seçimi İçin)
        self.left_frame = ctk.CTkFrame(self, width=200)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.btn_load = ctk.CTkButton(self.left_frame, text="Select a file", command=self.load_file)
        self.btn_load.pack(pady=20, padx=20)

        # Sağ Alan (Tablo ve Arama Motoru)
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Tablo Alanı (CustomTkinter'da kendi tablosu olmadığı için klasik ttk.Treeview kullanıyoruz)
        self.tree = ttk.Treeview(self.right_frame)
        self.tree.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Arama Kutusu (En alta yerleştiriyoruz)
        self.search_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Search on dataset...", width=400)
        self.search_entry.pack(side="bottom", pady=20)

        # --- 2. DİNAMİK TETİKLEYİCİ (EVENT BINDING) ---
        # İşte üzerine konuştuğumuz o an! Klavyeden parmak kalktığı an 'dinamik_arama' fonksiyonu çalışır.
        self.search_entry.bind("<KeyRelease>", self.dinamik_arama)

    def load_file(self):
        # Kullanıcıya DB dosyalarını da seçebileceğini söylüyoruz
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel Dosyaları", "*.xlsx"), ("CSV Dosyaları", "*.csv"),
                       ("SQLite Veritabanı", "*.db *.sqlite")]
        )
        if not filepath:
            return

        try:
            # 1. EXCEL VE CSV DURUMU
            if filepath.endswith('.csv'):
                self.df = pd.read_csv(filepath)
            elif filepath.endswith('.xlsx'):
                self.df = pd.read_excel(filepath)

            # 2. SQLITE VERİTABANI DURUMU (SENİN İSTEDİĞİN VİZYON)
            elif filepath.endswith('.db') or filepath.endswith('.sqlite'):
                # Veritabanı ile köprü (Connection) kuruyoruz
                conn = sqlite3.connect(filepath)

                # Veritabanının kalbine (sqlite_master) inip tablo isimlerini çekiyoruz
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()  # Örn: [('Musteriler',), ('Siparisler',)]

                if not tables:
                    print("Veritabanında hiçbir tablo bulunamadı!")
                    conn.close()  # Kapıyı kapatmadan çıkmak amatörlüktür
                    return

                # Şimdilik otomatik olarak ilk sıradaki tabloyu seçiyoruz
                first_table_name = tables[0][0]
                print(f"Sistem Bilgisi: Veritabanı bağlandı. '{first_table_name}' tablosu okunuyor...")

                # Pandas'a SQL sorgumuzu ve köprümüzü veriyoruz, o hallediyor
                query = f"SELECT * FROM {first_table_name}"
                self.df = pd.read_sql_query(query, conn)

                # Köprüyü yıkıyoruz (Hafıza sızıntısı olmasın diye)
                conn.close()

            # Verileri metne çevirip tablomuzu güncelliyoruz (Eski kodla aynı)
            self.df = self.df.astype(str)
            self.tabloyu_guncelle(self.df.head(100))

        except Exception as e:
            print("Dosya okunurken bir hata oluştu:", e)

    def tabloyu_guncelle(self, gosterilecek_df):
        # Önce tabloda eski kalan ne varsa temizliyoruz
        self.tree.delete(*self.tree.get_children())

        if gosterilecek_df is None or gosterilecek_df.empty:
            return

        # Sütun başlıklarını dinamik olarak Pandas'tan alıp Treeview'a ekliyoruz
        self.tree["column"] = list(gosterilecek_df.columns)
        self.tree["show"] = "headings"

        for col in self.tree["column"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # DataFrame içindeki verileri listeye çevirip satır satır tabloya basıyoruz
        df_rows = gosterilecek_df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)

    def dinamik_arama(self, event):
        # EĞER DOSYA YÜKLENMEDİYSE ARAMA YAPMA
        if self.df is None:
            return

            # Kutudaki yazıyı alıp, büyük-küçük harf duyarlılığını kaldırmak için küçültüyoruz
        aranan_kelime = self.search_entry.get().lower()

        # Eğer kullanıcı kutuyu tamamen sildiyse (kutu boşsa) orijinal verinin ilk 100 satırını geri getir
        if aranan_kelime == "":
            self.tabloyu_guncelle(self.df.head(100))
            return

        # --- PANDAS BÜYÜSÜ BURADA BAŞLIYOR ---
        # Tüm satırlarda ve sütunlarda aradığımız kelimeyi (sayı veya metin fark etmez) tarıyoruz.
        maske = self.df.apply(lambda row: row.astype(str).str.lower().str.contains(aranan_kelime).any(), axis=1)

        # Sadece eşleşen satırları alıyoruz
        filtrelenmis_df = self.df[maske]

        # Filtrelenmiş sonucun ilk 100 satırını tabloya gönderip güncelliyoruz
        self.tabloyu_guncelle(filtrelenmis_df.head(100))


if __name__ == "__main__":
    app = DataSearchEngine()
    app.mainloop()