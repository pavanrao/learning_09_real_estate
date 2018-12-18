import csv
import os
import statistics

from data.data_types import Purchase


def print_header():
    print("------------------------------------------------")
    print("-------Real estate app--------------------------")
    print("------------------------------------------------")
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, "data", "SacramentoRealEstateTransactions2008.csv")


def load_file(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)

        return purchases


def load_file_dict_reader(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        # header = fin.readline() -- dont strip header for DictReader
        reader = csv.DictReader(fin)
        for row in reader:
            print(type(row), row)
            print("Bed count: {}".format(row["beds"]))


def load_file_csv(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        header = fin.readline()
        reader = csv.reader(fin)
        for row in reader:
            print(row)


def load_file_basic(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        header = fin.readline()
        print("found header: {}".format(header.strip()))

        lines = []
        for line in fin:
            line_data = line.strip().split(",")
            lines.append(line_data)

        print(lines[:5])


def get_price(p):
    return p.price


def query_data(data):
    # Sort the list in place

    # use a method to get price for purchase object
    # data.sort(key=get_price)

    # use a lambda to get price of a purchase object
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print(
        "The most expensive house is ${:,} with {} beds and {} baths.".format(
            high_purchase.price, high_purchase.beds, high_purchase.baths
        )
    )

    # least expenseive house?
    low_purchase = data[0]
    print(
        "The least expensive house is ${:,} with {} beds and {} baths.".format(
            low_purchase.price, low_purchase.beds, low_purchase.baths
        )
    )

    # average price of house ?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price  # projection
        for p in data  # the set to process
    ]

    average_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(average_price)))

    # average price of 2 bedroom houses?
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    two_bed_homes = [
        p
        for p in data
        if p.beds == 2
    ]

    average_price = statistics.mean(p.price for p in two_bed_homes)
    average_baths = statistics.mean(p.baths for p in two_bed_homes)
    average_sqft = statistics.mean(p.sq__ft for p in two_bed_homes)
    print("The average 2 bedroom home price is ${:,}, baths={}, sq ft={}".
          format(int(average_price), round(average_baths, 1), round(average_sqft, 1)))


def main():
    print_header()
    file_name = get_data_file()
    data = load_file(file_name)
    query_data(data)


if __name__ == "__main__":
    main()
