from baseball_game_engine import make_quiz, check
import custom_error

answer = make_quiz()
# 무한반복
while True:
    # 숫자 세자리 중복없이 묻자
    player = input("숫자 세자리는? ")     # player: "123", "fun
    try:
        player_int = int(player)            # ValueError
    except ValueError:
        continue
    # 길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        print(f'입력한 숫자의 개수가 정답과 다릅니다. 정답:{len(answer)}글자')
        continue
    # strike, ball 확인하자
    strike, ball = check(answer, player)
    # 출력하자
    print(f'{player}\tstrike : {strike}\tball : {ball}')
    # strike 가 3일때 나가자
    if strike == 3:
        break
    # 축하해주자
    print('축하합니다. 짝짝짝')