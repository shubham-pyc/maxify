import requests
import json
import ast
import traceback
import maxify.assistants.maxymise_assistant.constants as const
from string import Template
from .utils import get_campagin_id_from_name
from maxify.services.exception_handler import ExceptionHander


class MaximizerAssistant():
    def __init__(self, campaign, user):
        self.campaign = campaign
        self.user = user
        self.url = const.MAXYMISER_URL
        self.token = None
        self.campaign_id = ""

        if isinstance(campaign, dict):
            self.campaign_id = campaign.get("id", "")

    def get_headers(self):
        return {
            "Authorization": "Bearer {}".format(self.token),
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }

    def convert_byte_to_dict(self, byte):
        '''
            Method to convert bytes array to hash table
            :Param byte: bytes array
            :Returns dict:
        '''
        ret_value = None
        try:
            ret_value = ast.literal_eval(byte.decode("utf8"))
        except Exception as e:
            print(e)
        return ret_value

    def get_campaign_details(self):
        '''
            Method to get campaign details
            :Returns Dict: dict with campaign details
        '''
        ret_value = {}
        try:
            if not self.token:
                raise ValueError("Auth Token not found")
            url = const.READ_CAMPAGINS_DETAILS_URL.replace(
                "$campaign_id", self.campaign_id)
            headers = self.get_headers()
            request = requests.get(url, headers=headers)
            ret_value = self.convert_byte_to_dict(request.content)
        except Exception as e:
            print(e)

        return ret_value

    def get_campaigns(self):
        '''
            Method to get campaign details
            :Returns Dict: dict with campaign details
        '''
        ret_value = {}
        try:
            if not self.token:
                raise ValueError("Auth Token not found")
            url = const.READ_CAMPAGINS_URL
            headers = self.get_headers()
            request = requests.get(url, headers=headers)
            ret_value = json.loads(request.content)
        except Exception as e:
            print(e)

        return ret_value

    def get_oauth_token(self):
        '''
            Method to get auth token
        '''
        try:
            print("Acquiring oauth token")
            url = const.OAUTH_URL
            headers = {
                "Authorization": const.COMBINED_SECRETE,
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
            }
            param = {
                "grant_type": "password",
                "username": self.user.username,
                "password": self.user.password
            }
            request = requests.post(url, headers=headers, data=param)
            data = None
            if request and request.content:
                data = self.convert_byte_to_dict(request.content)
            if data and "access_token" in data:
                self.token = data["access_token"]
                self.save_state()  # Function to save oauth token for future use
                print("Acquired oauth token")
            else:
                print("Problem in Acquiring oauth token")
        except Exception as e:
            traceback.print_stack(e)
            print(e)

    def create_script(self, script_name, content):
        '''
            Function to create script in a campaign
            :Param script name: name of the script
            :Param content: javascript
        '''
        try:
            if not self.token:
                raise ValueError("Auth Token not found")
            url = const.CAMPAGIN_SCRIPT_URL
            headers = self.get_headers()
            body = {
                "name": script_name,
                "description": "something",
                "content": content.encode("UTF-8")
            }
            request = requests.post(url, data=body, headers=headers)
            print(request.content)
        except Exception as e:
            print(e)

    def create_variants(self, content):
        '''
            Function to create a variant on maxymiser
            :Param content: html script
        '''
        try:
            if not self.token:
                raise ValueError("Auth Token not found")

            variants = 5
            variant_url = Template(const.ELEMENT_VARIANTS_URL)
            headers = self.get_headers()
            configuration = {
                "campaign_id": self.campaign_id,
                "element_id": "MTUwNjE1"
            }
            for x in range(variants):
                print("running")
                url = variant_url.substitute(configuration)
                body = {
                    "name": "Variant{}".format(x+1),
                    "content": content
                }
                response = requests.post(url, headers=headers, data=body)
                print(response.content)
        except Exception as e:
            print(e)

    def read_all_elements(self):
        '''
            Function to read all the elements of the campaign
            :Returns Dict: dict object containig all elements
        '''
        ret_value = []
        try:
            configuration = {
                "campaign_id": self.campaign_id,
            }
            url = Template(const.READ_ELEMENT_URL).substitute(configuration)
            headers = headers = self.get_headers()
            response = requests.get(url, headers=headers)
            ret_value = json.loads(response.content)

        except Exception as e:
            print(e)
        return ret_value

    def read_element(self, element_id):
        '''
            Function to read an element of the campagin
            :Param element_id: ID of the element
            :Returns dict: Information of the element
        '''
        ret_value = []
        try:
            configuration = {
                "campaign_id": self.campaign_id,
                "element_id": element_id
            }
            url = Template(const.ELEMENT_VARIANTS_URL).substitute(
                configuration)
            headers = headers = self.get_headers()
            response = requests.get(url, headers=headers)
            ret_value = json.loads(response.content)
            # print(ret_value)
        except Exception as e:
            print(e)
        return ret_value

    def read_campaign_scripts(self):
        '''
            Function to read the scripts of a campaign
            :Returns dict: information related to all scripts
        '''
        ret_value = []
        try:
            configuration = {
                "campaign_id": self.campaign_id,
            }
            url = Template(const.CAMPAGIN_SCRIPT_URL).substitute(
                configuration)
            headers = self.get_headers()
            response = requests.get(url, headers=headers)
            ret_value = json.loads(response.content)
        except Exception as e:
            print(e)

        return ret_value

    def save_state(self):
        '''
            Function to save state i.e oauth token for furture use
        '''
        try:
            pass
            # print(self.token)
        except Exception as e:
            print(e)

    def get_campaign_json(self, name=None):
        '''
            Function to get campaign json object from maxymiser
            :Param name: name of the campaign
            :Returns dict: object containing campaign information
        '''
        self.get_oauth_token()
        campagins = self.get_campaigns()
        campaign = get_campagin_id_from_name(
            campagins, name)
        self.campaign_id = campaign["id"]
        elements = self.read_all_elements()
        scripts = self.read_campaign_scripts()

        for element in elements["items"]:
            variants = self.read_element(element["id"])
            element["variants"] = variants["items"]
            # element["variants"] = {variant["name"]: variant["id"]
            # for variant in variants["items"]}
        campaign["elements"] = elements["items"]

        campaign["scripts"] = scripts["items"]

        del elements["items"]
        return campaign

    def update_variant_script(self, element_id, variant_id, content):
        '''
            Function to update variant script on maxymiser
            :Param element_id: ID of the element
            :Param variant_id: ID of the variant script
            :Param content: content of the script
        '''
        try:
            self.get_oauth_token()

            print("Updating variant script with id {}".format(variant_id))

            variant_url = Template(const.UPDATE_VARINT_URL)

            headers = self.get_headers()

            configuration = {
                "campaign_id": self.campaign_id,
                "element_id": element_id,
                "variant_id": variant_id
            }
            url = variant_url.substitute(configuration)
            body = {
                "content": content
            }
            response = requests.put(url, headers=headers, data=body)
            if response.status_code == 200:
                self.commit_changes()
            else:
                print("Something went wrong")
        except Exception as e:
            print(e)

    def commit_changes(self):
        try:
            print("Commiting changes")
            headers = self.get_headers()
            url = const.COMMIT_URL
            response = requests.put(url,headers=headers)
            print(response)
        except Exception as e:
            print(e)

    def update_campaign_script(self, script_id, content):

        '''
            Function to update site script on maxymiser
            :Param script_id: ID of the script
            :Param content: content of the script
        '''
        try:
            self.get_oauth_token()

            print("Updating campaign script with id {}".format(script_id))

            script_url = Template(const.UPDATE_CAMPAGIN_SCRIPT_URL)
            headers = self.get_headers()
            configuration = {
                "campaign_id": self.campaign_id,
                "script_id": script_id
            }
            url = script_url.substitute(configuration)
            body = {
                "content": content,
            }
            response = requests.put(url, headers=headers, data=body)
            response.raise_for_status()
            print("Script updated")
            self.commit_changes()
        except Exception as e:
            print(e)
        pass

    