# Testing Document

## Navbar - test has been done on all type of screen sizes

1. Clicking the logo turns user back to homepage. Test=Successful.
2. Clcking the account link in the menu doesn't take user to another page and the options after clicking comes up. All links under account works. Test=Successful.
3. Clicking the menu link works and leds the user to the menu page. Test=Successful.
4. The Cart Icon in the navbar is working. If I add something from the menu I can see that the price changes according to whats in the Cart. If I click on it then it will led the user to the cart page. Test=Successful.
5. Responsiveness of the Navbar is working and adjusting according to what screen the user has. Test=Successful.

## Home page - test has been done on all type of screen sizes

1. Homepage has been tested in responsiveness. The homepage is working on all advices and the design doesn't brake and the responsiveness is according to what screen the user has.Test=Successful.
2. Link "Check it out" is working. When user click on it the current page doesn't change but another tab opens and the user can see the link url from there. Test=Successful.

## Menu page - test has been done on all type of screen sizes

1. Menu Page is responsive and is changing according to the screen of the user. Test=Successful.
2. The food category links are all working and is taking the user to the page expected, without any error. Test=Successful.
3. If User reverse back to the menu page after clicking a link then it works, without an error. Test=Successful.

## Food pages  - test has been done on all type of screen sizes

1. If User click on add to cart then it works without any error. Test=Successful.
2. User can change quantity if he/she wants, without any problem. Test=Successful.
3. User can change quantity by clicking the quantity amount and typing in the quantity needed. Test=Successful.
4. If user add something in the cart and reverses. The order will be unchanged and stil there in the cart.Test=Successful.
5. Only Admins can see the Edit | Delete links. Test=Successful.
6. All links of the food pages are working without any error and takes user to expected page. Test=Successful.

## Food Management - test has been done on all type of screen sizes

1. If Admin clicks the Menu Management link under the account link the it works. Test=Successful.
2. In menu management page, if admin fills out the form then it works successful without any error and the new food appears on the chosen category. Test=Successful.
3. If admin clicks on "Cancel" button on the menu management page then it turns admin back to menu page. Test=Successful.
4. If admin click the 'Add Item' then it submits the form. Test=Successful.
5. If admin reverse after submitting the form and then again forwards the page, then the food will not be double submitted. Test=Successful.
6. Admin cannot submit form with filling out details of the food item. Test=Successful.
7. If admin goes to food pages then clicks the "Edit" link will make the admin able to make changes to the chosen food item.
8. If admin goes to food pages then clicks the "Delete" link will make the admin able to remove food item from the database.

## Register User - test has been done on all type of screen sizes

1. If user clicks on register link under the account link then it leds the user to the Signup page. Test=Successful.
2. If user clicks on "Back to login" link then user will be led to Signin page without any error. Test=Successful.
3. User cannot signup without filling out the user details first. Test=Successful.
4. If user clicks on "Sign up" button after filling out details, then the form will be submitted. Test=Successful.
5. User will get an confirmation email after signing up. Test=Successful.
6. If user clicks on "Signin" link then user will be led to Signin page without any error. Test=Successful.
7. If user reverses after signing up and the forwards again without changing anything, then the user will not get double email confirmations. Test=Successful.

## Sign In - test has been done on all type of screen sizes

1. User cannot sign in without filling out user details that is correct. Test=Successful.
2. User cannot reverse back after logging in. Test=Successful.
3. If user clicks on "Signup" link, then user will be led to Sign up Page. Test=Successful.
4. If user clicks on "home" link, then user will be led to home page. Test=Successful.
5. User cannot login without confirming email first. Test=Successful.
6. if user clicks on "Forgot Password?" link , then user will be led to Password reset page. Test=Successful.
7. If user checks "Remember Me" then user will get an alternative after logging in to save password and username. tested on Safari and Google Chrome. Test=Successful.
8. If user clicks on "Sign in" button after filling out the details then the form will be submitted. Test=Successful.

## Password reset - test has been done on all type of screen sizes

1. If user clicks on "Back to login" then user will be led to signin page. Test=Successful.
2. User cannot fill out any type of email that doens't exist in the databe or this error message "The e-mail address is not assigned to any user account", and the form will not be submitted. Test=Successful.
3. If user types in the correct email then user will get an email with a link where user can reset Password. Test=Successful.
4. Reset password link from emails works succesfully and changes the old password. Test=Successful.

## Cart - test has been done on all type of screen sizes

1. If cart is empty the user will se a message of "The cart is empty". Test=Successful.
2. If the cart is empty the user will only see "Keep ordering" button and not also "Secure Checkout" button. Test=Successful.
3. If user clicks on the "Keep ordering" button then the user will be led to the Menu page. Test=Successful.
4. If user has food items on the cart page then user can succesfully see the food item details. Test=Successful.
5. If user has food items on the cart page then user can succesfully update the quantity by changing the quanity and clicking the "Update" button. Test=Successful.
6. If user has food items on the cart page the user can succesfully remove it from the cart without removing it from the database. Test=Successful.
7. If user has food items in the cart then user can see the delivery, total and grand total of the delivery. Test=Successful.
8. If user clicks on the "Secure checkout" button the user will be led to the checkout page. Test=Successful.

## Checkout page - test has been done on all type of screen sizes

1. User cannot submit order without filling out the required order details.
2. User cannnot submit order without filling out the correct card details.
3. if user clicks on "Adjust cart" User will be led back to the cart page.
4. If user is logged in then user can save the information to the profile page.
5. If user is not logged in the user can click on "Create an account" or "Sign in" to save the information to the account.
6. If user has typed in the correct detail then the user can submit the form by clicking on the "Complete Order" Button, then the user will be led to the checkout success page.

## Checkout Successful - test has been done on all type of screen sizes

1. Order details on the checkout success page.
2. User will get a confirmation sent to the email address about the order.
3. if user clicks on "Do you wanna order more?" button then user will be led back to the menu page.
4. If user tries to reverse after submitting order, then user will be led back to the menu page.

## Stripe - test has been done on all type of screen sizes

1. If user has entered the wrong card details then the user will se an error message under. 
2. If user has enetered the right card details then the user can see what type of card the user has.
3. if User has to futher authenticate the card details the user will be led back to their bank.

## My profile - test has been done on all type of screen sizes

1. User can see user details in the my profile page. 
2. User can update the details by changing the value and clicking on the "UPDATE INFORMATION" button.
3. User can see order history in the my profile page. 
4. If user clicks on the order number then user will be led to Order details page"
5. In order details page if user clicks on "Back to profile" then that will led the user to the my profile page.


## Toast - test has been done on all type of screen sizes

1. Message works and it is shown in the top right corner of the page.
2. If sometihng added to cart then User can click on "Go to secure checkout" That will led the user to the cart page. 
3. Error messages works and is shown with the toast notification.

## Bugs found

1. Order confirmation webhook - Left because, the error was tried to get fixed by me and the excellent support team but somehow didn't still work after many different ways of trying to find solutions. A bug that is left to fix in the future.
