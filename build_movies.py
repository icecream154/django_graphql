import json


def generate_actor(aid: int):
    dictionary = {
        'model': 'api.actor',
        'pk': aid,
        'fields': {
          'name': "Michael" + str(aid),
          'city': "Berlin"
        }
    }
    return dictionary


def generate_movie(mid: int, aids: []):
    return {
        "model": "api.movie",
        "pk": mid,
        "fields": {
            "title": "Creed",
            "actors": aids,
            "year": "2015"
        }
    }


if __name__ == '__main__':
    with open('./movies-full.json', 'w', encoding='utf-8') as f:
        data = []
        for i in range(700000):
            data.append(generate_actor(i))

        for i in range(280000):
            aids = [i, i + 1, i * 2]
            data.append(generate_movie(i, aids))

        f.write(json.dumps(data))
