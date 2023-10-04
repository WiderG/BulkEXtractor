import tkinter as tk
from tkinter import filedialog
import zipfile
import rarfile

class FileExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("BulkEXtractor - Made by Wider")
        self.root.geometry("350x150")
        self.root.configure(bg="#36393f")

        self.button_bg = "#7289da"
        self.text_color = "#ffffff"
        self.files = ()

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Files", command=self.browse_files)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        options_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Clear Selection", command=self.clear_selection)
        options_menu.add_command(label="Extract to Subfolder", command=self.extract_to_subfolder)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="#36393f")
        frame.pack(expand=True, fill=tk.BOTH)

        browse_button = tk.Button(frame, text="Select Files", command=self.browse_files, bg=self.button_bg, fg=self.text_color, font=("Helvetica", 12))
        browse_button.pack(pady=10)

        extract_button = tk.Button(frame, text="Extract Files", command=self.extract_files, bg=self.button_bg, fg=self.text_color, font=("Helvetica", 12))
        extract_button.pack(pady=10)

        self.result_label = tk.Label(frame, text="", bg="#36393f", fg=self.text_color, font=("Helvetica", 12))
        self.result_label.pack()

        self.about_label = tk.Label(frame, text="", bg="#36393f", fg=self.text_color, font=("Helvetica", 12))
        self.about_label.pack()

    def browse_files(self):
        filetypes = (
            ("Zip files", "*.zip"),
            ("Rar files", "*.rar"),
            ("All files", "*.*")
        )
        self.files = filedialog.askopenfilenames(filetypes=filetypes)
        self.result_label.config(text="Files selected.")

    def extract_files(self):
        if self.files:
            destination_folder = filedialog.askdirectory()
            extracted_files = 0
            for file in self.files:
                if file.endswith('.zip'):
                    with zipfile.ZipFile(file, 'r') as zip_ref:
                        zip_ref.extractall(destination_folder)
                        extracted_files += len(zip_ref.namelist())
                elif file.endswith('.rar'):
                    with rarfile.RarFile(file, 'r') as rar_ref:
                        rar_ref.extractall(destination_folder)
                        extracted_files += len(rar_ref.namelist())
            self.result_label.config(text=f"Extraction completed. Total {extracted_files} files extracted.")
        else:
            self.result_label.config(text="No files selected.")

    def clear_selection(self):
        self.files = ()
        self.result_label.config(text="Selection cleared.")

    def extract_to_subfolder(self):
        # Add logic to extract to a subfolder within the destination folder
        pass

    def show_about(self):
        about_text = "BulkEXtractor\nVersion 1.0\nA simple tool to extract compressed files for games and such."
        self.about_label.config(text=about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExtractor(root)
    root.mainloop()
