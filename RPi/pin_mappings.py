# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import functools
from copy import deepcopy
from OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 12,
        5: 11,
        7: 6,
        8: 198,
        10: 199,
        11: 1,
        12: 7,
        13: 0,
        15: 3,
        16: 19,
        18: 18,
        19: 15,
        21: 16,
        22: 2,
        23: 14,
        24: 13,
        26: 10
    },

    # BCM pin to actual GPIO pin
    BCM: {
        3: 227,
	5: 226,
	7: 362,
	11: 229,
	13: 228,
	15: 231,
	19: 98,
	21: 99,
	23: 97,
	27: 143,
	29: 37,
	31: 37,
	33: 38,
	35: 39,
	37: 101,
	8: 354,
	10: 355,
	12: 100,
	16: 361,
	18: 68,
	22: 230,
	24: 96,
	26: 102,
	28: 142,
	32: 34,
	36: 35,
	38: 32,
	40: 33
    },

    SUNXI: _sunXi(),

    # User defined, initialized as empty
    CUSTOM: {}
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)
