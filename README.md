Mars Scraper

The goal is to create a dashboard which scrapes specific websites for information. First a script is created that scrapes and returns information which is then stored in a DataBase, in this case a MongoDB structureless DB. That information is served up through flask and presented in an HTML dashboard. A button on the dashboard is a reference to the 'scrape' endpoint, which instantiates the scape function, which runs the script and scapes the data and updates the DataBase with the most recently scraped data. At the end of the scrape function, the app is redirected to the dashboard home endpoint, which finds the Database and renders the HTML.

Concepts introduced in this exercise are Splinter and Beautiful Soup, as well as the Mongo DB structureless database. Using Django, items from within the DB are  Splinter Browswer can automate browser functions and will be used here to visit several websites. Splinter works in complement with Beautiful Soup. Once splinter visits a site, BS will parse the site's HTML. It is then up to the user to identify the information they need from the HTML based on the HTML tags. 

