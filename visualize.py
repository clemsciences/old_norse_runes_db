"""

"""

from collections import Counter

import matplotlib.pyplot as plt

import reader as runesdb_reader


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def extract_year(text):
    if "-" in text:
        beginning, end = text.split("-")
        return int((int(end) + int(beginning)) / 2)
    else:
        return int(text)


def display_runic_inscriptions_in_time(runic_insc):
    chronological_runic_insc = sorted(runic_insc, key=lambda ri: extract_year(ri["rs_extdat"]))
    x = [extract_year(ri["rs_extdat"]) for ri in chronological_runic_insc]
    runic_inscriptions_per_year = Counter(x)
    plt.rcParams["figure.figsize"] = (15, 10)
    plt.plot(x, [runic_inscriptions_per_year[t] for t in x])
    plt.show()


if __name__ == "__main__":
    interesting_runic_inscriptions = [row for row in runesdb_reader.read("runes_data_example.csv")
                                      if row["rs_translat"] != "-"]
    print(len(interesting_runic_inscriptions))
    display_runic_inscriptions_in_time(interesting_runic_inscriptions)
