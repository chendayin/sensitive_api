import requests


def main():
    url = "http://192.168.1.114:4000/sensitive"
    data = {'txt': 'test'}
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == '__main__':
    main()
