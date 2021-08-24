class Movie:
    def __init__(self):
        # 영화관, 제목, 가격, 시간
        self.theater = ''
        self.name = ''
        self.price = 7000
        self.time = ''
        self.stTime = ''

    def set_theater(self, th):
        self.theater = th

    def set_name(self, na):
        self.name = na

    def set_time(self, ti):
        self.time = ti

    def __str__(self):
        return f'제목 : {self.name}\t| 영화관 : {self.theater}\t| 시간 : {self.stTime}\t| 가격 : {self.price}'
