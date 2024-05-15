"""Many vehicle owners record the fuel efficiency of their vehicles as a way to track the health of 
the vehicle. If the fuel efficiency of a vehicle suddenly drops, there is probably something wrong 
with the engine or drive train of the vehicle. In the United States, fuel efficiency for gasoline 
powered vehicles is calculated as miles per gallon. In most other countries, fuel efficiency is 
calculated as liters per 100 kilometers. The formula for computing fuel efficiency in miles per 
gallon is the following:

mpg = end − start / gallons

where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.
The formula for converting miles per gallon to liters per 100 kilometers is the following:

lp100k = 235.215 / mpg"""


def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input("Enter the starting odometer (miles): "))

    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input("Enter the ending odometer (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon\n{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = float(end_miles - start_miles) / amount_gallons

    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg

    return lp100k


# Call the main function so that
# this program will start executing.
main()
