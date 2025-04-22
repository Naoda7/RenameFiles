import os
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

def rename_files():
    folder_path = entry_folder.get()
    base_name = entry_name.get().strip()
    custom_format = entry_custom.get()
    selected_format = numbering_format.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path.")
        return

    if not base_name:
        messagebox.showerror("Error", "New name cannot be empty.")
        return

    log_list.delete(0, tk.END)
    renamed_files = []

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(filename)
        counter = 0
        while True:
            suffix = ""
            if counter > 0:
                if selected_format == "(1)":
                    suffix = f"({counter})"
                elif selected_format == "_1":
                    suffix = f"_{counter}"
                elif selected_format == "custom":
                    suffix = f"{custom_format}{counter}"
            else:
                if selected_format == "custom":
                    suffix = f"{custom_format}"

            new_name = f"{base_name}{suffix}{ext}"
            new_path = os.path.join(folder_path, new_name)
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                renamed_files.append((filename, new_name, ext))
                break
            counter += 1

    # Urutkan berdasarkan ekstensi dan nama baru
    grouped = defaultdict(list)
    for old, new, ext in renamed_files:
        grouped[ext.lower()].append((old, new))

    for ext in sorted(grouped):
        sorted_group = sorted(grouped[ext], key=lambda x: x[1].lower())
        for old, new in sorted_group:
            log_list.insert(tk.END, f" {old} → {new}")

    messagebox.showinfo("Done", "Rename process completed!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_folder.config(state="normal")
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_selected)
        entry_folder.config(state="readonly")

def show_help():
    help_text = (
        "How to use FileRenom:\n\n"
        "- Put all the files you want to rename in one folder.\n"
        "- Click 'Select Folder' to choose your directory.\n"
        "- Type a new name in 'New Base Name'.\n"
        "- Choose the numbering format if needed.\n"
        "- If using custom format, type your suffix.\n\n"
        "Example:\nFile.jpg  → FileRenom.jpg\n"
        "File2.jpg → FileRenom (1).jpg\n\n"
        "Supported formats:\n"
        ".jpg, .jpeg, .png, .gif, .bmp, .tiff, .pdf, .doc, .docx,\n"
        ".xls, .xlsx, .txt, .mp3, .mp4, .avi, .zip, .rar, etc."
    )
    messagebox.showinfo("Usage Guide", help_text)

def toggle_custom_entry():
    entry_custom.config(state="normal" if numbering_format.get() == "custom" else "disabled")

# UI setup
root = tk.Tk()
root.iconbitmap("Icon.ico")
root.title("FileRenom")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="white")

default_font = ("Segoe UI", 10)

def styled_label(parent, text, pady=(10, 0)):
    return tk.Label(parent, text=text, font=default_font, bg="white").pack(pady=pady)

styled_label(root, "Select Folder:")
frame_folder = tk.Frame(root, bg="white")
frame_folder.pack(pady=5)

entry_folder = tk.Entry(frame_folder, width=35, font=default_font, state="readonly")
entry_folder.pack(side=tk.LEFT, padx=(0, 5))

tk.Button(frame_folder, text="Browse", command=browse_folder, font=default_font, bg="black", fg="white").pack(side=tk.LEFT, padx=(0, 10))

help_btn = tk.Button(frame_folder, text="?", command=show_help, bg="#f7fbff", fg="black",
                     font=("Segoe UI", 10, "bold"), width=2, height=1, relief="flat")
help_btn.pack(side=tk.LEFT)

styled_label(root, "New Base Name:")
entry_name = tk.Entry(root, width=40, font=default_font)
entry_name.pack(pady=5)

styled_label(root, "Numbering Format:")
numbering_format = tk.StringVar(value="(1)")
frame_radio = tk.Frame(root, bg="white")
frame_radio.pack(pady=5)

tk.Radiobutton(frame_radio, text="(1)", variable=numbering_format, value="(1)", command=toggle_custom_entry, font=default_font, bg="white").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="_1", variable=numbering_format, value="_1", command=toggle_custom_entry, font=default_font, bg="white").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="Custom", variable=numbering_format, value="custom", command=toggle_custom_entry, font=default_font, bg="white").pack(side=tk.LEFT, padx=10)

styled_label(root, "Custom Format Suffix (e.g., ' version_')")
entry_custom = tk.Entry(root, width=30, state="disabled", font=default_font)
entry_custom.insert(0, " custom_")
entry_custom.pack(pady=(0, 10))

tk.Button(root, text="Rename Files", command=rename_files, bg="black", fg="white", font=default_font, width=20).pack(pady=10)

styled_label(root, "Progress:")
frame_log = tk.Frame(root, bg="white")
frame_log.pack(pady=10, anchor="center")

log_scroll = tk.Scrollbar(frame_log)
log_scroll.pack(side=tk.RIGHT, fill=tk.Y)

log_list = tk.Listbox(frame_log, height=8, width=58, yscrollcommand=log_scroll.set,
                      selectbackground="#f0f0f0", font=("Consolas", 9), justify="left")
log_list.pack(side=tk.LEFT, fill=tk.BOTH)
log_scroll.config(command=log_list.yview)

def open_github():
    import webbrowser
    webbrowser.open_new("https://github.com/Naoda7")

# Tautan GitHub
github_link = tk.Label(root, text="Naoda7", fg="black", cursor="hand2", font=default_font, bg="white")
github_link.pack(pady=(5, 15))
github_link.bind("<Button-1>", lambda e: open_github())


root.mainloop()
