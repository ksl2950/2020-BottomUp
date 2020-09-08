def main():
    num = input()
    str = input()
    str_list=list(str)
    num_list = list(map(int,str_list))
    sum = 0
    for i in range (len(num_list)):
        sum += num_list[i]
    return sum


if __name__ == '__main__':
    print(main())