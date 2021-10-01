import os
data = os.listdir('.')  # 현재 디렉토리
data = os.listdir('..')  # 상위 디렉토리
# data = os.listdir('my_directory')
data = os.listdir('F:\\Python\\2301\\file handler')
data = os.listdir('F:/Python/2301/file handler')

# print(data)
for d in data:
    print(d)
    print(f'is directory? : {os.path.isdir(d)}')
    print(f'is file? : {os.path.isfile(d)}')