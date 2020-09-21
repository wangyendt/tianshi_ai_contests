#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: main
@time: 2020/09/22 00:14
"""

import os
import numpy as np
import pandas as pd
from sklearn.svm import SVC


def load_data(name='test'):
    path = os.path.join('data', name + '.csv')
    data = pd.read_csv(path)
    return data


def main():
    train_data = load_data('train')
    test_data = load_data('test')
    print(train_data.head(4))
    print(test_data.head(4))


if __name__ == '__main__':
    main()
