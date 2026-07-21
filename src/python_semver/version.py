import re


class Version:
    _NUM = "[0-9]|[1-9][0-9]+"
    _VER_CORE = re.compile(
        rf"({_NUM})\.({_NUM})\.({_NUM})")

    def __init__(self, verstr):
        match = self._VER_CORE.fullmatch(verstr)
        if not match:
            raise ValueError()

        self.major = int(match.group(1))
        self.minor = int(match.group(2))
        self.patch = int(match.group(3))