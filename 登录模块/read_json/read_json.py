import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def read_json(self):
        with open(self.fileopen, 'r', encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("login.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("result"),
                     data.get("flag"),
                     data.get("num")))
    print(arrs)
