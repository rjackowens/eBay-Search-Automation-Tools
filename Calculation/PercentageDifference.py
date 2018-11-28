average_active_price = 1023.0
average_sold_price = 816.46

percent_decrease = (average_sold_price - average_active_price)
percent_increase = ((average_sold_price/average_active_price) * 100)

print ("\nPercent decrease: " + str(round(percent_decrease, 4)) + ("%"))
print ("Percent increase: " + str(round(percent_increase, 4)) + ("%"))


# def percent_change(average_active_price, average_sold_price):
#     if average_active_price == average_sold_price:
#         return 100.0
#     try:
#         return (abs(average_active_price - average_sold_price) / average_sold_price) * 100.0
#     except ZeroDivisionError:
#         return 0
# print (percent_change)