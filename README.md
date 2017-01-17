# Mattermark API Wrapper
[![PyPI version](https://badge.fury.io/py/mattermark.svg)](https://badge.fury.io/py/mattermark)

> Python wrapper for the Mattermark REST API

[Mattermark](https://www.mattermark.com) is the best repository of company data on the internet. It is used by marketers and data scientists everywhere to get relevant information on the companies they care about. Mattermark provides an awesome REST API that allows developers to integrate their service into custom solutions for teams and organizations. At Foundry group we use Mattermark to help us stay up-to-date with the companies and fund managers we care about. The goal of this package is to make it absurdly simple to interact with the Mattermark API using Python.

## Installing

This package is register with PyPi, so all that is needed for installation is to run:

`pip install mattermark`

## Usage

To use the API start by creating a new mattermark instance

```python
import mattermark
mm = mattermark.mattermark("<my api key>")
```

It then becomes simple to search for companies and investors, extract company details, get an investor's portfolio, identify key company personnel, and get relevant company news. Each method returns a dictionary that is identical to the JSON returned by the API, and for endpoints that support paging, we give you the option of grabbing multiple pages at once.

```python
# Search for Foundry Group
foundry_search = mm.investorSearch("Foundry Group")
foundryID = foundry_search[0]["object_id"]

# Get a list of Foundry Group portfolio companies
foundry_portfolio = mm.investorPortfolio(foundryID)

# Get details on the Foundry Group organization
foundry_details = mm.investorDetails(foundryID)

mm.queries # Keeps track of the number of queries that have been used

```

We also support the funding events endpoint that returns all recent funding events.

```python

# Get some of the funding events that have happened today
events = mm.fundingEvents()

# Get even more funding events
more_events = mm.fundingEvents(Pages=10) # Will get the first 10 pages (500 events)

```

The companies endpoint makes it easy to get information about a specific company.

```python

# Search for "mattermark" in the company database
mattermark_search = mm.companySearch("mattermark")
mmID = mattermark_search[0]["object_id"]

# Get details on the company
mattermark_details = mm.companyDetails(mmID)
mm_score = mattermark_details["mattermark_score"]

# Get the key personnel
key_people = mm.companyPersonnel(mmID)

# Get the articles about the company
news = mm.companyNews(mmID)

# It is also easy to find similar companies
mm_similar_companies = mm.similarCompanies(mmID)
```

We also support the more advanced companies list endpoint that returns search results based on a variety of criteria.

```python
parameters = {"last_funding_date": "raised in past 9 months", "industries": "Finance"}
company_list_search = mm.companiesList(parameters)
```

To learn more about the different parameters for the company list endpoint please see the [mattermark API documenation](https://mattermark.com/api/documentation/)

## Recommended Key Storage

It is recommended that you store your API key in either a config file or as a system variable, and only read it when you need to create a new mattermark object. An example would be to create a new entry in your projects config.yml file, making sure this file stays untracked by version control:

```YAML
MM_API_KEY: <Your API Key>

```

Then you can use the PyYAML package to get the key any time you want to use it:

```python
config_file = open(".config.yml")
config_dict = yaml.safe_load(config_file)
config_file.close()
MM_API_KEY = config_dict["MM_API_KEY"]
```
