# -*- coding: utf-8 -*-

import math
import random
import colorsys

def init(world):
    """Color of an agent, random hue, full saturation and colorness."""
    return [int(math.floor(i*256)) for i in (list(colorsys.hsv_to_rgb(random.random(), 1.0, 1.0))+[1.0])]
