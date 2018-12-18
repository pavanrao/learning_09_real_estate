import csv
import os

from data.data_types import Purchase


def print_header():
    print('------------------------------------------------')
    print('-------Real estate app--------------------------')
    print('------------------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')

def load_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)

        return purchases


def load_file_dict_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:
        # header = fin.readline() -- dont strip header for DictReader
        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print("Bed count: {}".format(row['beds']))


def load_file_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        reader = csv.reader(fin)
        for row in reader:
            print(row)


def load_file_basic(file_name):
    with open(file_name, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        print('found header: {}'.format(header.strip()))

        lines = []
        for line in fin:
            line_data = line.strip().split(',')
            lines.append(line_data)

        print(lines[:5])


def query_data(data):
    pass


def main():
    print_header()
    file_name = get_data_file()
    data = load_file(file_name)
    query_data(data)


if __name__ == '__main__':
    main()
