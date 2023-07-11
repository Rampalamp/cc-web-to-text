### Crozier Creative Web To Text

Python project that aims to extract text from websites. My intent is that eventually you will be able to choose between querying a google search, and the scraper will go through every link returned by google (likely set limits to how many returned pages to scan over), OR just on a single given website URL.

I was seeing a lot of people loading their own, small or large, data sets into some locally running variety of NLPs. Hopefully (eventually), this project will be able to help populate some data based off of a single google search by :  
quickly going to each returned link  
extracting text  
dumping it into a .txt file  
this .txt file can then be used in an NLP that they control.

I suspect that if the data is not formatted/cleaned up to a certain extent, this will likely just cause confusion for the poor machines, alas....

I also suspect this (text extraction from websites) has almost certainly be done to a much greater extent already, but I felt like doing one myself. How long will I put effort towards this? TBD...

#### TODOs

Likely need to clean up the formatting, although it is returning text excluding all the HTML tags, it's still not very clean.
Setup the goog_scrape.py so that it will perform a query on google and iterate through the returned links, pulling and formatting text from each returned link.

#### Usage/Example

```bash
    python main.py -u https://www.google.ca/
```

Running this command should place a .txt file inside the fetched_data folder.
