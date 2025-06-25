def compute_feedback(decision, open_price, close_price):
    """
    Ocena trafności decyzji na podstawie zmiany ceny:
    - BUY: oczekujemy, że close > open
    - SELL: oczekujemy, że close < open
    - HOLD: zero punktów, brak akcji
    """
    if decision == "HOLD":
        return 0.5  # neutralna decyzja
    elif decision == "BUY":
        return 1.0 if close_price > open_price else 0.0
    elif decision == "SELL":
        return 1.0 if close_price < open_price else 0.0
    return 0.0
