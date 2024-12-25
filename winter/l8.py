"""
# Scraping the Web

In this notebook, we attempt to scrap UChicago's Course Catalog.
"""

"""
### From URL to HTML

Go to [UChicago's Economics Catalog](http://collegecatalog.uchicago.edu/thecollege/economics/) and **inspect** the page (Google how to do it).
"""
from urllib.request import urlopen
url = r"http://collegecatalog.uchicago.edu/thecollege/economics/"
page = urlopen(url)

html = page.read().decode("utf-8")
html

"""
### What are we finding?

Suppose we want to scrap the names of all courses.
Inspect again the webpage.
In what HTML tags are the names located?
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
soup.find_all("p",  {"class": "courseblocktitle"})

"""
### 
"""
course_titles = []
for a in soup.find_all("p",  {"class": "courseblocktitle"}):
    course_titles.appen(a.find("strong").text)


"""
# Task 1: Cleaning

`course_titles` includes not just the name of the courses, but also the course numbers and units worth.
Clean the data so we have just a list of course names left.

Hint: course number, course name, and units are all separated by a single period.
"""
pass

"""
# Task 2: DOI

Many scientific papers have corresponding DOIs that can be used to uniquely identify them.
Crossref provides a free API that takes in a doi and output the metadata of the associated paper.

Check out for example:
[`https://api.crossref.org/works/10.3386/w4509`](https://api.crossref.org/works/10.3386/w4509).

Write a script that takes in a DOI and outputs the authors of the associated paper.
"""
doi = r"10.3386/w4509"