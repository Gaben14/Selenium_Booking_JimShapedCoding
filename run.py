from booking.booking import Booking
import time

# Teardowns (def __exit__ method from booking class) will automatically
# be executed once Python executes the methods under the with section
with Booking() as bot:
    bot.land_first_page()
    bot.change_currency("USD")
    bot.select_place_to_go("New York")
    bot.select_dates("2023-05-22", "2023-05-25")  # Date format: 2023-05-21
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()

    time.sleep(5)
