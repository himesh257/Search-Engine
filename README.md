# Search Engine


This is a python based general purpose search engine project. Using python modules, i created a very simple general purpose search engine using google's API. This is (sadly) not a replacement for Google or any other high profile search engine. 

Tools:
1) Python (and python modules)
2) Flask
3) AJAX
4) html, CSS, and Bootstrap
    
Features:
1) Users can search for any search term and 5 search results will be displayed 
2) Users can either search for PDF files or simple URLs
3) Users can bookmark their favourite sites, and it will be saved in the database fo future reference
4) Search history will be recorded as wll
5) Url results will also display some description of the website
6) used CSS and Bootstrap to add some effects
    
Limitations:
1) we only display five search results as web scraping and using google's database to search can be illegal
2) we could've used Mongodb or SQL or any other database management systems but as this is not being deployed to any domain, graders will have difficulties with saving the data (eg. maybe Mongodb or SQL is not installed in their local machines, even if the website were to be deployed, with database, it is not free and I'm broke!)
3) the search results might take some time to generate, as we are using third-party package to generate them, hence we don't have control over it (PDF searching is relatively faster)

How to run the code?
1) users do not need to install any packages (given that the code is being run on Linux OS)
2) to activate virtual environment use this command
        --(in project directory) . /venv/bin/activate
3) after activating the virtual environment run, 
        --python main.py
        (this will start the website on localhost)

How to use it?
1) in order to search for a URL, select "URL" option next to the input tab, and click on "SearchURL" button to see the results. 
2) for PDFs, select "PDF" option and click on "SelectPDF" button (see the screenshot)
3) clicking on "ADD" button, saves the result in bookmarks (see the screenshot)
4) clicking on "Bookmarks" icon will show Bookmarks (see the screenshot)
5) any generated search results are saved in "History" along with the date and time of its search (see the screenshot)
    
    
    
    
    
