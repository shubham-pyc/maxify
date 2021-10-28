from urlparse import urljoin

SITE_ID = ""
MAXYMISER_URL = "https://api-us.maxymiser.com/v1/sites/XXXXX/sandbox/"
CLIENT_ID = ""
CLIENT_SECRETE = ""
COMBINED_SECRETE = ""

# API END POINTS
COMMIT_EP = "publish" 
OAUTH_EP = "https://api-auth-us.maxymiser.com/oauth2/v1/tokens"
CAMPAGIN_SCRIPT_EP = "campaigns/$campaign_id/scripts"
VARIANT_CREATING_EP = "campaigns/$campaign_id/elements/$element_id/variants"
READ_ELEMENT_EP = "campaigns/$campaign_id/elements"
READ_CAMPAGINS_EP = "campaigns"
READ_CAMPAGINS_DETAILS_EP = "campagins/$campaign_id"

# URLS
OAUTH_URL = OAUTH_EP
COMMIT_URL = urljoin(MAXYMISER_URL,COMMIT_EP)
CAMPAGIN_SCRIPT_URL = urljoin(MAXYMISER_URL, CAMPAGIN_SCRIPT_EP)
ELEMENT_VARIANTS_URL = urljoin(MAXYMISER_URL, VARIANT_CREATING_EP)
READ_ELEMENT_URL = urljoin(MAXYMISER_URL, READ_ELEMENT_EP)
READ_CAMPAGINS_URL = urljoin(MAXYMISER_URL, READ_CAMPAGINS_EP)
READ_CAMPAGINS_DETAILS_URL = urljoin(MAXYMISER_URL, READ_CAMPAGINS_DETAILS_EP)
UPDATE_VARINT_URL = ELEMENT_VARIANTS_URL+"/$variant_id"
UPDATE_CAMPAGIN_SCRIPT_URL = CAMPAGIN_SCRIPT_URL + "/$script_id"

# HEADER
GENERIC_HEADER = {
    "Authorization": COMBINED_SECRETE,
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
}

# Exception Messages


# print(x.encode("byte"))
