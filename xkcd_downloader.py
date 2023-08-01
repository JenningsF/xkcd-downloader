# Uses web scraper to download xkcd comics based off of user input
# to determine how many comics should be downloaded

import os, sys, requests, bs4

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

url = "https://xkcd.com/"
# creates ./xkcd directory to save images to
os.makedirs("xkcd", exist_ok=True)

# while not url.endswith('#'):
for _ in range(numberOfComics):
    # parses the xkcd homepage via its url
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

    # retrieves the comic number for the filename to assist in image ordering
    comicNumber = soup.find(id="middleContainer").findAll('a')
    comicNumber = comicNumber[-2].get("href")
    comicNumber = comicNumber.rsplit('/', 1)[-1]
    filename = comicNumber + "_" + os.path.basename(comicSrc)

    # saves the image to ./xkcd
    imageFile = open(os.path.join("xkcd", os.path.basename(filename)), 'wb')
    try:
        with open(os.path.join("xkcd", os.path.basename(filename)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
        print("Successfully saved image %s!" % filename)
    except IOError as err:
        print("Error in saving image: %s" % (err))
    imageFile.close()

    # get the previous button's url to navigate to the previous comic
    prevLink = soup.select("a[rel='prev']")[0]
    url = "https://xkcd.com" + prevLink.get("href")

print("Done.")