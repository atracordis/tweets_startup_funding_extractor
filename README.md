# Startup funding metadata extractor from Tweets

This project scrapes tweets from the techcrunch user then scrapes and puts in order metadata about startups funding, such as date, series, investors...

### Prerequisites

```
GetOldTweets3
regex
bs4
selenium
spacy
```

### Installing

Use Git Bash (https://gitforwindows.org/) on Windows (or install make) to create a virtual environment and activate it

```
make venv
source ./activate_venv
```

then you can execute the main file for a demonstration 

```
python main.py
```

## Built With

* [Selenium](https://www.selenium.dev/) - To manipulate browser from code
* [Chrome Driver](https://chromedriver.chromium.org/) - Version 83
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) - Tag manipulation in Python
* [SpaCy](https://spacy.io/) - NLP in Python

## Authors

* **Wajd MESKINI** 
