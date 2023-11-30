import tkinter as tk
import random


def new_game():
    global answer, attempt, guesses
    answer = random.randint(1, 100)
    attempt = 1
    guesses = []
    update_info_label("新しいゲームを始めます。\n1～100の数字を当ててください。")
    entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)
    guesses_label.config(text="過去の予想: なし")


def update_info_label(message):
    info_label.config(text=f"試行 {attempt}/6: {message}")


def guess():
    global attempt, guesses
    try:
        guess = int(entry.get())
    except ValueError:
        update_info_label("有効な数字を入力してください。")
        return

    guesses.append(guess)
    guesses_label.config(text=f"過去の予想: {', '.join(map(str, guesses))}")

    if guess == 0:
        update_info_label("ゲームを終了します。")
        guess_button.config(state=tk.DISABLED)
    elif guess == answer:
        update_info_label("正解です！おめでとうございます！")
        guess_button.config(state=tk.DISABLED)
    elif guess < answer:
        update_info_label("もっと大きい数字です。")
    else:
        update_info_label("もっと小さい数字です。")

    attempt += 1
    if attempt > 6:
        update_info_label(f"残念！正解は {answer} でした。")
        guess_button.config(state=tk.DISABLED)

    entry.delete(0, tk.END)


# GUIアプリケーションの作成
root = tk.Tk()
root.title("数当てゲーム")
root.geometry("400x300")  # ウィンドウの大きさを固定
root.resizable(False, False)  # ウィンドウのサイズ変更を不可に

# フォント設定
font_large = ("Arial", 16)

# ウィジェットの追加
info_label = tk.Label(root, text="1～100の数字を当ててください。", font=font_large)
info_label.pack()

entry = tk.Entry(root, font=font_large)
entry.pack()

guess_button = tk.Button(root, text="予想する", command=guess, font=font_large)
guess_button.pack()

guesses_label = tk.Label(root, text="過去の予想: なし", font=font_large)
guesses_label.pack()

new_game_button = tk.Button(root, text="新しいゲームを始める", command=new_game, font=font_large)
new_game_button.pack()

# ゲームの初期化
answer = 0
attempt = 1
guesses = []
new_game()

# イベントループの開始
root.mainloop()
