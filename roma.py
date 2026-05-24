D3rlord, [11.01.2026 19:17]
import tkinter as tk
import random

# ---------- ПЕРЕМЕННЫЕ ----------
score = 0
click_power = 1
auto_click = 0
prestige_bonus = 0  # бонус при перерождении

# Цены
normal_cost = 10
mega_cost = 150
auto_cost = 30
super_cost = 500
turbo_cost = 400

chest_visible = False  # сундук появляется
chest_bonus_text = ""

# ---------- АНИМАЦИИ ----------
def animate_click():
    click_btn.config(bg="#9d4edd")
    root.after(100, lambda: click_btn.config(bg="#7b2cbf"))

def animate_label(label, colors=["#ff77ff","#b84cff","#c77dff"]):
    def flash(i=0):
        label.config(fg=colors[i % len(colors)])
        if i < len(colors)*2:
            root.after(100, lambda: flash(i+1))
        else:
            label.config(fg="white")
    flash()

# ---------- ОБНОВЛЕНИЕ ----------
def update_labels():
    score_label.config(text=f"Очки: {score}")
    power_label.config(text=f"Сила клика: {click_power} (+{prestige_bonus} с перерождения)")
    auto_label.config(text=f"Автоклик: {auto_click}/сек")

    normal_btn.config(text=f"+1 к клику\nЦена: {normal_cost}")
    mega_btn.config(text=f"МЕГА КЛИК\n+10 к клику\nЦена: {mega_cost}")
    auto_btn.config(text=f"АВТО КЛИК\n+1/сек\nЦена: {auto_cost}")
    super_btn.config(text=f"СУПЕР КЛИК\n+50 к клику\nЦена: {super_cost}")
    turbo_btn.config(text=f"ТУРБО АВТОКЛИК\n+5/сек\nЦена: {turbo_cost}")

    if chest_visible:
        chest_btn.pack(pady=10)
    else:
        chest_btn.pack_forget()

# ---------- КЛИК ----------
def click():
    global score, chest_visible
    score += click_power + prestige_bonus
    animate_click()
    animate_label(score_label)
    # шанс на сундук 1/55
    if not chest_visible and random.randint(1, 55) == 1:
        chest_visible = True
    update_labels()

# ---------- УЛУЧШЕНИЯ ----------
def buy_normal():
    global score, click_power, normal_cost
    if score >= normal_cost:
        score -= normal_cost
        click_power += 1
        normal_cost = int(normal_cost * 1.4)
        animate_label(normal_btn)
        update_labels()

def buy_mega():
    global score, click_power, mega_cost
    if score >= mega_cost:
        score -= mega_cost
        click_power += 10
        mega_cost = int(mega_cost * 3)
        animate_label(mega_btn)
        update_labels()

def buy_auto():
    global score, auto_click, auto_cost
    if score >= auto_cost:
        score -= auto_cost
        auto_click += 1
        auto_cost = int(auto_cost * 1.6)
        animate_label(auto_btn)
        update_labels()

def buy_super():
    global score, click_power, super_cost
    if score >= super_cost:
        score -= super_cost
        click_power += 50
        super_cost = int(super_cost * 4)
        animate_label(super_btn)
        update_labels()

def buy_turbo():
    global score, auto_click, turbo_cost
    if score >= turbo_cost:
        score -= turbo_cost
        auto_click += 5
        turbo_cost = int(turbo_cost * 3)
        animate_label(turbo_btn)
        update_labels()

# ---------- ПЕРЕРОЖДЕНИЕ ----------
def prestige():
    global score, click_power, auto_click, normal_cost, mega_cost, auto_cost
    global super_cost, turbo_cost, prestige_bonus

    if score < 1000:
        info_label.config(text="Нужно минимум 1000 очков для перерождения!", fg="red")
        return

    prestige_bonus += 1

    # сброс всего
    score = 0
    click_power = 1
    auto_click = 0
    normal_cost = 10
    mega_cost = 150
    auto_cost = 30
    super_cost = 500
    turbo_cost = 400

    animate_label(info_label, colors=["#ffea00","#ff77ff","#b84cff"])
    info_label.config(text=f"Перерождение! Бонус к клику: {prestige_bonus}", fg="#ffea00")
    update_labels()

# ---------- АВТОКЛИК ----------
def auto_clicker():
    global score
    score += auto_click + prestige_bonus
    update_labels()
    root.after(1000, auto_clicker)

# ---------- СУНДУК ----------
def open_chest():
    global chest_visible, score, click_power, auto_click
    chest_visible = False

D3rlord, [11.01.2026 19:17]
bonus_type = random.choice(["+1 клик", "+10 клик", "+50 клик", "+1 авто", "+5 очков"])
    if bonus_type == "+1 клик":
        click_power += 1
    elif bonus_type == "+10 клик":
        click_power += 10
    elif bonus_type == "+50 клик":
        click_power += 50
    elif bonus_type == "+1 авто":
        auto_click += 1
    elif bonus_type == "+5 очков":
        score += 5

    info_label.config(text=f"Сундук дал: {bonus_type}!", fg="#00ff00")
    animate_label(info_label)
    update_labels()

# ---------- ОКНО ----------
root = tk.Tk()
root.title("Фиолетовый кликер v3")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg="#0b0614")

# ---------- ЛЕВАЯ ЧАСТЬ ----------
main = tk.Frame(root, bg="#0b0614")
main.pack(side="left", expand=True, fill="both")

title = tk.Label(main, text="💜 КЛИКЕР V3 💜", font=("Arial", 20, "bold"), fg="#b84cff", bg="#0b0614")
title.pack(pady=10)

score_label = tk.Label(main, text="Очки: 0", font=("Arial", 14), fg="white", bg="#0b0614")
score_label.pack()

power_label = tk.Label(main, text="Сила клика: 1", font=("Arial", 12), fg="#c77dff", bg="#0b0614")
power_label.pack()

auto_label = tk.Label(main, text="Автоклик: 0/сек", font=("Arial", 12), fg="#c77dff", bg="#0b0614")
auto_label.pack()

click_btn = tk.Button(main, text="КЛИК", font=("Arial", 18, "bold"), width=10, height=2,
                      bg="#7b2cbf", fg="white", activebackground="#9d4edd", command=click)
click_btn.pack(pady=20)

info_label = tk.Label(main, text="", font=("Arial", 12), bg="#0b0614", fg="white")
info_label.pack()

prestige_btn = tk.Button(main, text="Перерождение", font=("Arial", 12, "bold"),
                         bg="#ffea00", fg="#0b0614", command=prestige)
prestige_btn.pack(pady=10)

chest_btn = tk.Button(main, text="Открыть сундук 🎁", font=("Arial", 12, "bold"),
                      bg="#00ff00", fg="#0b0614", command=open_chest)

# ---------- ПРАВАЯ ПАНЕЛЬ ----------
shop = tk.Frame(root, width=280, bg="#120a24")
shop.pack(side="right", fill="y")

shop_title = tk.Label(shop, text="УЛУЧШЕНИЯ", font=("Arial", 14, "bold"), fg="#e0aaff", bg="#120a24")
shop_title.pack(pady=10)

normal_btn = tk.Button(shop, font=("Arial", 10), bg="#3c096c", fg="white", command=buy_normal)
normal_btn.pack(pady=5, padx=10, fill="x")

mega_btn = tk.Button(shop, font=("Arial", 10), bg="#3c096c", fg="white", command=buy_mega)
mega_btn.pack(pady=5, padx=10, fill="x")

auto_btn = tk.Button(shop, font=("Arial", 10), bg="#3c096c", fg="white", command=buy_auto)
auto_btn.pack(pady=5, padx=10, fill="x")

super_btn = tk.Button(shop, font=("Arial", 10), bg="#3c096c", fg="white", command=buy_super)
super_btn.pack(pady=5, padx=10, fill="x")

turbo_btn = tk.Button(shop, font=("Arial", 10), bg="#3c096c", fg="white", command=buy_turbo)
turbo_btn.pack(pady=5, padx=10, fill="x")

# ---------- ЗАПУСК ----------
update_labels()
auto_clicker()
root.mainloop()