from movie import Movie


class Ticketing:
    def __init__(self):
        self.sum = 1
        self.movies = []
        self.theater_list = set()
        self.movie_list = []
        self.ticket_list = []
        self.put_movie()

    def __str__(self):
        pass

    def show_movie(self):
        self.movies = list(set(i.name for i in self.movie_list))
        for index, movie in enumerate(self.movies):
            print(f'{index + 1}. {movie}')

    def ticketing(self):
        self.show_movie()
        num = int(input('뭐 예매할래!!! >> ')) - 1
        time_list = []
        i = 0
        for movie in self.movie_list:
            if movie.name == self.movies[num]:
                print(f'{i + 1}. !{movie.theater}! => {movie.stTime}')
                time_list.append(movie)
                i += 1
        num = int(input('뭐 예매할래!!! >> ')) - 1
        print('이거? >> ', time_list[num])

        pay = input(f'--금액 {7000 * self.sum}원--\n돈줄래1 예매더할래0 : ')
        if pay == '1':
            self.ticket_list.append(time_list[num])
            print('입금완료^^')
            self.show_ticket()
        elif pay == '0':
            self.sum += 1
            self.ticket_list.append(time_list[num])
            self.ticketing()
        else:
            self.ticket_list.append(time_list[num])
            print(f'잘못눌렀다 ✿두배✿입금완료^^ 금액 {7000 * self.sum*2}원')
            print('''
                    ＿人人 人人＿ 
                  ＞    감사   ＜
                    ￣Y^Y^Y^Y￣
            ＼😆へ　 へ😁ヘ　 く😎/ 
            ヘ / 　　 ( ヘ 　 ( ヘ 
               >　 　 <　　　　く
            ''')
            self.show_ticket()

    def show_ticket(self):
        print('╔══════════════════════════════════════ °• 예매내역 •° ════════════════════════════════════════╗')
        for d, i in enumerate(self.ticket_list):
            print(' ',d + 1, i)
        print('╚═════════════════════════════════════════ °• ♔ •° ══════════════════════════════════════════╝')

    def put_movie(self):
        # CGV
        demonslayer_1 = Movie()
        demonslayer_1.set_theater('CGV')
        demonslayer_1.set_name('귀멸의 칼날 무한열차')
        demonslayer_1.set_time('117')
        demonslayer_1.stTime = '12:00'

        conjuring3_1 = Movie()
        conjuring3_1.set_theater('CGV')
        conjuring3_1.set_name('컨저링3 - 악마가 시켰다')
        conjuring3_1.set_time('112')
        conjuring3_1.stTime = '15:30'

        furiousrage_1 = Movie()
        furiousrage_1.set_theater('CGV')
        furiousrage_1.set_name('분노의 질주 - 더 얼티메이트')
        furiousrage_1.set_time('143')
        furiousrage_1.stTime = '19:50'
        # 롯데시네마
        demonslayer_2 = Movie()
        demonslayer_2.set_theater('롯데시네마')
        demonslayer_2.set_name('귀멸의 칼날 무한열차')
        demonslayer_2.set_time('117')
        demonslayer_2.stTime = '13:20'

        conjuring3_2 = Movie()
        conjuring3_2.set_theater('롯데시네마')
        conjuring3_2.set_name('컨저링3 - 악마가 시켰다')
        conjuring3_2.set_time('112')
        conjuring3_2.stTime = '16:00'

        furiousrage_2 = Movie()
        furiousrage_2.set_theater('롯데시네마')
        furiousrage_2.set_name('분노의 질주 - 더 얼티메이트')
        furiousrage_2.set_time('143')
        furiousrage_2.stTime = '20:10'
        # 메가박스
        demonslayer_3 = Movie()
        demonslayer_3.set_theater('메가박스')
        demonslayer_3.set_name('귀멸의 칼날 무한열차')
        demonslayer_3.set_time('117')
        demonslayer_3.stTime = '14:00'

        conjuring3_3 = Movie()
        conjuring3_3.set_theater('메가박스')
        conjuring3_3.set_name('컨저링3 - 악마가 시켰다')
        conjuring3_3.set_time('112')
        conjuring3_3.stTime = '17:40'

        furiousrage_3 = Movie()
        furiousrage_3.set_theater('메가박스')
        furiousrage_3.set_name('분노의 질주 - 더 얼티메이트')
        furiousrage_3.set_time('143')
        furiousrage_3.stTime = '22:15'

        self.movie_list.append(demonslayer_1)
        self.theater_list.add(demonslayer_1.theater)
        self.movie_list.append(conjuring3_1)
        self.theater_list.add(conjuring3_1.theater)
        self.movie_list.append(furiousrage_1)
        self.theater_list.add(furiousrage_1.theater)

        self.movie_list.append(demonslayer_2)
        self.theater_list.add(demonslayer_2.theater)
        self.movie_list.append(conjuring3_2)
        self.theater_list.add(conjuring3_2.theater)
        self.movie_list.append(furiousrage_2)
        self.theater_list.add(furiousrage_2.theater)

        self.movie_list.append(demonslayer_3)
        self.theater_list.add(demonslayer_3.theater)
        self.movie_list.append(conjuring3_3)
        self.theater_list.add(conjuring3_3.theater)
        self.movie_list.append(furiousrage_3)
        self.theater_list.add(furiousrage_3.theater)
