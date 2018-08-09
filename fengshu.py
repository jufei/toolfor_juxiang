import os


def is_sushu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_sushu(num):
    return [x for x in range(2, num) if is_sushu(x)]


def get_subnum(num):
    sub = []
    tmp_num = num
    while not is_sushu(tmp_num):
        for su_shu in get_sushu(tmp_num):
            if num % su_shu == 0:
                sub.append(su_shu)
                tmp_num = int(tmp_num / su_shu)
    return sorted(sub)

print(get_subnum(100))


class fenshu(object):

    def __init__(self, value):
        if '/' in value:
            self.fenzi = int(value.split('/')[0])
            self.fenmu = int(value.split('/')[1])
        else:
            raise Exception('Invalid Fenshu, it should be a/b')

    def __repr__(self):
        return '{}/{}'.format(self.fenzi, self.fenmu)

    def __str__(self):
        return self.__repr__()

    def find_subitem(self, a, b):
        pass

    def __add__(self, fenshub):
        fenzi = self.fenzi * fenshub.fenmu + fenshub.fenzi * self.fenmu
        fenmu = self.fenmu * fenshub.fenmu
        return fenshu('{}/{}'.format(fenzi, fenmu))

    def __sub__(self, fenshub):
        fenzi = self.fenzi * fenshub.fenmu - fenshub.fenzi * self.fenmu
        fenmu = self.fenmu * fenshub.fenmu
        return fenshu('{}/{}'.format(fenzi, fenmu))

    def __mul__(self, fenshub):
        fenzi = self.fenzi * fenshub.fenzi
        fenmu = self.fenmu * fenshub.fenmu
        return fenshu('{}/{}'.format(fenzi, fenmu))

    def yuefen(self):
        fenzi_sub = get_subnum(self.fenzi)
        fenmu_sub = get_subnum(self.fenmu)
        nfenzi, nfenmu = self.fenzi, self.fenmu
        for asub in fenzi_sub:
            if asub in fenmu_sub:
                nfenzi = int(nfenzi / asub)
                nfenmu = int(nfenmu / asub)
                fenmu_sub.remove(asub)
        return fenshu('{}/{}'.format(nfenzi, nfenmu))

print(fenshu('1/2') + fenshu('1/3'))
print(fenshu('1/2') - fenshu('1/3'))
print((fenshu('3/2') * fenshu('5/6')).yuefen())
