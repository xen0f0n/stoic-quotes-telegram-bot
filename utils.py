import json
from random import randint


def get_quote():
    with open('quotes.json') as f:
        quotes = json.load(f)['quotes']
        rand_index = randint(0, len(quotes) - 1)

        return list(quotes[rand_index].values())


if __name__ == '__main__':
    print(get_quote())
