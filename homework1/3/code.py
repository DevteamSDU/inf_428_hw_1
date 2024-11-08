import math


def transform_time_to_cyclic(time):
    sin_time = math.sin(2 * math.pi * time / 24)
    cos_time = math.cos(2 * math.pi * time / 24)
    return sin_time, cos_time
