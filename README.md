<h1 align="center">PROTEIN SHAKES N SNACKS<h1>

<p align="center">
    <a href="https://food-bank-manager.herokuapp.com/">View the live project here.</a>
</p>

## This is a web based application designed for the sale of takaway shakes and protein snacks.

<h2 align="center"><img src="https://i.ibb.co/0tRh3g5/responsive-design.png"></h2>

-   ## User Experience (UX)

-   ### User stories

    -   #### First Time User Goals

        1. As a First Time User, I want to easily understand the main purpose of the web app.
        2. As a First Time User, I want to be able to browse the menu.
        3. As a First Time User, I want to be able to register to be able to make orders.
    
    -   #### Returning Visitor Goals

        1. As a Returning User, I want to be able to log into my profile.
        2. As a Returning User, I want to be able modify data and edit the app content.
    
    -   #### Frequent User Goals

        1. As a Frequent User, I want to the app to safely store and retrieve data.        
        2. As a Frequent User, I want to the app to be fast and efficient.

-   ### Design

    -   #### Color Scheme
        -   The application's two main colours are teal and white. The buttons have their distinctive and contrasting colours to visually hint at their function.

    -   #### Typography
        -   The font of choice for the application is Roboto Google font with Sans-Serif as backup.

    -   #### Imagery
        -   The Background image is referring to the purpose of the application. Icons hint at various features and CRUD functionalities.

*   ### Wireframes
    -   Atribute schema [View](/static/img/Database_schema.PNG)

    -   Relationship diagram (ERD) [View](/static/img/Relationship_diagram_(ERD).PNG)

    -   Homepage (Visitor's view) [View](/static/img/Homepage.png)

    -   Homepage (Logged in User's view) [View](/static/img/user_loggedin_view.png)

    -   Add New Food Item Page (Logged in User's view) [View](/static/img/add_new_item_view.png)

    -   Manage Food Categories Page (Admin's view) [View](/static/img/manage_food_categories_view.png)
    
## Features

- Responsive on all device screen sizes

- Interactive elements 
    -   Actions involving login, using CRUD functionalities and editing food items are confirmed Swith feedback messages [View](/static/img/feedback_message.png) 
    - Low stock warning is triggered if item's inventory value is 10 or less [View](/static/img/low_stock_warning.png)

- CRUD functionalities

## Technologies

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Font Awesome:](http://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Materialize:](https://materializecss.com/)
    - Materialize is used to provide the main Nav Bar, the side Nav Bar, the Hompage collapsible and food categories cards.
1. [jQuery:](http://jquery.com/)
    - jQuery is used to implement Materialize elements and form validation.
1. [Flask:](https://palletsprojects.com/p/flask/)
    - Flask is used to render html templates, enable user login password generation and flashing feedback messages.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB is used to provide the application with a database where the data saved by the users can be stored and edited.
1. [diagrams.net:](https://app.diagrams.net/)
    - Web based application diagrams.net is used to create wireframes during the design stage of the project.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/static/img/W3C_markup_validator.PNG) <br>
    Please note that even though the html validatation shows errors, these are all related to the use of Flask values in curly brackets and Jinga templating language expressions which are essential for the app's functioning.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](/static/img/W3C_CSS_validator.PNG)
-   I have used [PEP8 online check](http://pep8online.com/) to esure the Python code complies to [PEP8 Style Guide](https://peps.python.org/pep-0008/) in terms of layout, line length, indentation, blank lines, etc. - [Results](/static/img/PEP8%20checker%20result.PNG)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time User I can clearly distinugish the main sections of the web app's home page, the header with the app's name as well as buttons for registration and login. Below there is a search section and furter down a simple food item list.
    2. As a First Time User, I can perform searches and have access to such data as available stock size.
    3. As a First Time User, I've been able to register and create my profile giving me access to more advanced functionalities.

-   #### Returning Visitor Goals

    1. As a Returning User, I've been able to log into the app.
    2. As a Returning User, while being logged in I've been able to add, delete and edit particular food items as needed.

-   #### Frequent User Goals

    1. As a Frequent User, I'm aware that all the data in the app is stored in a cloud storage service and can be accessed only by authorized staff.
    2. As a Frequent User, I've been able to quickly update the just by clicking an item in the list and inputing figures in appropriate field.

### Further Testing
-   Black box testing schedule. [View](https://docs.google.com/document/d/1Xp4ro9cAy7-rdSsMTUlwHNvY8mwdun3R/edit?usp=sharing&ouid=113273292568686929472&rtpof=true&sd=true)
-   The website was tested on Google Chrome, Internet Explorer and Microsoft Edge.
-   The website was viewed on a variety of devices such as Desktop, Laptop and Android phone.
-   A large amount of testing was done to ensure that all pages were linking correctly.

### Known Bugs

-   Decrease and increase stock items fields need to be clicked near the bottom edge otherwise they can't be accessed. 

## Deployment

-   The app files have been manually deployed from a GitHub repository to a newly created Heroku app. The following commands have been executed in a Gitpod bash terminal:<br>
    1.  heroku login -i
    2.  heroku create app_name_here
    3.  git push heroku main

## Credits

### Code
-   The code has been largely adapted form [Code Institute's](https://codeinstitute.net/) 'Mini Project' tutorial in 'Backend Development' section by [Tim Nelson](https://github.com/TravelTimN).

### Content
-   Chocolate Protein Shake description and nutritional values [Chelsea's Messy Arpron](https://www.chelseasmessyapron.com/triple-chocolate-chunk-brownie-protein-shake/)
-   Coffee Protein Shake description and nutritional values [Love & Zest](https://www.loveandzest.com/coffee-lovers-protein-shake/)
-   Cookies and Cream Protein Shake descritption and nutritional values [The Seasoned Mom](https://www.theseasonedmom.com/cookies-and-cream-protein-shake/)
-   Strawberry and Banana Protein Shake descritption and nutritional values [The Protein Chef](https://theproteinchef.co/strawberry-banana-protein-shake-recipe/)
-   Peanut Butter Protein Shake descritption and nutritional values [eating bird food](https://www.eatingbirdfood.com/peanut-butter-protein-shake/)
-   Protein Packed Skinny Frozen Mocha description and nutritional values [Nutrition Starring YOU](https://nutritionstarringyou.com/protein-packed-skinny-frozen-mocha/)
-   Salted Caramel Mocha Protein Frapé descripion and nuritional values [The Seasoned Mom](https://www.theseasonedmom.com/salted-caramel-mocha-protein-shake/)
-   Vanilla Frapé descripion and nuritional values [foodfanatic](https://www.foodfanatic.com/recipes/healthy-homemade-vanilla-frappuccino-recipe/)
-   Reign Peach Fizz descripion and nuritional values [musclefood](https://www.musclefood.com/reign-peach-fizz.html)
-   Moose Juice Berry description and nutritional values [musclemoose](https://musclemoose.co.uk/product/berry/)
-   Protein Dynamix BCAA Amino Energy descripion and nuritional values [musclefinessewholesale](https://musclefinessewholesale.com/protein-dynamix-bcaa-amino-energy-12-x-500ml.html)
-   All remaining content was written by the developer.

### Media
-   Background image for the app is a free stock photo by Kindel Media at [Pexel] https://www.pexels.com/pl-pl/zdjecie/koktajl-sloj-odswiezenie-zimne-napoje-8181548/
-   Chocolate Protein Shake photo [Chelsea's Messy Arpron](https://www.chelseasmessyapron.com/wp-content/uploads/2013/10/Chocolate-Protein-Shake-1.jpg)
-   Coffee Protein Shake photo [Love & Zest](https://www.loveandzest.com/wp-content/uploads/2019/02/Coffee-Protein-Shake-Web-Ready-8-640x960.jpg)
-   Cookies and Cream Protein Shake [The Seasoned Mom](https://www.theseasonedmom.com/wp-content/uploads/2018/12/Cookies-and-Cream-Protein-Shake-8a.jpg)
-   Strawberry Banana Protein Shake [The Protein Chef](https://media.theproteinchef.co/wp-content/uploads/2021/08/Strawberry-Banana-Protein-Shake-Recipe-683x1024.jpg)
-   Peanut Butter Protein Shake [eating bird food](https://www.eatingbirdfood.com/wp-content/uploads/2021/07/peanut-butter-protein-shake-in-cup-633x950.jpg)
-   Protein Packed Skinny Frozen Mocha [Nutrition Starring YOU](https://www.simplyhappyfoodie.com/wp-content/uploads/2019/07/iced-coffee-protein-shake-1b.jpg)
-   Salted Caramel Mocha Protein Frapé [The Seasoned Mom](https://www.theseasonedmom.com/wp-content/uploads/2015/03/Salted-Caramel-Mocha-Protein-Shake-17.jpg)
-   Vanila Frapé [foodfanatic](https://food-fanatic-res.cloudinary.com/iu/s--Qr4q1aJB--/t_xlarge_p/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1502748400/healthy-homemade-vanilla-frappuccino-pic.jpg)
-   Reign Peach Fizz [musclefood](https://d3rxe6nylop6k3.cloudfront.net/catalog/product/cache/1/image/530x/9df78eab33525d08d6e5fb8d27136e95/m/o/monster-reign-peach-fizz-500ml-mf_dr391_sample_1.jpg)
-   Moose Juice Berry [musclemoose](https://musclemoose.co.uk/wp-content/uploads/2021/04/MooseJuice_Berry-Flavour-Can_Single-600x849.png)
-   Protein Dynamix BCAA Amino Energy [musclefinessewholesale](https://musclefinessewholesale.com/media/catalog/product/cache/21d694c873907d78b2b1c9b0cbd4c5fc/t/r/tropical_energy_drink.jpg)
### Acknowledgements
-   Also many thanks to my Harlow College tutor Patrick Justus Phd who provided me with input on black box testing, database schema and ERD.
