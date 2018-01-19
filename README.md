# Dr. Jordan Peterson Bookstore

This is a Django E-Commerce site built as the Stream 3 project of The Code Institute's classroom bootcamp. It's a fictional bookstore and video blog inspired by a real psychologist; Dr. Jordan Peterson.


## Live Demo

Here is the link for the Heroku-deployed website https://dr-jordan-peterson-bookstore.herokuapp.com/


## Apps

### Home

The index.html page which serves as the first page loaded, extending from base.html. I decided to remove the index.html page and just use the about.html as the first page because I found it added nothing to my website.


### About

The about.html page, as mentioned above, is the actual landing page for this website. It also explains who Dr. Jordan Peterson is as well as what the website entails.

### Accounts

This app allows visitors to register an account, log in, view their profile (which confirms what User they are logged-in as) and log out. This allows the User to then purchase books through the bookshop and cart.


### base.html

This formed the base-layer of the website. It contains the Navbar, background picture and Footer. The Top-Navbar contains links to Register & Log-in // Profile & Log-out, Cart, the Search box, and the Bottom-Navbar contains links to About, Book Store and YouTube Series.
The Footer contains links to Jordan Peterson's sites and social media accounts: JordanPeterson.com, Facebook, YouTube, Twitter, Patreon, Research Gate, Soundcloud and Reddit. It also contains the "Contact Us" link. 


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

**My original intention for this page was to provide Users with a download link containing the .pdf file for each book they had purchased,  as I have most of these books in this form. Hardcoding the download link wasn't viable, and calling the product download link with: "href="static/downloads/{{ product.download_link }}"" ended up rendering the entire library of books like this: ![Rend](https://s3-eu-west-1.amazonaws.com/jordan-peterson-bookstore/static/images/PurchasedFullRend.png "Full library download rendering")My lecturer said there was a simple way to provide the specific book links by routing via URLs, but time thinned out and he got busy, and I wasn't able to figure it out, so purchased.html only confirms payment with the pop-up message.**


### Search

This app allows Users to search the website, although I have realised too late that this function is incomplete.


## Prerequisites

Here is a list of software required to build this website:

Django==1.11.7

Pillow==4.3.0

boto==2.48.0

boto3==1.4.8

botocore==1.8.13

dj-database-url==0.4.2

django-forms-bootstrap==3.1.0

django-storages==1.6.5

docutils==0.14

gunicorn==19.7.1

jmespath==0.9.3

olefile==0.44

psycopg2==2.7.3.2

python-dateutil==2.6.1

pytz==2017.3

s3transfer==0.1.12

stripe==1.75.1


## Deployment

This project was deployed via Heroku, and pretested using Travis CI.


## Static File Storage

An amazon AWS S3 Bucket was used to host all of the static files.


## Built With

Django

HTML

CSS

Bootstrap

Python

SQLite database


## Versioning

The code was written on Cloud9 and version-controlled using github https://github.com/CrisperDarkling/Dr_Jordan_Peterson


## Project Management

I used the Asana website and app to manage my project tasks from beginning to end. I had multiple column headings under which I could easily create, alter and move tasks around.


My complete tasks:

![AsanaComp](https://s3-eu-west-1.amazonaws.com/jordan-peterson-bookstore/static/images/Asana_JPB_com.png "Asana Complete Tasks")


My incomplete tasks:

![AsanaIncomp](https://s3-eu-west-1.amazonaws.com/jordan-peterson-bookstore/static/images/Asana_JPB_incom.png "Asana Incomplete Tasks")


## Acknowledgments

I must acknowledge:

- Richard Dalton & Matt Rudge (Lecturers) and Katie Maxwell & Neil McEwen (Teaching Assitants) for all their teaching, support and coding wisdom throughout this coding course.
- My class mates for their high-spirits, help and hard work.
- Dr. Jordan Peterson for being an awesome inspiration.




<!--```-->
<!--Give examples-->
<!--```-->

<!--### Installing-->

<!--A step by step series of examples that tell you have to get a development env running-->

<!--Say what the step will be-->

<!--```-->
<!--Give the example-->
<!--```-->

<!--And repeat-->

<!--```-->
<!--until finished-->
<!--```-->

<!--End with an example of getting some data out of the system or using it for a little demo-->

<!--## Running the tests-->

<!--Explain how to run the automated tests for this system-->

<!--### Break down into end to end tests-->

<!--Explain what these tests test and why-->

<!--```-->
<!--Give an example-->
<!--```-->

<!--### And coding style tests-->

<!--Explain what these tests test and why-->

<!--```-->
<!--Give an example-->
<!--```-->
