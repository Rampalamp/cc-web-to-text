### Crozier Creative Web To Text

Python project that aims to extract text from websites. My intent is that eventually you will be able to choose between querying a google search (using their API), and the scraper will go through every link returned by google, OR just on a single given website URL.

I suspect this (text extraction from websites) has almost certainly been done to a much greater extent already, but I felt like doing one myself. How long will I put effort towards this? TBD...

#### TODOs

Setup the goog_scrape.py so that it will perform a query on google and iterate through the returned links, pulling and formatting text from each returned link.

#### Usage/Example

```bash
    python -m pip install -r requirements.txt
    python main.py -u https://www.google.ca/
```

Running this command should place a .txt file inside the fetched_data folder.
