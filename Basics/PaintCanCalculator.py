def getCans(height, width):
    print(round((height*width)/CoveragePerCan))


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# in Square Meters
CoveragePerCan = 5


getCans(height=test_h, width=test_w)
