# -*- coding: utf-8 -*-

import re


def test():
    dotnetFile = open('./12_3_2017,', 'r')
    text = dotnetFile.read()
    # 找到题目
    # mat = re.compile(r"{Title}:.*")
    # result = mat.findall(text)
    # print(result)

    # 找到题目及其第一作者
    mat_title_author = re.compile(
        r"{Title}:[^\n]*\n[^\n]*\n{Author}:[^\n]*", re.S)
    result = mat_title_author.findall(text)
    strs = result[0].split('\n')
    title = strs[0][9:]
    author = strs[2][10:]
    mat_year = re.compile(r"{Year}:.*")
    result = mat_year.findall(text)
    year = result[0][8:]
    print(title, author, year)


def NetfileParse(filename):

    dotnetFile = open(filename, 'r')
    text = dotnetFile.read()

    # 找到题目及其第一作者
    mat_title_author = re.compile(
        r"{Title}:[^\n]*\n[^\n]*\n{Author}:[^\n]*", re.S)
    result1 = mat_title_author.findall(text)
    mat_year = re.compile(r"{Year}:.*")
    result2 = mat_year.findall(text)
    for r1, r2 in zip(result1, result2):
        strs = r1.split('\n')
        title = strs[0][9:]
        author = strs[2][10:]
        year = r2[8:]
        yield (title, author, year)

if __name__ == "__main__":
    for x in NetfileParse('./12_3_2017,'):
        print(x)
