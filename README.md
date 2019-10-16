![PyPI](https://img.shields.io/pypi/v/runesdb) [![Build Status](https://travis-ci.org/clemsciences/old_norse_runes_db.svg?branch=master)](https://travis-ci.org/clemsciences/old_norse_runes_db)

# RuneS-DB

RuneS-DB is a platform where [results from different projects on runic inscriptions](https://www.runesdb.eu/project/data-sources/) 
are combined.

This repository is completely independent from RuneS-DB.

## Installation

Works for Python 3.6 and above.

```
$ pip install runesdb
```

## Sources

The data is available [here](http://www.runesdb.eu/) where you can export results of a query by clicking on a small 
button whose id is "butDownloadExcelModal" (I note it here because I needed time to find it!). 

When you download data, you get this note:
> The rights to the data are held by the Göttingen Academy of Sciences and Humanities and are subject to the CC-BY- SA law. The RuneS research units Göttingen, Eichstätt-München and Kiel were involved in the generation of the data. RuneS-DB contains data from the Kiel Runenprojekt, the Danish database runer.ku.dk and the Samnordisk runtextdatabas/Rundata accessible under the Open Database License (ODbL). Please also note the additional information on other origin of the data provided under the label sources .

If you confirm by clicking on "Download data", you will get a file named "runes_data.csv". 

## Code

User `reader.py` just to read your data. `visualize.py` provides a basic example on how to look at data according 
to estimated time of creation of runic inscriptions;
