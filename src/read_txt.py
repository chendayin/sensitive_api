import glob


def main():
    with open("../data/色情.txt", encoding="utf8", mode="r") as f:
        txts = f.readlines()
    fs = open("../data/dict.txt", encoding="utf8", mode="a")
    for txt in txts:
        fs.write("色情\t" + txt.strip() + "\n")


if __name__ == '__main__':
    main()
