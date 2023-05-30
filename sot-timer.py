import datetime
import tkinter as tk
import keyboard

def start_countdown():
    target_time = datetime.datetime.utcnow().replace(microsecond=0)
    target_time = target_time.replace(hour=int(hour_entry.get()), minute=int(minute_entry.get()), second=int(second_entry.get()))

    if target_time < datetime.datetime.utcnow():
        print("Hedef zaman geçmiş.")
        return

    while datetime.datetime.utcnow() < target_time:
        root.update()

    keyboard.press_and_release('enter')

def update_utc_time():
    current_time = datetime.datetime.utcnow().strftime('%H:%M:%S')
    time_label.config(text=f"UTC Time: {current_time}")
    root.after(1000, update_utc_time)

root = tk.Tk()
root.geometry("270x220")
root.configure(bg='#242424')
root.title('SOT Filo Zamanlayıcı')

# Ekranın genişliğini ve yüksekliğini alın
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Pencereyi ekranın ortasına yerleştirin
x_coordinate = int((screen_width / 2) - (300 / 2))
y_coordinate = int((screen_height / 2) - (300 / 2))
root.geometry("{}x{}+{}+{}".format(300, 300, x_coordinate, y_coordinate))

time_label = tk.Label(root, font=('Helvetica', 16), fg='#ffffff', bg='#242424', text="UTC Time:")
time_label.pack(pady=10)

hour_frame = tk.Frame(root, bg='#242424')
hour_frame.pack()
hour_label = tk.Label(hour_frame, fg='#ffffff', bg='#242424', text="Saat    :")
hour_label.pack(side=tk.LEFT, padx=(5, 10))
hour_entry = tk.Entry(hour_frame, bg='#ffffff', bd=0, font=('Helvetica', 12), width=4)
hour_entry.pack(side=tk.LEFT)

minute_frame = tk.Frame(root, bg='#242424')
minute_frame.pack()
minute_label = tk.Label(minute_frame, fg='#ffffff', bg='#242424', text="Dakika:")
minute_label.pack(side=tk.LEFT, padx=(5, 10))
minute_entry = tk.Entry(minute_frame, bg='#ffffff', bd=0, font=('Helvetica', 12), width=4)
minute_entry.pack(side=tk.LEFT)

second_frame = tk.Frame(root, bg='#242424')
second_frame.pack()
second_label = tk.Label(second_frame, fg='#ffffff', bg='#242424', text="Saniye:")
second_label.pack(side=tk.LEFT, padx=(5, 10))
second_entry = tk.Entry(second_frame, bg='#ffffff', bd=0, font=('Helvetica', 12), width=4)
second_entry.pack(side=tk.LEFT)

start_button = tk.Button(root, text='Başlat', fg='#ffffff', bg='#4285f4', font=('Helvetica', 12), command=start_countdown)
start_button.pack(pady=10)

github_label = tk.Label(root, font=('Helvetica', 10), fg='#a0a0a0', bg='#242424', text="github.com/volkancelik28 - DC:#9898")
github_label.pack(side=tk.BOTTOM, pady=10)

update_utc_time()
root.mainloop()