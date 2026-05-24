import tkinter as tk

# ---------- ПЕРЕМЕННЫЕ ----------
score = 0
click_power = 1
auto_click = 0

normal_cost = 10
mega_cost = 50
auto_cost = 30

# ---------- ФУНКЦИИ ----------
def animate_click():
    click_btn.config(bg="#9d4edd")
    root.after(100, lambda: click_btn.config(bg="#7b2cbf"))

def animate_score():
    score_label.config(font=("Arial", 16, "bold"))
    root.after(100, lambda: score_label.config(font=("Arial", 14)))

def update_labels():
    score_label.config(text=f"Очки: {score}")
    power_label.config(text=f"Сила клика: {click_power}")
    auto_label.config(text=f"Автоклик: {auto_click}/сек")

    normal_btn.config(text=f"+1 к клику\nЦена: {normal_cost}")
    mega_btn.config(text=f"МЕГА КЛИК\n+10 к клику\nЦена: {mega_cost}")
    auto_btn.config(text=f"АВТО КЛИК\n+1/сек\nЦена: {auto_cost}")

def click():
    global score
    score += click_power
    animate_click()
    animate_score()
    update_labels()

def buy_normal():
    global score, click_power, normal_cost
    if score >= normal_cost:
        score -= normal_cost
        click_power += 1
        normal_cost = int(normal_cost * 1.4)
        update_labels()

def buy_mega():
    global score, click_power, mega_cost
    if score >= mega_cost:
        score -= mega_cost
        click_power += 10
        mega_cost = int(mega_cost * 2)  # сильно дорожает
        update_labels()

def buy_auto():
    global score, auto_click, auto_cost
    if score >= auto_cost:
        score -= auto_cost
        auto_click += 1
        auto_cost = int(auto_cost * 1.6)
        update_labels()

def auto_clicker():
    global score
    score += auto_click
    update_labels()
    root.after(1000, auto_clicker)

# ---------- ОКНО ----------
root = tk.Tk()
root.title("Фиолетовый кликер")
root.geometry("650x380")
root.resizable(False, False)
root.configure(bg="#0b0614")

# ---------- ЛЕВАЯ ЧАСТЬ ----------
main = tk.Frame(root, bg="#0b0614")
main.pack(side="left", expand=True, fill="both")

title = tk.Label(
    main, text="💜 КЛИКЕР 💜",
    font=("Arial", 20, "bold"),
    fg="#b84cff", bg="#0b0614"
)
title.pack(pady=10)

score_label = tk.Label(main, text="Очки: 0",
                       font=("Arial", 14),
                       fg="white", bg="#0b0614")
score_label.pack()

power_label = tk.Label(main, text="Сила клика: 1",
                       font=("Arial", 12),
                       fg="#c77dff", bg="#0b0614")
power_label.pack()

auto_label = tk.Label(main, text="Автоклик: 0/сек",
                      font=("Arial", 12),
                      fg="#c77dff", bg="#0b0614")
auto_label.pack()

click_btn = tk.Button(
    main, text="КЛИК",
    font=("Arial", 18, "bold"),
    width=10, height=2,
    bg="#7b2cbf", fg="white",
    activebackground="#9d4edd",
    command=click
)
click_btn.pack(pady=25)

# ---------- ПРАВАЯ ПАНЕЛЬ ----------
shop = tk.Frame(root, width=230, bg="#120a24")
shop.pack(side="right", fill="y")

shop_title = tk.Label(
    shop, text="УЛУЧШЕНИЯ",
    font=("Arial", 14, "bold"),
    fg="#e0aaff", bg="#120a24"
)
shop_title.pack(pady=10)

normal_btn = tk.Button(
    shop,
    text="+1 к клику\nЦена: 10",
    font=("Arial", 10),
    bg="#3c096c", fg="white",
    activebackground="#5a189a",
    command=buy_normal
)
normal_btn.pack(pady=8, padx=10, fill="x")

mega_btn = tk.Button(
    shop,
    text="МЕГА КЛИК\n+10 к клику\nЦена: 50",
    font=("Arial", 10),
    bg="#3c096c", fg="white",
    activebackground="#5a189a",
    command=buy_mega
)
mega_btn.pack(pady=8, padx=10, fill="x")

auto_btn = tk.Button(
    shop,
    text="АВТО КЛИК\n+1/сек\nЦена: 30",
    font=("Arial", 10),
    bg="#3c096c", fg="white",
    activebackground="#5a189a",
    command=buy_auto
)
auto_btn.pack(pady=8, padx=10, fill="x")

# ---------- ЗАПУСК ----------
auto_clicker()
root.mainloop()