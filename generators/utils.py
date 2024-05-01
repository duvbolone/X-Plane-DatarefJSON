def progressbar(percent: float):
    empty = "░"
    full = "█"
    f = empty*10
    f = f.replace(empty, full, round(max(min(percent, 100), 0) / 10))

    return f