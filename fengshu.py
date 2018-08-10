import os

from my_math import number


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

    def __div__(self, fenshub):
        return self * fenshub.daoshu()

    def daoshu(self):
        return fenshu('{}/{}'.format(self.fenmu, self.fenzi))

    def yuefen(self):
        fenzi_sub = number(self.fenzi).fenjie()
        fenmu_sub = number(self.fenmu).fenjie()
        nfenzi, nfenmu = self.fenzi, self.fenmu
        for asub in fenzi_sub:
            if asub in fenmu_sub:
                nfenzi = int(nfenzi / asub)
                nfenmu = int(nfenmu / asub)
                fenmu_sub.remove(asub)
        return fenshu('{}/{}'.format(nfenzi, nfenmu))

# print(fenshu('1/2') + fenshu('1/3'))
# print(fenshu('1/2') - fenshu('1/3'))
# print((fenshu('3/2') * fenshu('5/6')).yuefen())
# print((fenshu('2/3') / fenshu('4/5')).yuefen())

print(fenshu('4/10').yuefen())
