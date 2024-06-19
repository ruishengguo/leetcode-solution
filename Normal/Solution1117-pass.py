# 1117、H2O生成
from typing import Callable


class H2O:
    def __init__(self):
        self.quene = []
        self.g = self.barrier()
        next(self.g)
        self.o = None
        self.h = None

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        if self.decision(releaseHydrogen):
            self.h()
            return
        else:
            self.h = releaseHydrogen
            self.g.send('H')
            return
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        # releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        if self.decision(releaseOxygen):
            self.o()
            return
        else:
            self.o = releaseOxygen
            self.g.send('O')
            return
        # releaseOxygen() outputs "O". Do not change or remove this line.
        # releaseOxygen()

    def barrier(self):
        while True:
            y = yield
            self.quene.append(y)
            if self.quene.count('O') >= 1 and self.quene.count('H') >= 2:
                self.hydrogen(self.marker)
                self.oxygen(self.marker)
                self.hydrogen(self.marker)
                self.quene.remove('H')
                self.quene.remove('H')
                self.quene.remove('O')

    def marker(self):
        pass

    def decision(self, func_):
        return func_ == self.marker
