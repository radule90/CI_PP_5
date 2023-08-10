![Responsive image](static/images/readme/respo.jpg)  

[Sun&Peaches Ecommerce](https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/) represents a unique fashion jewelry brand characterized by its distinctive design and timeless essence. Enriched with an array of colors, mermaids, and stars, it offers a canvas for creative combinations, appealing to individuals who cherish personal expression and freedom.  

The inspiration for this project came from my sister's desire to have a platform like this. She wanted a place where people could explore and purchase unique and stylish jewelry items, leading me to create the Sun&Peaches ecommerce website.  

I built this ecommerce project for Sun&Peaches using the knowledge I gained from the course "[Python Django Ecommerce | Advanced Django Web App From Basic](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/)" I used technologies like HTML, CSS, Django, Python, and JavaScript to create a user-friendly website where you can explore and purchase their fashionable jewelry items.   

Technologies Used:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" align="left" width="30px" style="padding-right: 10px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" align="left" width="30px" style="padding-right: 10px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" align="left" width="30px" style="padding-right: 10px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" align="left" width="30px" style="padding-right: 10px;" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" align="left" width="30px" style="padding-right: 10px;" />    
<br>
[Here you have a live version of the project.](https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/)  

When testing interactively, use a card number, such as [4242 4242 4242 4242](https://stripe.com/docs/testing?testing-method=card-numbers#visa). Enter the card number in the Dashboard or in any payment form.
- Use a valid future date, such as **12/34**.
- Use any three-digit CVC (four digits for American Express cards).
- Use any value you like for other form fields.   

---  

## Table of Contents

1. <details>
   <summary><a href="#ux">UX</a></summary>

   - [Visitor Goals](#visitor-goals)
   - [Business Goals](#business-goals)
   - [User Stories](#user-stories)
   - [Agile Development](#agile-development)
   - [Marketing](#marketing)

   </details>
   
2. <details>
    <summary><a href="#visual-design">Design</a></summary>

      - [Wireframes](#wireframes)
      - [Database Schema](#database-schema)
      - [Colors](#colors)
      - [Fonts](#fonts)
      - [Icons](#icons)

</details>

1. <details>
   <summary><a href="#styling-formatting-and-features">Styling, Formating and Features</a></summary> 
    
    - [Future Features](#future-features)

</details>

4.  <details>
    <summary><a href="#validation-and-testing">Validation and Testing</a></summary>
    <ul>
    <li><a href="#validation">Validation</a></li>
    <li><a href="#testing">Testing</a></li>

    <li>
    <details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Fixed Bugs](#fixed-bugs)
    </details>
    </li>
    </ul>

</details>
  
5. <details>
    <summary> <a href="#deployment">Deployment</a></summary>

      - [Local Deployment](#local-deployment)
      - [Heroku Deployment](#heroku-deployment)

</details>

6. <a href="#tools-and-platforms">Tools and Platforms</a>

7. <a href="#content-and-credits">Content and Credits</a>

8. <a href="#media">Media</a>
  
---  
  
## UX  

### Visitor Goals  
- Visitors of all ages interested in modern but dreamy jewelry - that is affordable
- Visitors who support slow fashion and sustainability
- Visitors who exclusively buy brands that harm none during the production process
- Visitors who support novelty, creativity and stepping out of a cliché
- Visitors who are seeking freedom and inspiration all the time in various colours and shapes in handmade products

### Business Goals  
- To introduce itself as a sustainable brand on the market 
- To make sure that its products are available in online purchase in every country 
- To always promote its philosophy of handcrafted goods 
- To promote its creativity, uniquness and simplicity at the same time 
- To attract visitors' attention with calm and warm atmosphere of its website
- To make the online shopping as simplest as possible
- To provide regular sales
- To position itself  as a trendsetter in slow fashion  domain  only  with intention of attracting new visitors  too  

### User Stories  
- As a **Site User** I can **view the homepage** so that **I can see the newest items in shop**  
- As a **Site Administrator** I can **manage user accounts** so that **I can maintain the integrity and security of the website and ensure a smooth user experience.**
- As a **Site User** I can **use search functionality** so that **I can find specific items in the shop**
- As a **Site User** I can **view a list of products** so that **I can browse and explore the list of products and find those that suit me**
- As a **Site User** I can **view detailed information about the product** so that **I can confirm that the product is suitable for me**
- As a **Site User** I can **view multiple images of product** so that **I can have better sense of product appearance**
- As a **Site User** I can **sign up for an account** so that **I can view my profile page**
- As a **Registered User,** I can **easily login and logout** so that **I can access my account information**
- As a **Registered User** I can **recover my password** so that **I can regain access to the account**
- As a **Site User** I can **receive a register confirmation email** so that **I am sure that registration went well**
- As a **Registered User** I can **view and update my account details** so that **I can keep information up to date**
- As a **Registered User** I can **leave reviews and ratings for products that I have bought** so that **I can share feedback with other customers**
- As a **Site User** I can **contact the owner through the contact form** so that **I can get more information, assistance or send complaints**
- As a **Site User** I can **filter products based on parameters(e.g. Brand)** so that **I can find specific items**
- As a **Site User** I can **easily sign up for a newsletter subscription** so that **I can receive updates on new products, promotions, sales**
- As a **Site User** I can **view a size guide for products** so that **I can choose right product size**
- As a **Site User** I can **view customer reviews of products** so that **I find out more about the quality of the product**
- As a **Registered User** I can **easily add product to the cart** so that **purchase is fast and simple as possible**
- As a **Registered User** I can **track my order history** so that **I have an overview of my previous purchases**
- As a **Registered User** I can **add products to my wishlist** so that **I can save them for future purchase**
- As a **Site Administrator** I can **access and manage all important options on the admin panel** so that **I can easily manage products, users, orders content**
- As a **Site Administrator** I can **add, delete, and update products on the front-end** so that **I should be able to access a user-friendly interface that allows me to do CRUD functionalities for products**
- As a **Registered User** I can **make secure payments using Stripe** so that **I can have confidence that my payment information is handled securely and my purchase is protected**
- As a **Site User** I can **seamlessly navigate the website with a clear header, navbar, and footer** so that **I can quickly navigate to what interests me and visit social networks**
- As a **Site Owner** I **need to have ReadMe document** so that **I have thorough and well-organized documentation for efficient website management**
- As a **Site Administrator** I can **create and manage product categories** so that **products are well organized and can be easily navigated**
- As a **Site Visitor** I can **easily navigate through product list** so that **I can browse through the entire product list fast**
- As a **Site Owner** I want **to have custom 403, 403_CSRF and 404 error pages** so that **visitors encountering these issues will have a better understanding of the problem.**
- As a **Site Owner** I want **to ensure that the codebase is well-organized, neatly formatted, and extensively commented** so that **it can be easily understood and maintained by other developers**
- As a **Registered User,** I can **change my password** so that **I can maintain the security of my account**
- As a **Site Administrator** I want **to have rich text editor** so that **I can send styled newsletter**
- As a **Registered User** I can **delete my own product review** so that **I can manage the content associated with my account**
- As a **Site Visitor** I want **the registration process to enforce strong password requirements** so that **ensure the security of my account**
- As a **Site User** I want **to see the total count of items in my shopping cart** so that **I can keep track of the quantity of products**.  

### Agile Development  
- During the development of the Sun&Peaches fashion jewelry e-commerce project, I followed an Agile approach to manage the project effectively.
- The project's development workflow was organised through GitHub Projects and Issues.
- Most of the time I focused on user stories to quickly plan the project due to time constraints
- Later in the development, I switched to the MOSCOW system to prioritize tasks better. This categorization method helped me decide what aspects were crucial (Must-Have), important (Should-Have), optional (Could-Have), or not needed (Won't-Have).
- I also started using GitHub Issues labels to organize tasks effectively, making it easier to see importance and type.
- I continuously assessed and adjusted the project. This allowed me to make real time changes based on feedback and insights.
- By applying Agile methodologies, I managed to create a functional e-commerce platform for Sun&Peaches. But, there is room for improvement to fully aligns with the brand's identity and meets all user requirements.

### Marketing  
- Marketing in slow fashion is also "slow" , soft and definitely not for the masses.
- The photos chosen here are supposed to attract free spirit visitors that are looking for inspiration in authenticity and creativity.
- All these in a subtle way, that doesn't require demands and doesn't set the patterns followed by crowds 
- Free shipping, in this case, would be the only option. Otherwise, I wouldn't represent anymore what I stand for.  

- I've created custom subscription app that efficiently delivers newsletters to our audience, enhancing our communication and engagement.
  ![Newsletter](static/images/readme/newsletter.jpg)
- I've created a Facebook mockup page for our Sun&Peaches jewelry store, encapsulating our brand's authentic charm and creative inspiration to resonate with our target audience
  ![Facebook Mockup](static/images/readme/facebook.png)

- I've strategically incorporated SEO-friendly keywords and crafted a captivating description that embodies Sun&Peaches' unique handcrafted jewelry inspired by nature, targeting free-spirited individuals seeking authenticity and creativity in their fashion choices
- Additionally, I've included a robots.txt and a sitemap.xml to optimize visibility on Google search engines.  

---  

## Design  

### Wireframes  
- The initial project wireframes. As they are created in the early planning stages, they will differ from the final project.  

  #### Desktop Wireframes   
  ![Desktop Home](static/images/wireframes/pc-Home.png)   
  ![Desktop Shop](static/images/wireframes/pc-Shop.png)   
  ![Desktop Product Details](static/images/wireframes/pc-Product.png)   
  ![Desktop Contact Page](static/images/wireframes/pc-Contact.png)   
  ![Desktop Profile Page](static/images/wireframes/pc-Profile.png)    
  
  #### Mobile Wireframes   
  ![Mobile Home](static/images/wireframes/Mobile-Home.png)   
  ![Mobile Shop](static/images/wireframes/Mobile-Shop.png)   
  ![Mobile Product Details](static/images/wireframes/Mobile-Product.png)   
  ![Mobile Contact Page](static/images/wireframes/Mobile-Contact.png)   
  ![Mobile Profile Page](static/images/wireframes/Mobile-Profile.png)    

### Database Schema  
- I've created an Entity-Relationship Diagram (ERD) as part of planning process to map out the relationships between different data entities in the system. This ERD serves as a blueprint that guides the development of the project. As I continue to refine and enhance the platform, any potential modifications or updates to the ERD will help ensure that the deployed site remains aligned with evolving goals and requirements.   
  ![ERD](static/images/readme/erd.png)   

### Colors  
- I selected these pastel colors that contribute to the overall visual appeal of the Sun&Peaches.
- I chose peach like color (#ff9c7f) because it looked playful and energetic and making it ideal for main heading.
- Light green (#8cada4) was chosen because it brings harmonious nature feel.
- Light brown (#bea494) allows the content and visuals to stand out while maintaining a calm ambience.
- Dark brown (#4c413b), while this pastel color is legable and readable.
- They might initially appear distinct, but when combined, they create a harmonious appearance.   
  ![Color Pallete](static/images/readme/colors.png)

### Fonts  
- I chose [Quicksand Google Font](https://fonts.google.com/specimen/Quicksand?query=quick) for its modern and clean appearance. This font's readability and simplicity enhance the user experience, making content easy to read and comprehend.    

  ![Quicksand Font](static/images/readme/quicksand.png)   
  
- For headings and important elements I chose [Laila Google Font](https://fonts.google.com/specimen/Laila?query=laila), as its elegant and distinctive style emphasizes key sections of the Sun&Peaches e-commerce.   

  ![Laila Font](static/images/readme/laila.png)   

### Icons  
- Icons used on this website are from [SVG Repo](www.svgrepo.com)
- As Favicon and cursor I chose to use peach to create playful visual experience that aligns with the brand's identity.
- Peach cursor adds a touch of uniqueness to user interaction, enhancing the overall user experience.  
  ![Peach](static/images/readme/peach.png)

- For pointer cursor I opted for a sun to provide clear feedback to users when they hover over elements like buttons and links.  
  ![Sun](static/images/readme/sun.png)  

- In the future, I plan to introduce a feature that allows users to choose between custom cursors and the standard cursors used on websites.
- This customization option will provide users with the flexibility to select their preferred cursor style.  

---  


## Styling, Formatting and Features   

### Styling, Formatting, Features

#### Design of Sun&Peaches:
- I decided to infuse lively colors into the design mix, creating a captivating blend.
- I went for gentle pastel shades to make everything look even better.
- The main title got a playful and energetic peachy hue (#ff9c7f) for a lively touch.
- To keep things in tune with nature, I picked a soothing light green shade (#8cada4).
- I added light brown (#bea494) to make important stuff stand out while keeping things calm.
- For easy reading, I added a dark brown shade (#4c413b).
- All these colors, though different, come together nicely for a balanced look.

#### Technologies Used:
- I skipped using Bootstrap to challenge myself with pure CSS.
- I ditched jQuery in favor of JavaScript to keep things simple and interactive.
- For Django views, I opted for function-based views instead of class-based that I've used in last project.
- To make sure everything's secure, I used the @login_required decorator and user_passes_test tests in Django's authentication system. This way, only the right users can access the right things.  

#### Home Page     
![Home Respo](static/images/readme/respo2.jpg)  

- In the header section, I've added essential links such as Home, Shop, and Contact as text links. With pure CSS and JS I made these links collapsing within a hamburger menu on smaller screens.   
  ![Navbar](static/images/readme/nav.jpg)    
  ![Navbar-Mobile](static/images/readme/nav-mob.jpg)   
- For user profile dashboard, search, and cart functionalities, I've utilized commonly recognized [FontAwesome](https://fontawesome.com/) icons.    
  ![Navbar-Menu-Open](static/images/readme/hamburger-open.jpg)
- For the search function, I opted to create an overlay with a centered search input that is prominently visible. To enhance the visibility of the search input, I applied a transparent brown overlay that complements the overall design of the site.   
  ![Search](static/images/readme/search.jpg)  
- On the homepage, my aim was to greet users with a warm welcome message and provide a brief introduction to the Sun&Peaches ecommerce platform.     
  ![Intro Message](static/images/readme/intro-msg.jpg)  
- Right after that, I included a captivating product carousel. Each image in the carousel is a link to the corresponding product, ensuring easy exploration     
  ![Swiper](static/images/readme/swiper.jpg)   
- I've used for that purpose [Swiper JS](https://swiperjs.com/), which was easy to implement thanks to its excellent documentation.

- For  strategic touch, I added a subscription section that allows users to join and receive newsletters.     
  ![Newsletter](static/images/readme/newsletter.jpg)

- I created a custom functionality that lets me send newsletters directly from the dashboard to all subscribed users, enhancing our marketing efforts.    
  ![Newsletter Send](static/images/readme/newsletter-send.jpg)
- And improved it with [TinyMCE](https://www.tiny.cloud/) Rich Text Editor, so that sent emails have really styling.
- For the footer, I opted to provide additional details about Sun&Peaches, including information about the store, address, social media links, as well as quick links to product categories.     
  ![Footer](static/images/readme/footer.jpg)
- I utilized a CSS Grid to ensure that the design remains responsive across different devices and screen sizes.

#### Shop     

  ![Shop Responsive](static/images/readme/shop-respo.jpg)   
  
- The shop page was structured with a side panel featuring category filters, allowing users to easily navigate through different product types.     
  ![Categories](static/images/readme/categories.jpg)
- I've used context processors to ensure that category links are accessible throughout the entire website, enabling display of categories across different pages.
- On smaller screens, I chose to collapes filter section to optimize space, and I used Font Awesome icons with animation to make it more intersting.      
  ![Categories-Mobile](static/images/readme/categories-mob.jpg)
  
- The main product list displays links to individual products.
- I added conditional rendering, if there are no products message will be displayed.     
  ![Shop](static/images/readme/shop.jpg)
- I deliberately omitted the "Add to Cart" option on this page.   
- Instead, users are encouraged to click on products to access their detailed descriptions, especially for items with variations.      

![Product Details](static/images/readme/product-details-respo.jpg)
- For the product detail page, I prioritized showcasing the product itself     
  ![Product Details](static/images/readme/product-detail.jpg)
- For most of the part I've used CSS Flexbox, as my favourite, for responsive design.    
   ![Product Details](static/images/readme/product-detail-respo.jpg)

- Variations for products have been implemented; however, I realized that I overlooked the implementation of stock tracking for each variation. This will be addressed in the next update by adding a "stock" field to the Variation models and defining a method in the product model to calculate the total stock of all variations for that specific product.
- I implemented a review star system inspired by [Python Django Ecommerce | Advanced Django Web App From Basic](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/), ensuring that only users who have purchased the product can leave reviews.    
  ![Review](static/images/readme/review.jpg)
- All product reviews are stored in the database using a model specifically designed to handle reviews.     
  ![Review Respo](static/images/readme/review-respo.jpg)
- I have implemented messages to be displayed to users who are not signed in or haven't purchased the product, ensuring that only signed-in users who have made a purchase are allowed to leave a review.
- For cases where a review has already been submitted, I've enabled the functionality to update the existing review. I accomplished this by creating a function based view called 'create_review' and securing it with the login decorator for more security.
- Additionally, users who have posted reviews are granted the ability to delete their reviews, with this functionality also protected by a login decorator.
   
- While initially planning to include an image gallery, it's currently scheduled for implementation in the future due to time constraints.
  
#### Contact Page     
![Contact Page Respo](static/images/readme/contact-respo.jpg)
- I have incorporated a contact page as an essential component of the website.
- I opted for a separate app to ensure easy scalability and potential future enhancements such as an AI chatbot
- This contact page allows users to send messages, and all the messages are stored in the database for record-keeping.     
  ![Contact Page](static/images/readme/contact.jpg)
- I have included placeholder contact information and a map of Antarctica for now, with the intention of integrating Google Maps for actual projects to display accurate location information.
- I've implemented conditional rendering for the full name field and email, ensuring they are prefilled if the user is signed in.

#### Dashboard / Account / Orders List      
- I decided to only let registered users shop for now, I think it is a good security measure. I might allow non-registered users to shop in the future.   
  ![Sign In](static/images/readme/signin.jpg)   
  ![Sign Out](static/images/readme/signout.jpg)
- I created a custom way for users to sign up using a [Python Django Ecommerce | Advanced Django Web App From Basic](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/).     
- I also added requirements for stronger passwords (I've used [stackoverflow](https://stackoverflow.com/questions/26823766/re-search-password-checking-error)):
  - It needs to have at least one number.
  - It needs to have at least one capital letter.
  - It needs to have at least one special symbol.
  - It needs to be at least 6 characters long.     
 
  ![Sign Up](static/images/readme/signup.jpg)
- After submitting the completed form, I wanted to provide new users with clear instructions on the next steps to take.    
  ![SignUp Confirm](static/images/readme/signup-confirm.jpg)    
  ![SignUp Confirm mail](static/images/readme/signup-confirm-mail.jpg)   
- I also added a feature for users who forget their password. 
- They can request a reset link, which they get through email.     
  ![Pass-reset](static/images/readme/passreset.jpg)
  ![Pass-reset-mail](static/images/readme/passreset-mail.jpg)
  ![Set New Pass](static/images/readme/setnew.jpg)
- I thought that is also nice feature to add to allow users can change their password if they want to.
- In a future update, I'll also give users the option to delete their account. Which I didn't get to implement due to time constraints.   
  ![Password Change](static/images/readme/change-pass.jpg)
- When a user signs up, a profile is created for them. They can save their shipping information to make shopping easier.
  ![Profile](static/images/readme/update-profile.jpg)
- Initially, in the user dashboard, I wanted users to see their order history and shipping details. As probably the most important user data. I thought it made sense to have all the options in one menu so users can easily change or view their information. That's why decided to make dashboard.   
  ![Dashboard](static/images/readme/dashboard.jpg)
- I primarily achieved responsiveness using CSS Flexbox, which I find to be my preferred method for positioning and layout due to its flexibility and adaptability. In addition I also used absolute and relative positioning where apropriate (e.g. collapsable menu icon).   
- Although it would have been easier if I had done the site with the help of Bootstrap, I did the whole site with custom CSS, in order to challenge myself and thus renew and learn new things.  
- Same reason for using function based views in Django instead of class based, as I feel more comfortable doing class based views so I wanted to challenge myself
  ![Dashboard](static/images/readme/dash-mob.jpg)
- I've secured the dashboard and the majority of its associated links by applying the login_required decorator, ensuring that only authenticated users can access these protected areas and functionalities.   
  ![Orders List](static/images/readme/orders.jpg)    
- I thought it was important for the user to have an overview of his previous purchases, so I decided and created a list of orders where the user can click on the order number to see all the important details. 
  ![Order Details](static/images/readme/order-details.jpg)   

#### Cart / Payments    
- The functionality for "Add to Cart" and "Place Orders" has been developed based on a [Python Django Ecommerce | Advanced Django Web App From Basic](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/).
![Cart Empty](static/images/readme/cart-empty.jpeg)   
- To indicate that a product has been added, I chose to subtly update the item count in the header of the cart icon.   
![Cart Count](static/images/readme/cart-count.jpg)
- Shipping costs are not included in this project due to the ecommerce's business policy.
  ![Cart](static/images/readme/cart.jpg)
- The integration of Stripe for payment processing was adapted from the Boutique Ado project, although without incorporating webhooks at this stage, which are intended for implementation in the future.   
![Checkout](static/images/readme/checkout.jpg)
- I utilized the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) element to present Stripe error messages. While I considered using it previously, it appeared suitable for this particular scenario.  
![Payment](static/images/readme/payment.jpg)
![Payment Success](static/images/readme/payment-success.jpg)
![Order Confirm](static/images/readme/order-confirm-mail.jpg)
- I've utilized Django messages to provide reports for most of the events in the project ([New line in django messages](https://stackoverflow.com/questions/58415186/how-to-make-a-new-line-in-django-messages-error)).  

### Future Features  
- Separate the subscription functionality into its own app.
- Replace reliance on forms by creating a dedicated model for newsletters to store them in the database.
- Enhance the icons in the navigation menu for a more unique and engaging design.
- Implement product variation stock management to accurately track available quantities.
- Integrate a product image gallery to showcase multiple images for each product.
- Optimize image sizes to improve website performance and loading times.
- Enhance the style of emails sent for registration and order confirmation
- Divide CSS and JavaScript files so that they load only when needed for specific apps
- Allow non-registered users to shop
- Improve filtering of products
- Implement a wishlist functionality that allows users to save and track their favorite products 
- Like / dislake reviews functionality
- Add list of countries with [Django Countries](https://pypi.org/project/django-countries/)

---  

## Validation and Testing
 
### Validation   
- Python files have passed validation through [CI Python Linter](https://pep8ci.herokuapp.com/), for some lines of code longer than 79 characters `# noqa` to ignore warnings in `settings.py`
- JavaScript when tested with [JSHint](https://jshint.com/) shows:  
   `One undefined variable Swiper`    
   `One unused variable`  
   `Two undefined variables Stripe and orderId`  
this is probably because they are loaded from other scripts.
- First I used [Autoprefixer](https://autoprefixer.github.io/) to add vendor prefixes and then validate with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and it shows no errors.  
- I tested the HTML page by page by copying the source code and directly input validating at [W3C Markup Validation Service](https://validator.w3.org).
- On Google Lighthouse, the results varied between 90 and 100, with the fact that for mobile devices the performance tests sometimes dropped to lower numbers which is probably due to unoptimized images, unfortunately I didn't have time to convert them to webp format and adjust them, while for other items they remained in the range of 90 to 100. It has been prioritized to be improved in the next version.

### Testing   
- Regarding responsiveness, the site was tested on several different devices and proved to be satisfactory, although there is room for improvement.   
- Creating a user and getting a welcome email based on testing so far works well, although the message needs to be formatted better.  

<table>
   <thead>
     <tr>
       <th>Expected </th>
       <th>Testing</th>
       <th>Result</th>
       <th>Fix</th>
   </thead>
   <tbody>
     <tr>
        <td>Incorrect URL / 404 Error Page</td>
        <td>Entered incorrect URL by deleting/inserting a letter</td>
        <td>404 Error Page displayed</td>
        <td></td>
     </tr>
     <tr>
        <td>Redirect to sign-in page</td>
        <td>
        Visited URLs protected with login_required decorator (a few exmples):
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/account/dashboard/
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/account/user_orders/
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/account/update_profile
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/account/set_new_password
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/account/password_change
            https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/newsletter
        </td>
        <td>Always redirected to sign-in page</td>
        <td></td>
     </tr>
     <tr>
        <td>Error for non-admin logged-in user when visiting page protected user_passes_test</td>
        <td>Visited URL protected with user_passes_test (https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/newsletter), logged in as non-admin</td>
        <td>Received a 404 error page</td>
        <td></td>
     </tr>
     <tr>
        <td>Access grant for admin logged-in user when visiting page protected user_passes_test</td>
        <td>Visited URL protected with user_passes_test, logged in as admin</td>
        <td>Successfully accessed the page	</td>
        <td></td>
     </tr>
     <tr>
        <td>Only the author of a review can delete it.</td>
        <td>I attempted to directly delete a review from another user:
https://sun-and-peaches-72eca0ee8a6a.herokuapp.com/shop/delete_review/14/</td>
        <td>I was unable to delete the review and received a message stating that the review either doesn't exist or I don't have permission to delete it.</td>
        <td></td>
     </tr>
     <tr>
        <td>The number of purchased products should be deducted from the stock.</td>
        <td>I purchased several products,</td>
        <td>The stock of those products was appropriately reduced.</td>
        <td></td>
     </tr>
     <tr>
        <td>The registration form enforces password criteria: minimum length of 6 characters, at least one number, at least one capital letter, and at least one special symbol. If passwords do not match or meet the criteria, the form submission is blocked.</td>
        <td>I attempted registration with passwords that did not match. I also tried registering with matching passwords that lacked at least one of the mandatory conditions.</td>
        <td>I was only able to successfully register when I satisfied all password criteria, ensuring the form submission was successful and I received a registration confirmation email.</td>
        <td></td>
     </tr>
     <tr>
        <td>The search functionality allows users to search by product name, product description, price, and category. When entering values that do not exist in the search, the system should provide no results. When entering values that match existing products, the system should display results according to the search condition.</td>
        <td>I entered various values that were not present in the search. I also entered values that matched existing products in the search.</td>
        <td>As expected, entering values that do not exist resulted in no search results being displayed.
When entering values that matched existing products, the search results were displayed based on the search criteria.</td>
        <td></td>
     </tr>
     <tr>
        <td>As a logged-in admin, I should be able to send styled newsletters using the Rich Text Editor. The recipients' input field should be automatically filled with subscribers' email addresses.</td>
        <td>I attempted to send a newsletter and observed the behavior.</td>
        <td>The newsletter email was successfully styled using the Rich Text Editor, and the recipients' input field was pre-filled with the email addresses of subscribers.</td>
        <td></td>
     </tr>
   </tbody>
 </table>


### Bugs   
- Currently, there is no quantity control for product variations, I consider adding a stock variation field to the model and implementing a method to calculate the total stock for the product. This will allow for better control and management of product variations' stock levels. This fix is planned for the next update.
- Maybe it's not a bug, but the custom cursor can probably bother users. In the next upgrade remove or maybe allow the user to click a switch to choose what they want to use

#### Fixed Bugs  
- Bug: I was using "except ObjectNotExist" which caused an error.
- Fix: After researching, I realized that the correct exception is "ObjectDoesNotExist," so I updated the code to use "except ObjectDoesNotExist" instead.

- Bug: Custom cursor was not precise.
- Fix: After reading https://bengammon.co.uk/custom-css-cursors-and-offset/, I followed the instructions to center the custom cursor and improve its precision.
  ```
  cursor: url(cursor.png) 15 15, pointer;
  ```
- Bug: Search function resulted in local variable 'products' and 'product_count' being referenced before assignment.
- Fix: I declared and assigned the variables 'products' and 'product_count' with default values of 0 to avoid the referenced before assignment error in the search function.

- Bug: On the checkout page, the form field was named "phone" which did not match the model field "phone_number".
- Fix: Changed the form field name to "phone_number" to match the model field and ensure proper data binding on the checkout page.

- Bug: The search functionality was not displaying products on the next page when paginating.
- Fix: Added the query parameter to the pagination links so that the search query is preserved on the next page using &q={{ request.GET.q }}.

Bug: scripts.js:70 Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')
```
  const dashboard = document.querySelector("#dashboard-nav-icon");
  const dashboardNav = document.querySelector(".dashboard-list");
  dashboard.addEventListener('mouseover', () => { dashboard.classList.toggle("fa-bounce"); }); 
  dashboard.addEventListener('mouseout', () => { dashboard.classList.toggle("fa-bounce"); });
  dashboard.onclick = (event) => { event.preventDefault(); dashboardNav.classList.toggle("active"); }; 
```
- Fix: Wrapping the code in the 'DOMContentLoaded' event listener, the script will execute only after all DOM elements are ready and accessible, preventing the error.
---  

## Deployment  
#### How to Clone
1. Go to the repository of [project](https://github.com/radule90/CI_PP_5)
    
2. Click on the Code button above the list of files
    
3. Choose one of remote URL: HTTPS, SSH, GitHub CLI and click the copy button or download a copy of the [project repository](https://github.com/radule90/CI_PP_5/archive/refs/heads/main.zip) and extract the zip file to your base folder.
    
4. In your IDE Terminal change the current working directory to the one where you want the clone
    
5. Type following code (for example is used GitHub CLI URL) in Git Bash/Terminal of IDE and press Enter:
    
    ```
    https://github.com/radule90/CI_PP_5.git
    ```
    
6. In order to work properly, it needs to be installed project requirements, type following code in Git Bash/Terminal:
    
    ```
    pip3 install -r requirements.txt
    ```
    
7. Update `ALLOWED_HOSTS` in `settings.py`, and create evn.py file and change values:
    
    ```
    import os
    
    os.environ["DATABASE_URL"] = "Your URL of ElephantSQL instance"  
    os.environ["SECRET_KEY"] = "Your secret key"  
    
    # For Debug to be True in production and False in deployment
    os.environ.setdefault("DEBUG", "True")
    
    # Please note that the email provider only uses password authentication, 2-factor authentication will not work
    os.environ["EMAIL_HOST_USER"] = "Your email address"
    os.environ["EMAIL_HOST_PASSWORD"] = "Your email password"

    # AWS credentials
    os.environ["AWS_ACCESS_KEY_ID"] = "Your AWS access key"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "Your AWS secret key"

    Stripe credentials
    os.environ["STRIPE_PUBLIC_KEY"] = "Your stripe public key"
    os.environ["STRIPE_SECRET_KEY"] = "Your stripe secret key"
    ```

8. Run the migrate command to create the data tables.  
    `python3 manage.py migrate`
    
9. Create a superuser: `python3 manage.py createsuperuser`
    
10.  Run the local server:  
    `python3 manage.py runserver`
    

#### How to Fork

1. Go to the repository of [project](https://github.com/radule90/CI_PP_5)
2. Bellow navigation bar on the top of the page in right corner you will locate Fork button
3. When clicked, you should have a copy of repository in your GitHub


### Heroku Deployment
- A requirements.txt file created with pip3 freeze > requirements.txt.
    
- Procfile `web: gunicorn sun_and_peaches.wsgi:application`
    
- Create a new [Heroku](https://heroku.com/) app, select name and region
    
- Add Config Var to Heroku settings, where key is PORT and the value is 8000 and also add Congig Vars for:
    
    ```
    DATABASE_URL            "Your URL of ElephantSQL instance"  
    EMAIL_HOST_PASSWORD     "Your email password"    
    EMAIL_HOST_USER         "Your email address"   
    SECRET_KEY              "Your secret key"  
    AWS_ACCESS_KEY_ID       "Your AWS access key"
    AWS_SECRET_ACCESS_KEY   "Your AWS secret key"
    STRIPE_PUBLIC_KEY       "Your stripe public key"
    STRIPE_SECRET_KEY       "Your stripe secret key"
    ```
    
- In Settings, set the buildpacks to Python
    
- In Deploy section, select the Github repository from the menu
    
- Link the Heroku app to the Github repository
    
- Deploy the repository
    
- Click the View App button to see live version of the project   

---   

## Tools and Platforms   
- [Codeaynwhere](https://codeanywhere.com/) - IDE for project development
- [Github](https://github.com/) - Storing code remotely
- [Heroku](https://heroku.com/) - Deployment
- [ElephantSQL](https://www.elephantsql.com) - Database hosting service
- [AWS](https://aws.amazon.com/) 
- [Stripe](https://stripe.com/en-gb-de)
- [Django](https://www.djangoproject.com) - Python web framework
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [JSHint](https://jshint.com/) - JSHint, a JavaScript Code Quality Tool
- [W3C Markup Validation Service](https://validator.w3.org)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [CSS Autoprefixer](https://autoprefixer.github.io/) - Autoprefixer CSS online
- [Autoprefixer](https://autoprefixer.github.io/) - Autoprefixer is a PostCSS plugin which parses your CSS and adds vendor prefixes
- [Balsamiq Wireframes](https://balsamiq.com/) - Wireframes
- [DrawSQL](https://drawsql.app/) - Database diagrams
- [Python](https://www.python.org/)
- [SVG Repo](https://www.svgrepo.com)
- [SVG to CSS converter](https://www.svgbackgrounds.com/tools/svg-to-css/)
- [FireShot: Full Webpage Screenshots + Annotations](https://getfireshot.com/) - Screen Capture
- [cloudconvert](https://cloudconvert.com/png-to-webp) - Online png to webp converter  
- [Favicon Generator](https://www.favicon-generator.org/)
- [TinyMCE](https://www.tiny.cloud/) - Rich Text Editor
- [Gunicorn](https://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX
- [psycopg2](https://github.com/psycopg/psycopg2) - Python-PostgreSQL Database Adapter
- [DJ-Database-URL](https://github.com/jazzband/dj-database-url)
- [Swiper JS](https://swiperjs.com/) - Product, Image Slider

---

## Content and Credits  
- The following articles and tutorials helped me arrive at the final code solution
  - [Code Institute](https://codeinstitute.net/de/)
  - Rory Patrick Sheridan (Mentor) - Great advice and guidance
  - [Python Django Ecommerce | Advanced Django Web App From Basic](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/) - Used as base for this project
  - [100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/) - Great tutorials and learning resource
  - [Python Lessons](https://www.youtube.com/@PyLessons) - Great tutorials and learning resource
  - [Django documentation](https://www.djangoproject.com/) - Additional learning resources
  - [W3Schools](https://www.w3schools.com) - Additional learning resources
  - [Corey Schafer](https://www.youtube.com/@coreyms) - Great tutorials and learning resource
  - [Django Mastery](https://www.youtube.com/@djangomastery) - Great tutorials and learning resource
  - [Dennis Ivy](https://www.youtube.com/@DennisIvy) - Tutorials and learning resource
  - [Django Countries](https://pypi.org/project/django-countries/) - Django application that provides country choices for use with forms
  - [SVG Repo](https://www.svgrepo.com)
  - [SVG to CSS converter](https://www.svgbackgrounds.com/tools/svg-to-css/)
  - [django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/6.2.0/)
  - [Django Slug Tutorial](https://learndjango.com/tutorials/django-slug-tutorial)  
  - [ChatGPT](https://openai.com/blog/chatgpt) - For textual content (e.g. about, address)

---

## Media   
  - [babs the label](https://babsthelabel.com/) - Product pictures, description
  - [SVG Repo](https://www.svgrepo.com) - Mouse cursors, favicon
  - [FontAwesome](https://fontawesome.com/) - Social network icons
  - [Devicon](https://devicon.dev/) - Icons representing programming languages
  - [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) - Antartica map
