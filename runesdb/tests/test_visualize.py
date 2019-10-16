"""

"""
import os
import unittest
from collections import Counter

import matplotlib.pyplot as plt

from runesdb import PACKDIR
from runesdb import reader as runesdb_reader

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class UnitTest(unittest.TestCase):

    def test_display_runic_inscriptions_in_time(self):
        interesting_runic_inscriptions = [row for row in runesdb_reader.read(os.path.join(PACKDIR, "tests", "resources",
                                                                                          "runes_data_example.csv"))
                                          if row["rs_translat"] != "-"]
        chronological_runic_insc = sorted(interesting_runic_inscriptions,
                                          key=lambda ri: runesdb_reader.extract_year(ri["rs_extdat"]))
        x = [runesdb_reader.extract_year(ri["rs_extdat"]) for ri in chronological_runic_insc]
        runic_inscriptions_per_year = Counter(x)
        plt.rcParams["figure.figsize"] = (5, 3)

        plt.plot(x, [runic_inscriptions_per_year[t] for t in x])
        plt.title("Elder Futhark runic inscriptions")
        plt.ylabel("Number of found inscriptions")
        plt.xlabel("Years")
        plt.show()
        self.assertEqual(len(interesting_runic_inscriptions), 171)
