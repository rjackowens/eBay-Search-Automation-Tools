# Example Day Variations
variation_1 = "P0DT23H4M6S" # Single day = 0
variation_2 = "P2DT18H45M11S" # Single day = 2

# Example Hour Variations
variation_3 = "P7DT3H43M33S" # Single hour = 3
variation_4 = "P3DT14H21M33S" # Multiple hours = 14

# Example Minute Variations
variation_5 = "P2DT3H5M33S" # Single hour, Single minutes = 5
variation_6 = "P8DT6H25M33S" # Single hour, Multiple minutes = 25
variation_7 = "P3DT14H6M33S" # Multiple hours, Single minute = 6
variation_8 = "P6DT12H45M33S" # Multiple hours, Multiple minutes = 45

def timeLeftDay(x):
    x = x[1:3].replace("D","")
    return(x)

def timeLeftHour(x):
    x = x[4:6].replace("H","").replace("T","")
    return(x)

def timeLeftMinute(x):
    if len(x) == 13:
        x = x[6:9].replace("M","").replace("H","")
    else:
        x = x[6:8].replace("M","").replace("H","")
    return(x)

def timeLeft(x):
    days = timeLeftDay(x)
    hours = timeLeftHour(x)
    minutes = timeLeftMinute(x)
    if int(days) == 0:
        return(hours + "h " + minutes + "m left")
    else:
        return(days + "d " + hours + "h " + minutes + "m left")
