import json


def read_json(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    data = read_json("user_update.json")
    """
       期望数据格式：[("13099999999","123456","8888","账号不存在!",false),
            ("17864307785","error","8888","密码错误!",false)]
    """
    list = []
    for n in data.values():
        list.append((n["username"], n["pwd"], n["code"], n["msg"], n["flag"]))  # n["key"] 或n.get("key")
    print(list)