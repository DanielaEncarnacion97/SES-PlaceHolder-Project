# OneStop: Shopping List with React.js and Flask backend

Create a grocery list and compare prices from Walmart and Target to see which option is more affordable overall.

Front end implemented with React.js (v15) and Twitter Bootstrap (v3). Back end implemented with python and run on Flask. Created for Capital One Software Engineering Summit, January 2020.

Uses Webpack, Yarn.


# Running the Back End
Clone this repository and navigate into the directory.

Install dependencies using the provided `requirements.txt`

Run `python3 __init__.py` (those are double underscores on each side). 

Open http://localhost:5000 in a web browser.


# Running the Front End

## Install
`npm install -g yarn` (use `sudo` if this gives you problems)

`yarn install`

## What is Yarn?
https://code.facebook.com/posts/1840075619545360
https://scotch.io/tutorials/yarn-package-manager-an-improvement-over-npm

## Run
`npm start` (May need to run `npm install` first)

Open http://localhost:8080 in a web browser.

## Build
`npm run build`

# More Information about the Application
1. Enter each item that you are planning to buy on your shopping trip
2. For each item, the backend code searches up the item on the Target and Walmart websites and web scrapes the data of the first few items
3. For Target and Walmart, all items are compared to find the one that has the lowest listed price. The item’s name from the website is cross referenced with the user inputted item name to verify its relevance.
4. The cheapest item (and its data) from both stores is sent back to the front end, with a note of which store offered the cheaper item
5. The app will calculate the total cost of your shopping trip for both stores and display this in its UI, allowing the user to see which store yields the lower total price.
