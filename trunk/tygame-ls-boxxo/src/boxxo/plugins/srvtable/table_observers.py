# coding=UTF-8

__author__ = [
    'Zhaoqh'
    '"Zhouhao" <zhouhao@tuyoogame.com>',
]


class TYObservers(dict):
    '''
    桌子上的观察者的集合
    '''
    def __init__(self, table):
        super(TYObservers, self).__init__()
        self.table = table


