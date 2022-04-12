"""
Create a query for OpenAlex using specific search criteria,
which will be passed into a function
"""

import os
import requests


# if using this package locally please set your own email address as an environmental variable
email_address = os.environ['email_address']

def works_query_from_doi(doi = "10.7861/clinmedicine.19-2-169", email = email_address):
    # accepts a doi and returns a url query string for OpenAlex
    url = f"https://api.openalex.org/works/doi:{doi}?mailto:{email_address}"
    return url
