# -*- coding: utf-8 -*-
# @Time : 2022/2/16 0:13
# @Author : 王文玉
# @Site : 
# @Description: 
# @File : generate_sub_zn.py
# @Software: PyCharm
zn = open('../SP1/zn_subwords.txt', 'w', encoding='utf-8')

with open('../data/lao-zh.para.vocab1.txt', 'r', encoding='utf-8') as fr:
    for line in fr.readlines():
        word = line.replace('\n', '') + ' _'
        for char in line.replace('\n', ''):
            word = word + char + ' '
        zn.write(word[0:-1] + '\n')

zn.close()