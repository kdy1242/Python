from baseball_game_engine import make_quiz, check
import custom_error

answer = make_quiz()
# 무한반복
count = 0


def save_history(player, count):
    with open('baseball_history.txt', 'a') as f:
        f.write(f'{player}: {count}\n')


def load_history():
    count_list = []
    with open('baseball_history.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == '' or not line:
                break
            # print(line.rstrip())
            line_data = line.rstrip().split(': ')
            count_list.append(line_data[1])
        count_list.sort()
        return count_list[:3]


while True:
    # 숫자 세자리 중복없이 묻자
    player = input("숫자 세자리는?(t: top3)  ")     # player: "123", "fun
    if player == 't':
        history = load_history()
        print(history)
        continue
    try:
        player_int = int(player)            # ValueError
    except ValueError:
        continue
    # 길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        print(f'입력한 숫자의 개수가 정답과 다릅니다. 정답:{len(answer)}글자')
        continue
    # strike, ball 확인하자
    count += 1
    strike, ball = check(answer, player)
    # 출력하자
    print(f'{player}\tstrike : {strike}\tball : {ball}\t{count}트')
    # strike 가 3일때 나가자
    if strike == 3:
        # 저장하자
        save_history(player, count)
        break
# 축하해주자
print('축하합니다. 짝짝짝')