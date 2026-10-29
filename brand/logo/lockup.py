"""The mark beside the name, for any pair of cuts, and the rule that picks a cut for a size."""
from cuts import SQUARE, marks, words
from letters import R

MARK_SCALE, WORD_AT = 1.05, 262       # the mark is 218 units wide; the name starts 262 units in


def lockup(mark_cut, word_cut):
    mark, _ = marks()[mark_cut]
    name, (x, y, w, h) = words()[word_cut]
    body = (f'<g transform="translate(104,{-R}) scale({MARK_SCALE})">{mark}</g>'
            f'<g transform="translate({WORD_AT},0)">{name}</g>')
    return body, (-8, y, WORD_AT + w + 8, h)


def shares(word_width):
    """How much of a lockup's width the mark and the name each take."""
    total = WORD_AT + word_width
    return SQUARE[2] * MARK_SCALE * 0.92 / total, word_width / total


def choose(order, table, method, width_mm):
    """The most detailed cut, in `order`, that holds in `method` at this width. None if none does."""
    for name in order:
        least = table[name][method]
        if least is not None and least <= width_mm:
            return name
    return None
