def main(word):
    wordArray = list(word)
    for i in range(97, 123):
        found = False
        for index in range(0, len(wordArray)):
            if chr(i) == wordArray[index]:
                print(index, end=' ')
                found = True
                break
        if found == False:
            print(-1, end=' ')


if __name__ == '__main__':
    main(input())
