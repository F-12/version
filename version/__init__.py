# coding:utf-8

# helper methods
class Version:

    def __init__(self, v, name='', base=10):
        '''
        create a Version instance by different ways

        a Version object represent a version for anything, such as software, libs,
        code repository and so on. A version can be comparable, computable.
        We will use an 32-bit integer to represent a version, at the same time learning
        from the representation of IP address, we can print a version as a dot-seperated
        string to increment readability.

        by integer:
            v = Version(1)
        by dot-seperated string
            v0 = Version('1.0')
            v1 = Version('1.0.1')
            v2 = Version('1.0.1.1')
        by 32-bit binay string
            v3 = Version('0b00000001000000010000000100000001',base=2)
            v4 = Version('00000001000000010000000100000001',base=2)
        '''
        self.name = name
        if type(v) is int:
            self.version = v
        if isinstance(v, str) and '.' in v:
            tokens = map(int, v.split('.'))
            assert len(tokens) <= 4 and len(
                filter(lambda t: t < 0 or t > 255, tokens)) <= 0
            v_arr = map(lambda t: format(t, '08b'), tokens) + \
                ['00000000'] * (4 - len(tokens))
            self.version = int(
                ''.join(v_arr),
                base=2)
        elif isinstance(v, str):
            self.version = int(v, base)

    def __str__(self):
        v_string = format(self.version, '032b')
        v_arr = [str(int(v_string[pos * 8:(pos + 1) * 8], base=2))
                 for pos in range(4)]
        return self.name + 'v' + '.'.join(v_arr)

    def __cmp__(self, other):
        return cmp(self.version, other.version)

    def _incr(self,level):
        self.version += 256 ** level
        return self
    def incr_significant(self):
        return self._incr(3)
    def incr_import(self):
        return self._incr(2)
    def incr_normal(self):
        return self._incr(1)
    def incr_small(self):
        return self._incr(0)
