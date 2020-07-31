# Pizza House

... This is a website made for people who love to order food from home.
... You will find every type of fast food here for a good price and a 
... easy way on ordering them.

## UX

### User Stories

* User story 1 : I can see info about the company.
* User story 2 : I can navigate to cart, menu or my account through the navbar.
* User story 3 : When I am in menu I can choose what type of food I want to order.
* User story 4 : I can add the food to the cart and I can choose the quantity
* User story 5 : I can see selected food, price and delivery price in the cart page .
* User story 6 : I can update quantity and delete food items from the cart.
* User story 7 : I can create my own account.
* User story 8 : I can login and logout to my account.
* User story 9 : My order details in the cart is saved to my account.
* User story 10 : I can fill my delivery details in the checkout page.
* User story 11 : I can pay with Stripe.
* User story 12 : I can see a successful order message and order details after payment.
* User story 13 : I can see my order history in my profile page if I am logged in.
* User story 14 : As an admin, I can add food items to the menu, edit and delete them.
* User Story 15 :  As an admin I can go to the admin panel and see order details.

Mockups: [Wireframe (click me)](pizza_house.pdf)

## Features

### Existing Features

* Sign in - When User clicks on the accounts link in the navbar, then clicks on login. That leads him to the sign in page. That is the page where he/she can login by typing in their emailadress/username and password.

* Sign Up - When User clicks on the accounts link in the navbar, then clicks on register. That leds him to the signup page. That is the page where he/she can signup by typing in their emailadress, username and password.

* Add food item - A function only available for loggedin admins to add new food items to the menu. That is a fucntion where the admin can add to the food menu by clicking the accounts button, then menu management. The admin will be led to the add to menu page, where he/she fills up a form. When that is done then he/she will just need to click add to menu button to make a new food item appear in the menu.

* Edit food item -  A function only available for loggedin admins to edit food items in the menu. The admin have to click the menu button then select a food category to find the food items. then he/she can  click blue "edit" link to be led to the edit page. Where he will find a form with the present values that he/she can change and make the change happen by clicking the "Update item" button.

* Delete food item -  A function only available for loggedin admins to delete food items in the menu. The admin have to click the menu button then select a food category to find the food items. then he/she can  click red "delete" link. That redirects them to the same page but with the food item deleted from the database.

* Add to cart - Add to bag is a function that is located in the selected category page of the food menu. You have to first click the menu link in the navbar and then select a food category of your choice to find it. That makes it possible to the user to select quantity then click "ADD TO CART" button to make the food item appear in the cart page.

* Cart - Where user can see the current total price in the right of the top navbar. When User click the cart icon in the right of the top navbar then he/she comes to the cart page. In the Cart page, the user can see food details, delivery price and grand total. In the cart the user can delete food item by clicking the "Remove" button. The user can update the quantity of the chosen food item by selecting a quantity on the right of the food item and then clicking the blue "Update" button. User can choose to keep ordering by clicking blue/white button "Keep Ordering" that then redirects him back to the menu page. User can also go the the checkout by pressing the white/blue button "Secure Checkout"

* Toast - Is an confirmation message that appears in the right topcorner of the website. That shows when for example, an error happens or a successful function.


* Checkout - User can purchase the order by going to the checkout page and filling out the form. User will have to click the cart icon in the top right navbar to go to the cart page first. Then the user have to click the "Secure Checkout" Page to be directed to the checkout page if the user has something in the cart already, Otherwise user have to use the "Add To Cart" feature first. In the checkout page the user can see order details at the bottom. When the user is in the checkout page then he haft to fill out the form (Delivery details) and then card details for the purchase to go through, for that to happen then he haft to press the blue "Complete order" button first. User have the alternative to adjust the cart by clicking the "adjust cart" button. User can also save the delivery details to the profile page.

* Checkout Success - If checkout proccess is successful, then user will come to a checkout successful page. That will show the user a confirmation of the order and the order details under it.

* Stripe - Stripe is a payment processing platform allowing merchants to accept credit card payments on their apps and websites. I have implemented the stripe inside the checkout page of the website.

* My Profile - In the profile page the user can fill out delivery details and see order history. User can go the the profile page by logging in first. Then clicking the accounts page and then after clicking the "My profile" link in the navbar.

* Order History - User can see the Order History at the bottom of the page. User can then click the order number to find the order details that was purchased from before. 


### Features Left to Implement

* Delivery status
* Adding toppings and extra things like Soda&chips.

## Technologies/Databases Used

* Python3 - Backend Logic for the website.
* Stripe - For payments.
* JavaScript/Jquery - For payment aand toast logic.
* SQLite - for storing data in the workspace.
* Postgres - for storing data in Heroku.
* HTML5 - For structure and text.
* Google Fonts To make the website more user friendly.
* Bootstrap4/CSS - For classes of color and responsiveness of the website


## Testing

[TESTME.md (click me)](TESTME.md)


## Deployment

1. First install dj_database_url, psycopg2-binary, gunicorn and whitenoise.
2. Create a requirements.txt file - command in the terminal: pip3 freeze — local > requirements.txt
2. Create a Procfile - web: gunicorn pizza_house.wsgi:application
3. Change debug from True to False.
4. Login to Heroku. Command in the terminal: heroku login
5. Create an new Heroku App
7. Add postgres Database from Heroku.
8. Make pizza_house/settings.py changes with importing dj_database_url and adding the postgres database
9. Migrate the changes.
10. Connect Heroku to repository - ex. command: heroku git:remote -a  pizza_house
11. Create any config variables.
12. Push the core to Heroku - command in the terminal: echo web: git push -u heroku master
13. Run the App - command : heroku ps:scale web=1


## Credit 

* Mentor & Code expert: Rohit Sharma
* [Django 3 By Example](https://books.google.se/books?id=y83aDwAAQBAJ&pg=PA246&lpg=PA246&dq=how+to+fetch+id+from+a+form+django+views&source=bl&ots=j4BNzbest4&sig=ACfU3U2LhNPP3Do6XlMRR9DRXrYXoaFi7Q&hl=sv&sa=X&ved=2ahUKEwit9u-V66fqAhW6AxAIHfHMCscQ6AEwA3oECAcQAQ#v=onepage&q&f=false)
* [Code Institute Tutorials & Support Team](https://codeinstitute.net/)
* [Harvard CS50 Tutorial - Django](https://www.youtube.com/watch?v=ZjAMRnCu-84)
