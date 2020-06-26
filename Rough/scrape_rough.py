from bs4 import BeautifulSoup
import pandas as pd
import time
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
    
def scrape():
    browser = init_browser()
    
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(3) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    articles = soup.find('div', class_= "list_text")
    news_title = articles.find('div', class_= 'content_title').text
    news_p = articles.find('div', class_ = 'article_teaser_body').text
    print(news_title)
    print('---')
    print(news_p)

    mars_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_url)
    time.sleep(3) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find('a', class_ = 'fancybox')['data-fancybox-href']
    featured_image_url = (f'//www.jpl.nasa.gov{featured_image}')
    print(f'The website is {featured_image_url}')
    
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    time.sleep(3) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    mars_weather = soup.find('div', class_ = "css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").get_text()
    print(mars_weather)
    
    facts_url = 'https://space-facts.com/mars/'
    fact_tables = pd.read_html(facts_url)
    comparison = fact_tables[1]
    comparison.set_index('Mars - Earth Comparison')
    html_comp = comparison.to_html(index = False)
    html_comp.replace('\n', '')
    print(html_comp)
    
    overview = fact_tables[0]
    ov = overview.rename(columns = {0 : "Profile", 1 : 'Statistic'})
    ov.set_index('Profile')
    html_ov = ov.to_html(index = False)
    html_ov.replace('\n', '')
    print(html_ov)


    hemispheres = ['Cerberus', 'Schiaparelli', 'Syrtis Major', 'Valles Marineris']
    hemisphere_image_urls = []
    for i in hemispheres:
        hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemis_url)
        browser.click_link_by_partial_text(i)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        i_image_url = soup.find('img', class_ = 'wide-image')['src']
        i_image = (f'https://astrogeology.usgs.gov{i_image_url}')
        hemisphere_image_urls.append({'Hemisphere' : f'{i} Hemisphere', 'img_url' : i_image})
        print(i_image)
    
    mars = {'News_Title' : news_title, 'News_Paragraph' : news_p, 'Mars_Photo' : featured_image_url, 'Mars_Weather' : mars_weather, 'Mars_Overview' : html_ov, 'Hemisphere_Photos' : hemisphere_image_urls}
    
    return mars











