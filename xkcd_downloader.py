# Uses web scraper to download xkcd comics based off of user input
# to determine how many comics should be downloaded

print("How many comics you would like to download?")
print("Enter a positive number or 'All' to download all of the comics\n")

while True:
    numberOfComics = input()
    try:
        numberOfComics = int(numberOfComics)
    # if input is not a number, check if it is a valid str (all)
    except:
        # checks if input is any permutation of 'all'
        if numberOfComics.lower() != "all":
            print("Invalid input! Please enter a positive number or 'All'.\n")
        else:
            break
        continue
    # if input is a number, check if it is positive
    if numberOfComics < 1:
        print("Invalid input! Please enter a positive number or 'All'.\n")
        continue
    break

print("Input: ", numberOfComics)
