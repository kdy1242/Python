# 파이썬 객체 그대로 저장하자
import pickle
from person import Person


if __name__ == '__main__':
    n1 = Person('공도윤', '곰세마리')
    n4 = Person('김설', 'stay(저스틴비버)')
    friend = [n1, n4]

    with open('object.bin', 'wb') as f:
        pickle.dump(n1, f)

    with open('objects.bin', 'wb') as f:
        pickle.dump(friend, f)
