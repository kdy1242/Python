import random


# 숫자야구게임
# 퀴즈내자 숫자 세자리 중복없이
def make_quiz():
    list_r = random.sample(range(1, 9 + 1), 3)
    string_number = "".join(map(str, list_r))

    return string_number


def check(answer, player):
    strike = 0
    ball = 0

    for i, p in enumerate(player):
        for j, a in enumerate(answer):
            if p == a:  # 번호가 같으면
                if i == j:
                    strike += 1     # 번호가 있고, 자리가 같으면 strike += 1
                else:
                    ball += 1       # 번호가 있고, 자리가 다르면 ball += 1

    return strike, ball


if __name__ == '__main__':
    answer = make_quiz()
    strike, ball = check("238", "241")
    print(strike, ball)  # 1  0
    strike, ball = check("381", "182")
    print(strike, ball)  # 1  1