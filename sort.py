VOLUME_THRESHOLD = 1_000_000
DIMENSION_THRESHOLD = 150
MASS_THRESHOLD = 20

STANDARD_TYPE = "STANDARD"
SPECIAL_TYPE = "SPECIAL"
REJECTED_TYPE = "REJECTED"

def is_bulky(width: float, height: float, length: float) -> bool:
    volume = width * height * length
    return volume >= VOLUME_THRESHOLD or max(width, height, length) >= DIMENSION_THRESHOLD
    

def is_heavy(mass: float) -> bool:
    return mass >= MASS_THRESHOLD
    

def is_standard(width: float, height: float, length: float, mass: float):
    return not is_bulky(width, height, length) and not is_heavy(mass)


def is_rejected(width: float, height: float, length: float, mass: float):
    return is_bulky(width, height, length) and is_heavy(mass)


def sort(width: float, height: float, length: float, mass: float) -> str:

    if is_standard(width, height, length, mass):
        return STANDARD_TYPE
    elif is_rejected(width, height, length, mass):
        return REJECTED_TYPE
    return SPECIAL_TYPE