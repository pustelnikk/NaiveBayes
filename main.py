import csv
import random


def create_matrix(name):
    data = []
    with open(name) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def main():

    # dane treningowe i testowe
    X = create_matrix('train.csv')
    Y = create_matrix('test.csv')

    random.seed(1)
    X = random.sample(X, 5)

    # odpowiedzi do danych testowych
    y = [y[0] for y in Y]

    # lista  słowników -> lista zawiera słowniki z atrybutami i ich licznością w danej kolumnie
    attr_count = []

    for val in X[0]:
        attr_count.append({val: 1})

    for row in X[1:]:
        for idx, val in enumerate(row):  # poszczegolne kolumny
            if val in attr_count[idx]:
                attr_count[idx][val] += 1
            else:
                attr_count[idx][val] = 1

    # testowanie
    answers = []    # do porownania ze zbiorem Y

    for row in Y:
        prop = {}

        # możliwe wartości klucza z pierwszej kolumny
        for key in attr_count[0].keys():

            # do obliczania prawdopodobieństwa w jednym wierszu
            prop[key] = attr_count[0][key] / len(X)

            for idx, col in enumerate(row[1:]):
                mianownik = attr_count[0][key]
                licznik = 0.0

                # obliczanie licznika
                for x_row in X:
                    if x_row[0] == key and x_row[idx+1] == col:
                        licznik += 1.0

                # wygladzanie jesli trzeba
                if licznik == 0.0:
                    licznik = 1.0
                    mianownik += len(attr_count[idx+1])

                # obliczanie prawdopodobienstwa
                prop[key] *= licznik / mianownik
                #
        answers.append(max(prop, key=lambda x: prop[x]))

    print()
    acc = 0.
    tp = 0.0
    tn = 0.0
    fp = 0.0
    fn = 0.0

    for ans, test in zip(answers, y):
        print(f'{ans}, {test}')

        if ans == 'p' and test == 'p':
            tp += 1
        elif ans == 'e' and test == 'p':
            fn += 1
        elif ans == 'p' and test == 'e':
            fp += 1
        else:
            tn += 1

    accuracy = (tp + tn)/(tp + tn + fp + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f = 2 * precision * recall / (precision + recall)
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F: {f}')


if __name__ == '__main__':
    main()
