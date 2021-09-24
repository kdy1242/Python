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
    if len(player) != 3:
        raise custom_error.InvalidCountError("3자리가 아닙니다")
    # strike, ball 확인하자
    strike, ball = check(answer, player)
    # 출력하자
    print(f'{player}\tstrike : {strike}\tball : {ball}')
    # strike 가 3일때 나가자
    if strike == 3:
        break
    # 축하해주자
    print('축하합니다. 짝짝짝')