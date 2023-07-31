# Uses web scraper to download xkcd comics based off of user input
# to determine how many comics should be downloaded

import os, requests, bs4

"""
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
"""

url = "https://xkcd.com"
os.makedirs("xkcd", exist_ok=True)

# downloads and parses the initial xkcd homepage
print("Downloading page %s..." % url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

# finds and selects the comic image
comic = soup.select("#comic img")
if comic == []:
    print("Could not find comic image.")
else:
    comicSrc = "https:" + comic[0].get("src")
    print("Comic source:", comicSrc)

print("Done.")