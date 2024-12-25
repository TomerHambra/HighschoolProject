import json


def count_colored(f):
    return len(f)-f.count('1')


def split_dictionaries():
    with open('dataset.json', 'r') as f:
        data = json.load(f)

    dicts = [{} for i in range(8)]
    for key, value in data.items():
        dicts[(count_colored(key))//7][key] = value

    i = 1
    for part in dicts:
        with open(f'data_vol{i}.json', 'w+') as f:
            json.dump(part, f)
        i += 1


if __name__ == '__main__':
    split_dictionaries()