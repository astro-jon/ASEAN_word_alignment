# -*- coding: utf-8 -*-
# @Time : 2022/2/14 15:17
# @Author : 王文玉
# @Site : 
# @Description: 
# @File : trainSP.py
# @Software: PyCharm
import sentencepiece as spm

spm.SentencePieceTrainer.Train(input='./data/lao.txt', model_prefix='./SP/lao', vocab_size=1000, model_type="unigram") # 在当前目录下生成 lao.model 和 lao.vocab 文件

# # 加载训练好的模型，切分文本
# sp = spm.SentencePieceProcessor(model_file='./SP1/lao2.model')
#
# # 编码 text -> id
# result = sp.encode(['ບາງຄັ້ງຂ້ອຍກໍ່ໃສ່ເກືອໜ້ອຍໜຶ່ງ'], out_type=int)
# print(result)
# result = sp.encode(['ບາງຄັ້ງຂ້ອຍກໍ່ໃສ່ເກືອໜ້ອຍໜຶ່ງ'], out_type=str)
# print(result)
# subwords = sp.EncodeAsPieces('ບາງຄັ້ງຂ້ອຍກໍ່ໃສ່ເກືອໜ້ອຍໜຶ່ງ')
# print(subwords)
#
# for _ in range(10):
#     result = sp.encode('ບາງຄັ້ງຂ້ອຍກໍ່ໃສ່ເກືອໜ້ອຍໜຶ່ງ', out_type=str, enable_sampling=True, alpha=0.1, nbest_size=-1)
#     print(result)