# Uses web scraper to download xkcd comics based off of user input
# to determine how many comics should be downloaded

import os, sys, requests, bs4

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

url = "https://xkcd.com/"
# creates ./xkcd directory to save images to
os.makedirs("xkcd", exist_ok=True)

# parses the initial xkcd homepage via its url
print("Downloading page %s..." % url)
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
    sys.exit(1)
soup = bs4.BeautifulSoup(res.text, "html.parser")

# finds the comic image url
comic = soup.select("#comic img")
if comic == []:
    print("Could not find comic image.")
else:
    comicSrc = "https:" + comic[0].get("src")

# downloads image from comic image url
print("Downloading image %s..." % comicSrc)
res = requests.get(comicSrc)
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
    sys.exit(1)

# saves the image to ./xkcd
imageFile = open(os.path.join("xkcd", os.path.basename(comicSrc)), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

print("Done.")