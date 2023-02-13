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

Before writing any of the actual code for the Beauty Broker website, I took some time to evalaute what users would typically expect from a restaurant website. I used GitHub's Project's feature to create a User Stories board that I updated as I went along to keep track of the User Goals that I had decided upon.

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

- To create an aesthetic website to draw the eye of customers
- To create a website that showcases and promotes the range of effective skincare on offer
- To provide a way for users to purchase the skincare products available
- To be able to track orders made through the website
- To be able to manage the range of skincare on offer
- To provide meaningful information for users that allows them to select skincare right for them, encouraging them to shop with us again
- To encourage users to return to the site via email subscriptions
- To present the skincare available in a way easy to navigate to retain user attention
- To provide a site with high user experience to retain users
- To provide a means of web marketing to customers through emails and Facebook page

### Iterations

To take an Agile approach to the project, I planned the stages that I would carry out the work. I categorised each User Story into 'must have', 'Could have' and 'Should have' and almost all of them fell into one of the 5 Epics.

At this stage in the Beauty Broker website, I completed all user stories apart from a couple of the 'could have items', which I decided were outside the scope for this sprint of the project.

However, I did end up completing the user story for viewing blog posts via the implementation of the 'skincare secrets'. When carrying out user testing, I found that some of my family/friends did not know much about skincare products or what they would need to look for. This made the user story for viewing skincare blog posts more important to me, as I wanted users to be able to choose their skincare products with confidence. I also decided this was a good move for the store as an informed user is more likely to make a purchase, and return to the site in the future if they found it helpful!

#### Iteration 1
Iteration 1 was mainly setting up the website and incorporating essential functionalities that were needed to build the rest of the project such as accounts and navigation via the main navbar. I completed the bulk of the Viewing and Navigation epic within this iteration.

Thanks to Django and utlising all-auth, setting up the apps and user accounts was accomplished relatively quickly. This allowed me to add basic product and product detail views within this iteration.

<br>

<details><summary>Iteration 1</summary>

![Iteration 1](images/iteration1.png)

</details>

<br>

#### Iteration 2
Iteration 2 focused on the epic for Searching and Sorting items. It was very time consuming sorting products by skincare, category, skin type and implementing the search functionality, thus consituted a whole iteration!

<details><summary>Iteration 2</summary>

![Iteration 2](images/iteration2.png)

</details>

<br>

#### Iteration 3
Iteration 3 was also a large iteration. It focused on the Purchasing and Checkout epic, including the bag functionality.

<details><summary>Iteration 3</summary>

![Iteration 3](images/iteration3.png)

</details>

<br>

#### Iteration 4
Iteration 4 moved away from shopper user stories and brought the focus to the Admin and Store Management epic. In this iteration I implemented the CRUD functionality for store owners to manage the range of skincare products within their store.

<details><summary>Iteration 4</summary>

![Iteration 4](images/iteration4.png)

</details>

<br>

#### Iteration 5
After all the 'essential' e-commerce functionalities were completed, I used iteration 5 to introduce extra features to add value to the user.
I added the wishlist functionality, brand focus and skin secrets pages. The features introduced in this implementation of the project help to make the Beauty Broker site more educational for its users and help them to understand the products they're buying, and encourage them to return!

<details><summary>Iteration 5</summary>

![Iteration 4](images/iteration5.png)

</details>

<br>

### First Time Visitors

- Visitors are greeted by an elegant landing page, where the purpose of the site as a skincare retailer is clear
- The home page shows the key features of the webite - shopping skincare, information on brands, skincare tips and the ability to sign up to a newsletter, with linke to the relative pages
- The navbar is clearly positioned and laid out
- The users have a choice about how they want to shop for their products- by product type, skin type and sorting by price etc
- First time users that are not familiar with skincare are able to access information about basic skincare routines, the different product types
- The Skin Secrets page also directs users to other high quality websites so they can learn more about what products and ingredients they might want
- First time visitors are encouraged to return to the site via web marketing in the form of email subscriptions and a Beauty Broker Facebook page
- Flash messages help instill user confidence in the site
- First time visitors can easily register for an account
- Visitors have the option to purchase without havign to go through the process of making an account if they so choose


### Returning Visitors

- Returning visitors can quickly navigate to their favourite products via searchin, product categorising and sorting
- Returning visitors can log into their account to see their previous orders
- Returning visitors have a faster time going through checkout if they have saved information to their profile
- Returning visitors can view their wishlist to refresh themselves on items they want to purchase

### User Journey

1. As a user, the landing page informs me that I am on the Beauty Broker website and the key words I can see tell me this is a skincare website
2. The homepage shows that I can shop skincare, view featured brands, signup to a newsletter or view more information about skincare products
3. I can see a clear navigation menu at the top of the page, with a search bar. The icons show me that I can create an account, and that I shopping bag tells me that I have an empty shopping bag
4. The options on the navigation menu show me that I can access the products through product category, by skin concern or view all products.
5. I don't know much about skincare so I click to take me to the page that will give me more information on this.
6. After reading the page and selecting the links I think will be useful to me, I have an idea about what type of products I need in my routine and the types of ingredients I want in them.
7. I want something to help with my dry skin so I click the option to show me products for dry skin.
8. When I click on the product I want, a page tells me information about it including ingredients so I can check if it has a specific ingredient I'm after (e.g. hyaluronic acid for dry skin). I can add the selected item with my bag, with the option of amending the quantity if I want. A message at the top tells me I have successfully added my chosen quantity to my shopping bag.
9. I hit the keep shopping button and select a further few items.
10. When I am finished selecting my products, I go into my shopping bag and double check what I am about to buy before going to checkout.
11. Upon arriving on the checkout page, I see that if I create an account then I can save my information for future, so I decide to register.
12. After confirming with via a confirmation email I have an account!
13. I go to fill in the checkout form, which lets me know which fields I MUST fill in and highlights if I make any errors.
14. After entering my information correctly, there is a short loading screen then I am met with a page that confirms my order has been successful!
15. When I go in to my account section, I can see the order I have just created and the delivery information that I asked to save.

Whilst planning the functionality for the Beauty Broker website, I had to consider how I was going to achieve both the aims for the user and the restaurant. This led to the creation of the features found in the Features section.