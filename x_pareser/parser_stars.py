import re


class RegexExpression:
    MAP_PATTERN = re.compile(r'\d+')
    ALF_COORD_PATTERN = re.compile(r'\d{1,2}:[ ]?\d{1,2}:[ ]?\d{1,2}\.\d')
    DEL_COORD_PATTERN = re.compile(r'([+-]){1}[ ]?\d{1,2}:[ ]?\d{1,2}:[ ]?\d{1,2}')
    L_COORD_PATTERN = re.compile(r'([+-])?\d+\.\d{2}')
    B_COORD_PATTERN = re.compile(r'([+-])?\d+\.\d{2}')
    TYPE_PATTERN = re.compile(r'[ ]?(\w*)')
    M_PATTERN = re.compile(r'\d\.\d{1,2}')
    SP_PATTERN = re.compile(r'[OBACFSGKM][0-9]?([.][0-9])?')
    N_ALF_PATTERN = re.compile(r'([+-])?\d\.\d{3}')
    N_DEL_PATTERN = re.compile(r'([+-])?\d\.\d{3}')
    PAR_PATTERN = re.compile(r'\d*')
    VR_PATTERN = re.compile(r'([+-])\d{3}')
    HD_PATTERN = re.compile(r'\d+')
    FL_PATTERN = re.compile(r'\d*')


class ReaderBrightStars:
    def __init__(self, star_str):
        self._star_str = star_str
        self._map = None
        self._alf_coord = None
        self._del_coord = None
        self._l_coord = None
        self._b_coord = None
        self._type = None
        self._m = None
        self._sp = None
        self._n_alf = None
        self._n_del = None
        self._par = None
        self._hd = None
        self._fl = None

    def read(self):
        str_pos = 0
        str_pos = self._read_map(str_pos)
        str_pos = self._read_alf_coord(str_pos)
        str_pos = self._read_del_coord(str_pos)
        str_pos = self._read_l_coord(str_pos)
        str_pos = self._read_b_coord(str_pos)
        str_pos = self._read_type(str_pos)
        str_pos = self._read_m(str_pos)
        str_pos = self._read_sp(str_pos)
        str_pos = self._read_n_alf(str_pos)
        str_pos = self._read_n_del(str_pos)

        return self

    def _read_map(self, str_pos):
        _match = RegexExpression.MAP_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._map = int(_match.group(0))
        return str_pos

    def _read_alf_coord(self, str_pos):
        _match = RegexExpression.ALF_COORD_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._alf_coord = tuple(map(float, _match.group(0).split(':')))
        return str_pos

    def _read_del_coord(self, str_pos):
        _match = RegexExpression.DEL_COORD_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        sd = _match.group(0).split(':')
        self._del_coord = (sd[0][0], float(sd[0][1:]), float(sd[1]), float(sd[2]))
        return str_pos

    def _read_l_coord(self, str_pos):
        _match = RegexExpression.L_COORD_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._l_coord = float(_match.group(0))
        return str_pos

    def _read_b_coord(self, str_pos):
        _match = RegexExpression.B_COORD_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._b_coord = float(_match.group(0))
        return str_pos

    def _read_type(self, str_pos):
        _match = RegexExpression.TYPE_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._type = _match.group(0)
        return str_pos

    def _read_m(self, str_pos):
        _match = RegexExpression.M_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._m = float(_match.group(0))
        return str_pos

    def _read_sp(self, str_pos):
        _match = RegexExpression.SP_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._sp = _match.group(0)
        return str_pos

    def _read_n_alf(self, str_pos):
        _match = RegexExpression.N_ALF_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._n_alf = float(_match.group(0))

        return str_pos

    def _read_n_del(self, str_pos):
        _match = RegexExpression.N_DEL_PATTERN.search(self._star_str[str_pos:])
        str_pos += _match.end()
        self._n_del = float(_match.group(0))
        return str_pos

    @property
    def map(self):
        return self._map

    @property
    def alf_coord(self):
        return self._alf_coord

    @property
    def del_coord(self):
        return self._del_coord

    @property
    def l_coord(self):
        return self._l_coord

    @property
    def b_coord(self):
        return self._b_coord

    @property
    def type(self):
        return self._type

    @property
    def m(self):
        return self._m

    @property
    def sp(self):
        return self._sp

    @property
    def n_alf(self):
        return self._n_alf

    @property
    def n_del(self):
        return self._n_del
