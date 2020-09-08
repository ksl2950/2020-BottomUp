
def P_2884():
    print('숫자 두개를 입력하세요: ', end='')
    h, m = map(int, input().split())
    if m >= 45:
        m -= 45
    elif m < 45:
        if h == 0:
            h = 23
            m = 60-(45-m)
        else:
            h -= 1
            m = 60 - (45 - m)
    print(h, m)

if __name__ == '__main__':
      P_2884()