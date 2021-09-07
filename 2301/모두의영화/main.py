from 기능 import Ticketing


def print_menu():
    print('-----------메뉴------------')
    print('1. 상영 중인 영화 보기')
    print('2. 예매하기')
    print('3. 예매 내역 확인하기')
    print('4. 종료')
    print('-----------------------')
    menu = input('>> 메뉴를 선택하세요 : ')
    return menu


def main():
    movie_T = Ticketing()
    while True:
        menu = print_menu()
        if menu == '1':
            movie_T.show_movie()
        elif menu == '2':
            movie_T.sum = 1
            movie_T.ticketing()  # 예매하기
        elif menu == '3':
            movie_T.show_ticket()  # 예매 내역 확인
        elif menu == '4':
            print('종료한다~')
            break
        else:
            print('다시 입력하렴...')


if __name__ == '__main__':
    main()
