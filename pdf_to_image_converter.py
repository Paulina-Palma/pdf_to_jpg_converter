from pdf2image import convert_from_path
from tkinter import messagebox, filedialog, ttk
import tkinter as tk
import os

# Define the path to the "extracted_images" folder on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "extracted_images")
if not os.path.exists(desktop_path):
    os.mkdir(desktop_path)


def pdf2img():
    try:
        pdf_path = e1.get()
        pages = convert_from_path(pdf_path)

        progress_bar["maximum"] = len(pages)  # Set the maximum value for the progress bar
        status_label.config(text="Converting...")  # Update the status label

        for i, page in enumerate(pages, start=1):
            page.save(os.path.join(desktop_path, f'page_{i}.jpg'), 'JPEG')
            progress_bar["value"] = i  # Update the progress bar
            master.update_idletasks()  # Refresh the GUI

    except Exception as e:
        result = f"Error: {e}"
        messagebox.showinfo("Result", result)
    else:
        result = "Conversion successful!"
        status_label.config(text=result)  # Update status to success
        messagebox.showinfo("Result", result)
    finally:
        progress_bar["value"] = 0  # Reset the progress bar


def browse():
    pdf_file = filedialog.askopenfilename(
        initialdir=os.path.expanduser("~"),
        title="Select PDF File",
        filetypes=[("PDF files", "*.pdf")]
    )
    e1.delete(0, tk.END)  # Clear the entry box
    e1.insert(0, pdf_file)  # Insert selected file path


# Set up the main window
master = tk.Tk()
master.title("PDF to Image Converter")

# Widgets
tk.Label(master, text="File Location").grid(row=0, column=0, sticky="W")

e1 = tk.Entry(master, width=50)
e1.grid(row=0, column=1)

browse_button = tk.Button(master, text="Browse", command=browse)
browse_button.grid(row=0, column=2, padx=5, pady=5)

convert_button = tk.Button(master, text="Convert", command=pdf2img)
convert_button.grid(row=1, column=1, columnspan=2, pady=10)

# Progress bar and status label
progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=2, column=1, columnspan=2, pady=10)

status_label = tk.Label(master, text="")
status_label.grid(row=3, column=1, columnspan=2)

tk.mainloop()
