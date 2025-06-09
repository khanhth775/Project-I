from pyvi import ViTokenizer
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict
import re
import nltk
from stop_words import get_stop_words

def format_text(input_file, max_line_length):
    keyword_table = defaultdict(list)
    line_number = 0
    formatted_text = ""

    with open(input_file, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            line = line.strip()
            words = ViTokenizer.tokenize(line).split()

            formatted_line = ''
            current_line_length = 0

            for word in words:
                if current_line_length + len(word) <= max_line_length:
                    formatted_line += word + ' '
                    current_line_length += len(word) + 1
                else:
                    formatted_text += formatted_line.strip() + '\n'
                    line_number += 1

                    for keyword in words:
                        if is_valid_keyword(keyword):
                            keyword_table[keyword].append(line_number)

                    formatted_line = word + ' '
                    current_line_length = len(word) + 1

            formatted_text += formatted_line.strip() + '\n'
            line_number += 1

            formatted_text = re.sub(r'^[.!?,;:]', '', formatted_text)

            for keyword in words:
                if is_valid_keyword(keyword):
                    keyword_table[keyword].append(line_number)

    return formatted_text, keyword_table

def is_valid_keyword(word):
    stop_words_vn = get_stop_words('vietnamese')
    stop_words_eng = nltk.download('stopwords')
    return word.lower() not in stop_words_vn and stop_words_eng

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        txt_file_entry.delete(0, tk.END)
        txt_file_entry.insert(tk.END, file_path)

def process_text():
    input_file = txt_file_entry.get()
    max_line_length = int(max_length_entry.get())
    if not input_file:
        messagebox.showerror("Error", "Please select a text file.")
        return
    if not max_line_length:
        messagebox.showerror("Error", "Please enter the maximum line length.")
        return

    try:
        formatted_text, keyword_table = format_text(input_file, max_line_length)
        result_text.configure(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, formatted_text)
        result_text.configure(state='disabled')

        keyword_table_str = ""
        for keyword, line_numbers in keyword_table.items():
            keyword_table_str += f'{keyword}: {line_numbers}\n'

        keyword_table_text.configure(state='normal')
        keyword_table_text.delete(1.0, tk.END)
        keyword_table_text.insert(tk.END, keyword_table_str)
        keyword_table_text.configure(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Text Formatter")

txt_file_label = tk.Label(window, text="Text File:")
txt_file_entry = tk.Entry(window, width=50)
txt_file_button = tk.Button(window, text="Browse", command=open_file)

max_length_label = tk.Label(window, text="Số ký tự tối đa của một hàng:")
max_length_entry = tk.Entry(window, width=10)

process_button = tk.Button(window, text="Process", command=process_text)

result_label = tk.Label(window, text="Văn bản đã định dạng:")
result_text = tk.Text(window, height=10, width=60)
result_text.configure(state='disabled')

keyword_table_label = tk.Label(window, text="Bảng từ khoá:")
keyword_table_text = tk.Text(window, height=10, width=60)
keyword_table_text.configure(state='disabled')

txt_file_label.grid(row=0, column=0, padx=5, pady=5)
txt_file_entry.grid(row=0, column=1, padx=5, pady=5)
txt_file_button.grid(row=0, column=2, padx=5, pady=5)

max_length_label.grid(row=1, column=0, padx=5, pady=5)
max_length_entry.grid(row=1, column=1, padx=5, pady=5)

process_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

result_label.grid(row=3, column=0, padx=5, pady=5)
result_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

keyword_table_label.grid(row=5, column=0, padx=5, pady=5)
keyword_table_text.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
