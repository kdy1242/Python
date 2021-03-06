class Entertainer:  #키, 얼굴. 인성, 이름
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):   #인성
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)  #self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'

아이유 = Entertainer('아이유')
#아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭쌤이상형')
아이유.set_kind('That\'s very good.')
print(아이유)

전유리 = Entertainer('간디')
전유리.set_height('130cm')
전유리.set_face('gandi')
전유리.set_kind('Goob')
print(전유리)

뷔 = Singer('뷔', 'Love Maze')
뷔.set_height('130cm')
뷔.set_face('gandi')
뷔.set_kind('Goob')
print(뷔)

심수련 = Talent('심수련', '펜트하우스')
심수련.set_height('175cm')
심수련.set_face('괜찮다')
심수련.set_kind('괜찮다')
print(심수련)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(전유리)
print(방탄소년단)

