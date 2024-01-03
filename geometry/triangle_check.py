# function to check whether three sides of given lengths can build a triangle

def triangle_check(a, b, c) -> bool:
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True

