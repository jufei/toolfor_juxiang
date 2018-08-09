import os


def is_sushu(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


def get_sushu():
    return [x for x in range(1000) if is_sushu(x)]


print(get_sushu())


def get_all_sub_item(num):
    pass


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

print(fenshu('1/2') + fenshu('1/3'))
print(fenshu('1/2') - fenshu('1/3'))
print(fenshu('3/2') * fenshu('5/6'))
