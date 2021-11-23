class Error(Exception):
    pass


class MaxOfOneDeck(Error):
    pass


class WrongPosOneDeck(Error):
    pass


class WrongPos(Error):
    pass


class PosIsBusy(Error):
    pass


class WrongPosTwoDeck(Error):
    pass


class WrongPosThreeDeck(Error):
    pass


class WrongPosFourDeck(Error):
    pass


class NotExistingPos(Error):
    pass


class DuplicationPos(Error):
    pass


class AlreadyShot(Error):
    pass


class NotAvailablePosLeft(Error):
    pass
