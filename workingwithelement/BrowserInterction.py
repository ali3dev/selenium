from selenium import webdriver


class BrowserInteraction():
    def test(self):
        baseurl = 'https://www.letskodeit.com/'
        driver = webdriver.Firefox()

        # Window Mazimize
        driver.maximize_window()
        #open URl
        driver.get(baseurl)
        #Get Title 
        title = driver.title
        print('Title of the Web-page is:- ' + title)
        #Get Current URl
        currenturl = driver.current_url
        print('Current Url of the web page is:- ' + currenturl)
        #Browser Resfreshed 
        driver.refresh()
        print('Browsers Refreshed 1st time:- ')
        driver.get(driver.current_url)
        print('Browsers Refreshed 2nd time:- ')
        #Open Another URl 
        driver.get('https://www.letskodeit.com/login')
        #Browser back
        driver.back()
        print('Go one step back in browser history')
        #Browser forward
        print('Go one step forward in browser history')
        #Get page source 
        Page_source = driver.page_source
        #Browser Close
        # driver.close()
        #Browser Quit
        driver.quit()



browser = BrowserInteraction()
browser.test()