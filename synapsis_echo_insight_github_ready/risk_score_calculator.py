
import numpy as np

def calculate_atr(klines, period=14):
    if len(klines) < period + 1:
        return 0.0

    trs = []
    for i in range(1, period + 1):
        high = klines[-i]['high']
        low = klines[-i]['low']
        prev_close = klines[-i - 1]['close']
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        trs.append(tr)

    return np.mean(trs)

def normalize_risk_score(atr, scale=1000):
    return min(1.0, atr / scale)
