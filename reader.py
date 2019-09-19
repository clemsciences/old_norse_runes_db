"""

"""

import csv
import codecs


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def read(filename):
    with codecs.open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, dialect=csv.unix_dialect, delimiter=";", quoting=csv.QUOTE_ALL)
        return [row for row in reader]


if __name__ == "__main__":
    runes_db_filename = "runes_data.csv"
    read(runes_db_filename)
