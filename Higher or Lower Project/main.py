# Todo1: ロゴを入れる
from game_data import data
from art import logo, vs
import random

print(logo)

# Todo2: 表示用にフォーマット関数を用意
def format_data(person):
    name = person["name"]
    desc = person["description"]
    country = person["country"]
    return f"{name}, a {desc}, from {country}"

# Todo3: ランダムな人物データを1つ返す関数
def get_random_person():
    return random.choice(data)

# Todo4: ゲームスタートの処理
score = 0
game_should_continue = True

a = get_random_person()
b = get_random_person()

while b == a:
    b = get_random_person()

while game_should_continue:
    print(f"Compare A: {format_data(a)}")
    print(vs)
    print(f"Against B: {format_data(b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_follow = a["follower_count"]
    b_follow = b["follower_count"]

    is_correct = (guess == "A" and a_follow > b_follow) or (guess == "B" and b_follow > a_follow)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        a = b
        b = get_random_person()
        while b == a:
            b = get_random_person()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

#
#
# #Todo1 :ロゴを入れる
# from game_data import data
# from art import logo,vs
# import random
# print(logo)
#
# # Todo2: 比較相手Aを載せる game_data.pyより引用
#
# def compare_a():
#     index = random.randint(0, len(data) - 1)
#     print(f"Compare A: {data[index]["name"]} ,{data[index]["description"]},{data[index]["country"]}")
#     return data[index]['follower_count']
#
#
# def compare_b():
#     index = random.randint(0, len(data) - 1)
#     print(f"Against B:  {data[index]["name"]} ,{data[index]["description"]},{data[index]["country"]}")
#     return data[index]['follower_count']
#
#
# # Todo3 :VSのロゴと、対戦相手Bを載せる
# a_follow = compare_a()
# print(vs)
# b_follow = compare_b()
#
# # Todo4:input入力
#
# # Todo5: もしguessが当たったら正解の表示とscoreの加算をする
# score = 0
# guess = input("Who has more followers? Type 'A' or 'B': ")
#
# while b_follow == a_follow:
#
#     if guess == "A" and a_follow > b_follow:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     elif guess == "B" and b_follow > a_follow:
#         score += 1
#         b_follow = a_follow
#         print(f"You're right! Current score: {score}")
#     else:
#         break
#     print(f"Sorry, that's wrong. Final score: {score}")
#
#
# # Todo6:再度ループで継続する。この時、1問目でBとして出題された問題を2問目ではＡとして出題する
#
#
# # Todo7: 間違えたらループ終了ファイナルスコアを出力する