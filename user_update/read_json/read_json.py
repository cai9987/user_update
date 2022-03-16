import json


class ReadJson(object):
    def __init__(self, filename):
        self.fileopen = "../data/" + filename

    def read_json(self):
        with open(self.fileopen, 'r', encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("user_update.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("user_name"),
                     data.get("user_header"),
                     data.get("user_moner"),
                     data.get("user_experience"),
                     data.get("result")))
    print(arrs)