para = """Devices have been used to aid computation for thousands of years, 
mostly using one-to-one correspondence with fingers. The earliest 
counting device was probably a form of tally stick. Later record 
keeping aids throughout the Fertile Crescent included calculi (clay 
spheres, cones, etc.) which represented counts of items, probably 
livestock or grains, sealed in hollow unbaked clay containers.[4][5] 
The use of counting rods is one example."""

print(para[0]) # 8 include |  11 exclusive
"""
    Slicing 
        -> [0] => get character at index 0
        -> [:8] => start from very beginning up to 7 ( last index is exclusive )
        -> [8:] => start from index 8 up to the last
        -> [2:8] => Range between index 2 to 7
        -> [:] => all together
"""
# print(len(para));
# print(para[len(para)-2])