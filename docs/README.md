# Beauty Broker.

### An online beauty retailer for skincare lovers!

## Contents
- [About](#about)
- [User Experience](#user-experience)
    - [Target audiences](#target-audiences)
    - [User Stories](#user-stories)
    - [Beauty Broker's Aims](#beauty-brokers-aims)
    - [Iterations](#iterations)
    - [First Time Visitors](#first-time-visitors)
    - [Returning Visitors](#returning-visitors)
    - [User Journey](#user-journey)
    - [Colour Scheme and Fonts](#colour-scheme-and-fonts)
    - [Wireframes](#wireframes)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## About

![Am I responsive screenshot](images/am-i-responsive.png)

Beauty Broker is a website for a fictional online skincare retailer, aimed at those with a love for skincare. The code was written in Gitpod, with the repository stored in GitHub and hosted on Heroku with an Elephant SQL PostGreSQL database.

This site was born out of my own love and interest in skincare having battled through acne and hyperpigmentation. The knowledge I have gained through research and watching some of my favourite 'Skinfluencers' (featured in the Skincare Secrets page) has really improved not only the condition of my skin but also my self-confidence. Beauty Broker aims to provide shoppers with not only a range of highly rated skincare products to purchase, but also equip them with the knowledge of how to use these products to transform their skin and their own self-confidence.

Potentail customers can easily navigate to find the product they are looking for by shopping by product type or skin type as well as sorting by price/category/rating. The website also aims to empower it's users by providing information they might find useful when shopping for skincare such as what ingredients to look for, suggesting products for their skin type and providing them with a suggested basic skincare routine.

The site provides full e-commerce purchasing functionality to support both shoppers and store owners in tracking orders through the use of accounts and webhooks.

Store owners can also use the site to control their product tool, allowing them to provide shoppers with the latest in skincare trends and keep up with new product releases. They can also edit and remove existing lines.

The Beauty Broker website was made with the Django framework and largely utilises HTML, CSS, Python and components of Javascript/jQuery.

A link to the live site can be found [here](https://beauty-broker.herokuapp.com/).

## User Experience

### Target Audiences

- Primarily aimed at adults and young adults who want to take care of their skin
- For users with an existing knowledge of skincare
- For users with an existing skincare routine looking to add new products
- For users with no knowledge skincare
- For those wanting to target a particular skin concern i.e. blemish prone skin
- For users wanting to purchase new skincare products now
- For users wanting to browse their next skincare purchase
- For users wanting to research skincare
- For users wanting to subscribe to a newsletter

### User Stories

Before beginning to code the Beauty Broker website, I took some time to reflect on what it was that users would expect from a skincare website. I used GitHub's Projects feature to create a User Stories board to list all of the user goals I had come up with, and the epics that the vast majority of these would fall under.

Before writing any of the actual code for the Sushi & Sake website, I took some time to evalaute what users would typically expect from a restaurant website. I used GitHub's Project's feature to create a User Stories board that I updated as I went along to keep track of the User Goals that I had decided upon.

![Screenshot of user stories board](images/user-stories-1.png)
![Screenshot of user stories board](images/user-stories-2.png)

1. Epic - Registration and User Accounts
    - User - create a wishlist
    - User - recieve a confirmation email after registering
    - User - be able to recover my password
    - User - have my own personal account
    - User - be able to log in and out of my account
    - User - register for an account
2. Epic - Viewing and Navigation
    - Navigate easily around the sites pages
    - Be able to see a list of all products
    - Be able to view a specific product details
    - View a specific category
3. Epic - Sorting and Searching
    - User - easily see what I have searched for and the number of results returned
    - User - search for a product by name or description
    - User - sort products into different categories of skincare product
    - User - sort products into different skin types
    - User - sort the list of available products
4. Epic - Purchasing and Checkout
    - User - receive an email confirmation of my order after checking out
    - User - view order confirmation after checkout
    - User - easily enter my payment information
    - User - feel my personal information is secure
    - User - adjust the quantity of products in my bag
    - User - view items in my bag to be purchased
    - User - easily select the products I would like to purchase
5. Epic - Admin and Store Management
    - Store - delete a product
    - Store - edit/update a product
    - Store - add new products

I also considered future implementations outside the scope of this sprint:
- User - Rate a product I've purchased
- User - View skincare blog posts (I eventually decided to implement this in the current sprint so that the site could add more value to users wanting to find out more about skincare products and routines)
- User - take a skincare quiz to find out what type of skin I have

### Beauty Broker's Aims

- To create a website that echoes the vibrant atmosphere of the Sushi & Sake Japanese Kitchen and draw in new customers
- To create a website that showcases and promotes the exciting cuisine to encourage users to make bookings
- Provide guests with a way to book a table at the restaurant
- Provde the restaurant staff with the means to be able to view any bookings made
- Provide the restaurant staff with the means to be able to manage bookings
- Provide the restaurant staff with the means to be able to view any messages sent to the restaurant
- To have the use of a booking system that prevents double bookings to avoid poor experiences for customers
- The restaurant would like a way to easily manage and update their menus with the revelevant food items, prices and dietary information
- As a restaurant owner, I would like a space to promote offers and events to encourage people to come to the restaurant (future implementation)
