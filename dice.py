MAX_DICE = 6

def dice_roll():
    """Rolls a dice once

    Returns:
        _type_: int
    """
    import random
    roll = random.randint(1,MAX_DICE)
    return roll