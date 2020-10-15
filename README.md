Mars Scraper

The goal is to create a dashboard which scrapes specific websites for information. First a script is created that scrapes and returns information which is then stored in a DataBase, in this case a MongoDB structureless DB. 

Concepts introduced in this exercise are Splinter and Beautiful Soup, as well as the Mongo DB structureless database. Splinter Browswer can automate browser functions and will be used here to visit several websites. Splinter works in complement with Beautiful Soup. Once splinter visits a site, BS will parse the site's HTML. It is then up to the user to identify the information they need from the HTML based on the HTML tags. 

Having a jupyter Notebook is helpful as it allows us to test the script, which includes the automated browser visiting the various sites, collecting the HTML, which is then 