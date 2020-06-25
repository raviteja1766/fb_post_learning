import enum

from ib_common.constants import BaseEnumClass


class ReactionType(BaseEnumClass, enum.Enum):
    WOW = 'WOW'
    LIT = 'LIT'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'
    THUMBS_DOWN = 'THUMBS-DOWN'
    ANGRY = 'ANGRY'
    SAD = 'SAD'
