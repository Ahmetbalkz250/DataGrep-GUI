# 🔍 OmniSearch: Dynamic Data Search Engine
OmniSearch is an event-driven desktop search engine that allows you to perform instant, real-time searches across massive datasets (Excel, CSV) and relational databases (SQLite).

Instead of using clunky database viewers or slow spreadsheet software, it loads the data directly into RAM (Pandas DataFrame). Each time the user presses a key (`<KeyRelease>`), it instantly filters across all rows and columns like Chrome's CTRL+F logic

## 🚀 Key Features

* **Real-Time Search (Dynamic Triggering):** The search is not triggered by a button click; it filters the data instantly with every keystroke.
* **Multi-Format Support:** It can read flat files like `.csv` and `.xlsx`, as well as `.db` and `.sqlite` databases. The system automatically detects tables via `sqlite_master` when database is connected.
* **Performance Optimization:** To prevent user interface (GUI) freezing, only the first 100 rows of filtred results are displayed on screen (Treeview). No data is lost in the backgraund.
* **Modern Interface:** It offers minimalist and user-friendly experience with dark mode from CustomTkinter 

## 🛠️ Tech Stack

* **Python 3.x**
* **CustomTkinter:** For modern, sleek UI design.
* **Pandas:** For in-memory data manipulation and high-speed filtering.
* **SQLite3:** Built-in database connection and querying.

---

## 💻 Installation & Setup

To run the project from the source code on your local machine, first install required library:

```bash
pip install -r requirements.txt
```

(Note: If requirements.txt is missing, you can install the core libraries using pip install customtkinter pandas openpyxl)

Then, execute the main script:
```bash
python main.py
```

## 📖 How to Use?
* Click the "Select a File" button on the left menu when application is opened.

* Select the file you want to inspect (.csv, .xlsx, veya .db) from your computer.

* The first 100 rows of table will appear on the right panel when file is loaded.

* Begin typing text or number you want to filter in the search bar at the bottom. Table updates automatically across all columns as you typing (case-insensitive).

## 📦 Converting to a Desktop Application (EXE)
If you want to run this program on any Windows standalone PC without Python, you can convert a single-click .exe file.
* Install PyInstaller: Open your terminal and run the following command:
```bash
pip install pyinstaller
```
* Create EXE File: Open the terminal inside your project directory and run following command:
```bash
pyinstaller --noconsole --onefile main.py
```
Note: The --noconsole parameter prevents the CMD window from opening. Only user interface (GUI) is appeared.
* Run the Program: A new folder named "dist" will be created when the process finishes. You can use the "main.exe" file in this folder as you desire, or even you copy this file to any location you want.
