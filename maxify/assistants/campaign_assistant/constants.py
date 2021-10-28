
# Paths
import os
import sys



DUMMY_DEV_TEST_SUITE_PATH = os.path.join(os.path.dirname(__file__),'static','$campaign_Test_Suite.xlsx')
# ARGUMENT MESSAGES
VARIANT_ARG_MESSAGE = 'Number of variants for the campaign'
NAME_ARG_MESSAGE = "Name of the campiagn"
REMOVEPATH_ARG_MESSAGE = "Removes bookingPath from files"
DEBUG_ARG_MESSAGE = "Flag for testing purporses"
CONDITIONS_ARG_MESSAGE = "List of Conditions choice:"


# Excel Sheet Coordinates
SHEET_CONFIG = {
    "sheet names": {
        "Campaign Configuration": {
            "campaign name": "D4",
            "reviewed by": "C15",
        },
        "Eligibility Criteria": {
        },
        "Variant": {},
        "KPI Data Collection": {
            "campaign name": "D4",
            "reviewed by": "C8"
        }
    }
}
