import tkinter as tk
import random


def new_game():
    global answer, attempt
    answer = random.randint(1, 100)
    attempt = 1
    info_label.config(text="新しいゲームを始めます。1～100の数字を当ててください。")
    entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)


def guess():
    global attempt
    try:
        guess = int(entry.get())
    except ValueError:
        info_label.config(text="有効な数字を入力してください。")
        return

    if guess == 0:
        info_label.config(text="ゲームを終了します。")
        guess_button.config(state=tk.DISABLED)
    elif guess == answer:
        info_label.config(text="正解です！おめでとうございます！")
        guess_button.config(state=tk.DISABLED)
    elif guess < answer:
        info_label.config(text="もっと大きい数字です。")
    else:
        info_label.config(text="もっと小さい数字です。")

    attempt += 1
    if attempt > 6:
        info_label.config(text=f"残念！正解は {answer} でした。")
        guess_button.config(state=tk.DISABLED)


# GUIアプリケーションの作成
root = tk.Tk()
root.title("数当てゲーム")

# ウィジェットの追加
info_label = tk.Label(root, text="1～100の数字を当ててください。")
info_label.pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="予想する", command=guess)
guess_button.pack()

new_game_button = tk.Button(root, text="新しいゲームを始める", command=new_game)
new_game_button.pack()

# ゲームの初期化
answer = 0
attempt = 1
new_game()

# イベントループの開始
root.mainloop()
