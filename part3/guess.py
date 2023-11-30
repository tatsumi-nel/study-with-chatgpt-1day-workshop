import random


def play_number_guessing_game():
    while True:
        # 答えとなる数字をランダムに選ぶ
        answer = random.randint(1, 100)
        print("\n新しいゲームを始めます。1～100の数字を当ててください。")

        # ユーザが6回以内に答えを当てるか、0を入力するまで繰り返す
        for attempt in range(1, 7):
            try:
                # ユーザからの入力を受け取る
                guess = int(input(f"試行 {attempt}/6: あなたの予想する数字を入力してください: "))

                # ゲーム終了の条件
                if guess == 0:
                    print("ゲームを終了します。")
                    return

                # 答えとの比較
                if guess == answer:
                    print("正解です！おめでとうございます！")
                    break
                elif guess < answer:
                    print("もっと大きい数字です。")
                else:
                    print("もっと小さい数字です。")

            except ValueError:
                print("有効な数字を入力してください。")

        else:
            # 5回の試行で答えられなかった場合
            print(f"残念！正解は {answer} でした。")

        # ゲームを続けるか確認
        play_again = input("\nもう一度プレイしますか？（ yes / no ）: ")
        if play_again.lower() != "yes":
            break


# ゲームを実行する
play_number_guessing_game()
