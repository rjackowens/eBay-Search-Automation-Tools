from time_left_converter import timeLeftString

# Examples for testing
variation_1 = "P0DT23H4M6S" # Single day = 0
variation_2 = "P2DT18H45M11S" # Single day = 2
variation_3 = "P7DT3H43M33S" # Single hour = 3

def daySorter(x):
    switcher = {
        0: 0,
        1: 10000,
        2: 20000,
        3: 30000,
        4: 40000,
        5: 50000,
        6: 60000,
        7: 70000,
        8: 80000,
        9: 90000,
        10 : 100000
    }
    return (switcher.get(x))

def hourSorter(x):
    switcher = {
        0: 0,
        1: 100,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600,
        7: 700,
        8: 800,
        9: 900,
        10: 1000,
        11: 1100,
        12: 1200,
        13: 1300,
        14: 1400,
        15: 1500,
        16: 1600,
        17: 1700,
        18: 1800,
        19: 1900,
        20: 2000,
        21: 2100,
        22: 2200,
        23: 2300
    }
    return (switcher.get(x))

def minuteSorter(x):
    switcher = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59
    }
    return (switcher.get(x))

def valueGenerator(x):
    day = daySorter(int(timeLeftString(x)['days']))
    hour = hourSorter(int(timeLeftString(x)['hours']))
    minute = minuteSorter(int(timeLeftString(x)['minutes']))
    value = day + hour + minute
    return value
    
print(valueGenerator(variation_1))

