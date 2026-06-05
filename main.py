import customtkinter as ctk
from tkinter import ttk, filedialog
import pandas as pd
import sqlite3


class DataSearchEngine(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Data Search Engine")
        self.geometry("1000x600")

        # Store the original data in memory
        self.df = None

        # --- GUI SETUP ---
        self.left_frame = ctk.CTkFrame(self, width=200)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.btn_load = ctk.CTkButton(self.left_frame, text="Select a file", command=self.load_file)
        self.btn_load.pack(pady=20, padx=20)

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Treeview for displaying data
        self.tree = ttk.Treeview(self.right_frame)
        self.tree.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Search on dataset...", width=400)
        self.search_entry.pack(side="bottom", pady=20)

        # --- EVENT BINDING ---
        # Trigger dynamic search on key release
        self.search_entry.bind("<KeyRelease>", self.dynamic_search)

    def load_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"),
                       ("SQLite Database", "*.db *.sqlite")]
        )
        if not filepath:
            return

        try:
            # 1. EXCEL & CSV
            if filepath.endswith('.csv'):
                self.df = pd.read_csv(filepath)
            elif filepath.endswith('.xlsx'):
                self.df = pd.read_excel(filepath)

            # 2. SQLITE DATABASE
            elif filepath.endswith(('.db', '.sqlite')):
                conn = sqlite3.connect(filepath)
                cursor = conn.cursor()

                # Fetch table names from sqlite_master
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()

                if not tables:
                    print("No tables found in the database!")
                    conn.close()
                    return

                # Auto-select the first table
                first_table_name = tables[0][0]
                print(f"System Info: Database connected. Reading table '{first_table_name}'...")

                # Load table into DataFrame
                query = f"SELECT * FROM {first_table_name}"
                self.df = pd.read_sql_query(query, conn)
                conn.close()

            # Convert all data to string for consistent search capabilities
            self.df = self.df.astype(str)
            self.update_table(self.df.head(100))

        except Exception as e:
            print("An error occurred while reading the file:", e)

    def update_table(self, display_df):
        # Clear existing data in Treeview
        self.tree.delete(*self.tree.get_children())

        if display_df is None or display_df.empty:
            return

        # Setup dynamic columns
        self.tree["column"] = list(display_df.columns)
        self.tree["show"] = "headings"

        for col in self.tree["column"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # Insert rows
        df_rows = display_df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)

    def dynamic_search(self, event):
        # Abort if no file is loaded
        if self.df is None:
            return

        search_term = self.search_entry.get().lower()

        # Reset to first 100 rows if search is empty
        if search_term == "":
            self.update_table(self.df.head(100))
            return

        # Search across all columns (case-insensitive)
        mask = self.df.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)
        filtered_df = self.df[mask]

        # Update table with top 100 matched rows
        self.update_table(filtered_df.head(100))


if __name__ == "__main__":
    app = DataSearchEngine()
    app.mainloop()