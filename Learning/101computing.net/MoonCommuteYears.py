commute = int(input("How many miles to work (one way): "))
annual_commute_in_miles = commute * 2 * 5 * 52
annual_commute_in_kilometers = annual_commute_in_miles * 1.609
moon_round_trip = 384400 * 2
years = moon_round_trip / annual_commute_in_kilometers

print("Your commute would take " + str(round(years, 3)) + " years to make a round trip to the moon.")