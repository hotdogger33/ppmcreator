from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
from tkinter import colorchooser

def create_ppm_file():
    text = text_entry.get()
    text_color = text_color_button['bg']
    bg_color = bg_color_button['bg']

    if not text.strip():
        status_label.configure(text="Please enter some text.")
        return

    font = ImageFont.truetype('FreeSans.ttf', 24)
    text_width, text_height = font.getsize(text)

    image = Image.new('RGB', (text_width, text_height), bg_color)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, fill=text_color, font=font)

    first_word = text.split()[0]
    counter = get_counter()
    file_name = f"{first_word}_{counter}.ppm"  # Change the file extension to .ppm
    image.save(file_name, format='PPM')  # Specify the format as PPM

    status_label.configure(text=f"File '{file_name}' created successfully.")

# Update the create_button_click function
def create_button_click():
    create_ppm_file()

def get_counter():
    counter_file = "counter.txt"
    counter = 1

    if os.path.isfile(counter_file):
        with open(counter_file, 'r') as file:
            counter = int(file.read()) + 1

    with open(counter_file, 'w') as file:
        file.write(str(counter))

    return counter

def choose_text_color():
    color = colorchooser.askcolor(title="Choose Text Color", color="black")[1]
    if color:
        text_color_button.configure(bg=color, activebackground=color)
        text_color_button['fg'] = invert_color(color)

def choose_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color", color="white")[1]
    if color:
        bg_color_button.configure(bg=color, activebackground=color)
        bg_color_button['fg'] = invert_color(color)

def invert_color(color):
    r, g, b = colorchooser.HTMLColorToRGB(color)
    inverted_r = 255 - r
    inverted_g = 255 - g
    inverted_b = 255 - b
    return f"#{inverted_r:02x}{inverted_g:02x}{inverted_b:02x}"

# Create the main window
window = tk.Tk()
window.title("Text to PPM")
window.geometry("500x300")
window.resizable(False, False)  # Make the window non-resizable

# Create the input elements
text_label = tk.Label(window, text="Enter the text:")
text_label.pack(pady=10)

text_entry = tk.Entry(window)
text_entry.pack()

text_color_button = tk.Button(window, text="Choose Text Color", command=choose_text_color, bg="black", fg="white")
text_color_button.pack(pady=10)

bg_color_button = tk.Button(window, text="Choose Background Color", command=choose_bg_color, bg="white", fg="black")
bg_color_button.pack(pady=10)

create_button = tk.Button(window, text="Create PPM", command=create_button_click)
create_button.pack(pady=10)

status_label = tk.Label(window, text="")
status_label.pack(pady=10)

window.mainloop()
