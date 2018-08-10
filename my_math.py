import sys


class number(object):

    def __init__(self, num):
        self.num = num

    def is_sushu(self):
        if self.num == 1:
            return False
        elif self.num in [2, 3]:
            return True
        else:
            for i in range(2, self.num):
                if self.num % i == 0:
                    return False
            return True

    def is_heshu(self):
        return not self.is_sushu()

    def sushu_list(self):
        return [x for x in range(2, self.num) if number(x).is_sushu()]

    def fenjie(self):
        if self.num == 1:
            return []
        else:
            sub = []
            tmp_num = self.num
            while number(tmp_num).is_heshu():
                for su_shu in number(tmp_num).sushu_list():
                    if tmp_num % su_shu == 0:
                        sub.append(su_shu)
                        tmp_num = int(tmp_num / su_shu)
                        break
            sub.append(tmp_num)
            return sorted(sub)

if __name__ == '__main__':
    # number(4).fenjie()
    # for i in range(1, 100):
    #     print('check {}'.format(i))
    #     if number(i).is_sushu():
    #         print('{} is sushu.'.format(i))
    # print(number(4).sushu_list())

    for i in range(100):
        if number(i).is_heshu():
            print(i)
            print('{}  fenjie wei: {}'.format(i, number(i).fenjie()))
    # print(number(4).fenjie())
    # print(number(6).sushu_list())
    print(number(6).fenjie())

