#-*-coding:utf-8 -*-

def count_words(test_file):
    try:
        with open(test_file)as len_test:
            len_date=len_test.read()
    except IOError:
        msg='文件的路径不对'
        print msg
    else:
        words=len_date.split()
        num_words=len(words)
        print '字符的数量为：'+str(num_words)


test = 'F:\pi_digits.txt'
count_words(test)