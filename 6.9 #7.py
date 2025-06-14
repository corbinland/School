def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds
def test(condition):
    if condition:
        print("Test passed")
    else:
        print("Test failed")
test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
