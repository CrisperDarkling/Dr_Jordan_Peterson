# Dr. Jordan Peterson Bookstore

This is a Django E-Commerce site built as the final project of The Code Institute's classroom bootcamp. It's a fictional bookstore and video blog inspired by a real psychologist; Dr. Jordan Peterson.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Apps

### Home
The index.html page which serves as the first page loaded, extending from base.html. I decided to remove the index.html page and just use the about.html as the first page because I found it added nothing to my website.

### About
The about.html page, as mentioned above, is the actual landing page for this website. It also explains who Dr. Jordan Peterson is as well as what the website entails.

### Accounts
This app allows visitors to register an account, log in, view their profile (which confirms what User they are logged-in as) and log out. This allows the User to then purchase books through the bookshop and cart.

### Blogcategories
The Blogcategories app displays three of Dr. Peterson's 2017 YouTube lecture series; Maps of Meaning, Personality and its Transformations, The Psychological Significance of the Bible. The first two are psychology lectures he teaches at the University of Toronto, which he records every year to share online. The Biblical lectures were a public series started by demand because of his increasing popularity as a public speaker and lecturer.

### Blog
Once a Blogcategory is selected, the Blog app displays the lectures as a set of blogposts, each with a thumbnail, description, publish date and "Read More" button. Clicking "Read More" brings the User to a viewpost.html which displays the embedded YouTube video which can be watched on-site. There is also a "Go Back" to bring the User back one page.

### Cart
This is where the User can view and adjust the books they have selected from the products page just before clicking "Checkout" to make a purchase.

### Categories
This app displays the seven different book categories covered by this bookstore. These are:
1 - Clinical Psychology & Personality
2 - General
3 - History
4 - Jordan B Peterson
5 - Literature/Philosophy
6 - Neuroscience
7 - Religion & Religious History

### Checkout
This is where Users purchase the books they've added to their Cart. Users can adjust the quantity of each book they have selected. Here they fill out their personal and payment details to buy the books via Stripe.

### Contact
This app allows Users to fill in a form and contact the site developer. They are redirected to the landing about.html page and notified by pop-up message: "We have recieved your email & will get back to you as soon as possible!".

### Products
This app displays the books from the Category the User selected in categories.html. Each book is displayed on its own panel-card which has the Book Image, Name, Author, Price and "View Product" button. Pressing this button opens up a modal which has the same information as the panel-card, but also includes the book description and an "Add to Cart" button attached to a "Quantity" selector. "Add to Cart" will add the choosen amount of books to the User's Cart and then redirect them to the Categories page. products.html also has a "Go Back" button which will take the User back one page.

### Purchased
purchased.html is rendered once the User has successfully completed a purchase through checkout.html. A pop-up message is displayed saying "You have successfully paid".
** My original intention for this page was to provide Users with a download link containing the .pdf file for each book they had purchased,  as I have most of these books in this form. Hardcoding the download link wasn't viable, and calling the product download link with: "href="static/downloads/{{ product.download_link }}"" ended up rendering the entire library of books ![Purchased Full Render](./README-images/PurchasedFullRend.png) My lecturer said there was a simple way to provide the specific book links using URLs, but time thinned out and he got busy, and I wasn't able to figure it out, so purchased.html only confirms payment.**

### Search


## Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

This project was deployed via Heroku, and pretested using Travis CI.

## Built With

Django
HTML
CSS
Bootstrap
Python
SQLite database



## Versioning

The code was written on Cloud9 and version-controlled using github.





## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
