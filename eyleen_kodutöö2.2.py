def validate_pin(pin):
    if len(pin) in (4, 6) and pin.isdigit ():
        return True
    else:
        return False
        