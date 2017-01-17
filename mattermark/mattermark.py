###############################################################################
# Python wrapper for the Mattermark API.
#
# Author: Carl Cortright
# Date: 10/27/2016
# Updated: 1/16/2017
#
################################################################################
import requests

class mattermark:
    COMPANIES_URL = "https://api.mattermark.com/companies"
    INVESTOR_URL = "https://api.mattermark.com/investors"
    SEARCH_URL = "https://api.mattermark.com/search"
    FUNDING_URL = "https://api.mattermark.com/fundings"
    QUERIES_URL = "https://api.mattermark.com/queries"
    queries = 0

    #
    # Initialization function
    #
    def __init__(self, api_key):
        self.api_key = api_key
        payload = {"key": self.api_key}
        if(requests.get(self.COMPANIES_URL, payload).status_code == 403):
            raise ValueError("Invalid API key")
        else:
            self.queries += 1

    #
    # Searches for a company and returns a dictionary of results
    #
    def companySearch(self, company):
        payload = {"key": self.api_key, "term": company, "object_types": "company"}
        result = requests.get(self.SEARCH_URL, payload)
        self.queries += 1
        return result.json()

    #
    # Searches for an investor and returns a dictionary of results
    #
    def investorSearch(self, investor):
        payload = {"key": self.api_key, "term": investor, "object_types": "investor"}
        result = requests.get(self.SEARCH_URL, payload)
        self.queries += 1
        return result.json()

    #
    # Returns a dictionary of details about a company given the ID
    #
    def companyDetails(self, companyID):
        company_url = self.COMPANIES_URL + "/" + str(companyID)
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        self.queries += 1
        return result.json()

    #
    # Returns a dictionary of news stories about a company
    #
    def companyNews(self, companyID):
        company_url = self.COMPANIES_URL + "/" + str(companyID) + "/stories"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        self.queries += 1
        return result.json()

    #
    # Returns a list of similar companies
    #
    def similarCompanies(self, companyID):
        company_url = self.COMPANIES_URL + "/" + companyID + "/similar"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        self.queries += 1
        return result.json()

    #
    # Returns a dictionary of important people at the company
    #
    def companyPersonnel(self, companyID):
        company_url = self.COMPANIES_URL + "/" + companyID + "/people"
        payload = {"key": self.api_key}
        result = requests.get(company_url, payload)
        self.queries += 1
        return result.json()

    #
    # Gets all of the funding events from a certain day
    #
    def fundingEvents(self, date=None, Pages=1):
        funding_list = []
        # If the date is None, then we get the events from today
        if(date != None):
            payload = {"key": self.api_key, "date": str(date)}
        else:
            payload = {"key": self.api_key}
        results_p1 = requests.get(self.FUNDING_URL, payload)
        self.queries += 1
        for funding in results_p1["fundings"]:
            funding_list.append(funding)
        if(results_p1["meta"]["total_pages"] > 1 and Pages > 1):
            if(Pages < results_p1["meta"]["total_pages"]):
                Pages = int(results_p1["meta"]["total_pages"])
            for i in range(2, Pages+1):
                payload["page"] = i
                result = requests.get(self.FUNDING_URL, payload)
                self.queries += 1
                results = result.json()
                for funding in results["fundings"]:
                    funding_list.append(company)
        return funding_list

    #
    # Returns the details about an investor given their id as a dictionary
    #
    def investorDetails(self, investorID):
        investor_url = self.INVESTOR_URL + "/" + str(investorID)
        payload = {"key": self.api_key}
        result = requests.get(investor_url, payload)
        self.queries += 1
        return result.json()

    #
    # Return a list of the companies in the investor's portfolio
    #
    def investorPortfolio(self, investorID, Paging=True):
        company_list = []
        url = self.INVESTOR_URL + "/" + str(investorID) + "/portfolio"
        payload = {"key": self.api_key}
        result = requests.get(url, payload)
        self.queries += 1
        results_p1 = result.json()
        # Add each company to the list
        for company in results_p1["companies"]:
            company_list.append(company)
        # Deal with paging
        if(results_p1["meta"]["total_pages"] > 1 and Paging == True):
            for i in range(2, results_p1["meta"]["total_pages"]+1):
                payload = {"key": self.api_key, "page": i}
                result = requests.get(url, payload)
                self.queries += 1
                results = result.json()
                for company in results["companies"]:
                    company_list.append(company)
        return company_list
