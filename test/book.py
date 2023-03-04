for i in range(5):
    with open("words.txt", "r" ,encoding='utf-8') as f:
        x = f.read().splitlines()
    print(x[i])

