'''
    This module contains code responsible for
    1: Creating folder structure
    2: Creating campaign files
    3: Injecting boilterplate code into files
'''

#import sys
import os
import json
#import re
from string import Template
import openpyxl as excel
import maxify.assistants.campaign_assistant.constants as constants


from maxify.modals.campaign import CLICampaign, MaxymiserCampaign
from .utils import make_abbreviation, merge_conditions
from .lib import criteria as conditions
from .lib import configurations_code as code





class CampaignAssistant:
    '''Class CampaginAssistant responsible for
        1: Creating folder structure
        2: Creating campaign files
        3: Injecting boilterplate code into files
    '''

    def __init__(self, campaign, user, exception_handler):
    #def __init__(self,campaign_name, creator,debug = False, variants = 1,is_booking_path = True):
        '''
            Constructor Function
            :Param campaign: campaign objects
            :Param user: User Object with credentials
            :Param exception_handler
        '''
        self.campaign = campaign
        self.creator = user
        self.e_handler = exception_handler
        # self.campaign.variants = self.campaign.variants

    # Creates required folders

    def setup_folder(self):
        '''
            Method to setup all the required folders
        '''
        try:
            path_list = [
                self.campaign.campaign_path,
                self.campaign.requirment_folder,
                self.campaign.source_folder,
                self.campaign.campaign_scripts_folder,
                self.campaign.vscode_folder,
                self.campaign.test_suite_folder,
            ] + self.campaign.elements_folders

            if type(self.campaign) is CLICampaign:
                path_list += [self.campaign.variant_scripts_folder]

            if not os.path.exists(self.campaign.campaign_path):
                for folders in path_list:
                    os.mkdir(folders)
                self.campaign.is_folder_setup = True
                print("Created Directory at : {}".format(
                    self.campaign.campaign_path))
        except Exception as e:
            self.e_handler.handle_exception(e)

    # Creates all the initials files
    def inject_files(self):
        '''
            Method to create all the required files
            1) Qualification Script
            2) Analytics Script
            3) All Variant Scripts
            4) Tasks script
        '''
        files_to_create = [
            self.campaign.qualification_script,
            # self.campaign.common_script,
            self.campaign.analytics_script,
            self.campaign.vscode_task_file,
        ] + self.campaign.variant_script_files + self.campaign.site_scripts
        try:
            if os.path.exists(self.campaign.campaign_path) and self.campaign.is_folder_setup:
                if type(self.campaign) is MaxymiserCampaign:
                    files_to_create += [self.campaign.configuration_file]

                for script in files_to_create:
                    open(script, 'a').close()

                if type(self.campaign) is CLICampaign:
                    for i in range(1, self.campaign.variants+1):
                        open(self.campaign.variant_script_file.replace(
                            "$", str(i)), 'a').close()

            # self.create_dev_suit()
        except Exception as e:
            self.e_handler.handle_exception(e)

    # Method to insert boilerplate code into all the files
    def populate_file(self):
        '''
            Method to inject code into files
            1) Common script
            2) Qualification Script
            3) Variant Scripts
        '''

        file_code_mapping = {
            self.campaign.qualification_script: code.QUALIFICATION_CODE,
            # self.campaign.common_script:code.COMMON_CODE,
            self.campaign.analytics_script: code.ANALYTICS_CODE,
            self.campaign.vscode_task_file: code.TASK_CODE,
        }

        try:

            for variant_name in self.campaign.variant_script_files:
                if variant_name not in file_code_mapping:
                    file_code_mapping[variant_name] = code.VARIANT_CODE

            if type(self.campaign) is CLICampaign:
                for i in range(1, self.campaign.variants+1):
                    variant_name = self.campaign.variant_script_file.replace(
                        "$", str(i))
                    if variant_name not in file_code_mapping:
                        file_code_mapping[variant_name] = code.VARIANT_CODE
            elif type(self.campaign) is MaxymiserCampaign:
                file_code_mapping[self.campaign.configuration_file] = json.dumps(
                    self.campaign.configurations)
                

                
                file_code_mapping.update(self.campaign.script_content_mapping)


            # created an abbreviation for the campaign for data layer object
            abbreviation = make_abbreviation(
                self.campaign.campaign_name, self.campaign.is_booking_path)

            # Check if the path exists and folder is setup
            if os.path.exists(self.campaign.campaign_path) and self.campaign.is_folder_setup:
                # content contains the code for that file
                for path, content in file_code_mapping.items():
                    with open(path, 'a') as f:
                        placeholders = {
                            "replace": abbreviation,
                            "campaign": self.campaign.full_campaign_name
                        }
                        template = Template(content)
                        final_text = template.safe_substitute(placeholders)
                        try:
                            f.writelines(final_text.encode("utf-8"))
                        except  Exception as e:
                            self.e_handler.handle_exception(e)
        except Exception as e:
            self.e_handler.handle_exception(e)

    def inject_eligibility_criteria(self, criterias):
        '''
            Method to inject Eligibility Creterial into Qualification Scripts
            :Param criterias: list of elibigility criterias
        '''
        file_mapping = self.get_condition_mapping()
        checked_conditions = {}
        conditions_to_check = []
        function_to_call = []
        condition_to_inject = ""
        try:
            with open(self.campaign.qualification_script, 'a+') as script:

                for criteria in criterias:
                    if criteria in file_mapping:
                        condition_object = file_mapping[criteria]
                        script.writelines(condition_object['code'])
                        conditions_to_check.append(
                            condition_object['requirement'])
                        function_to_call.append(condition_object['call'])

                condition_to_inject = merge_conditions(conditions_to_check)
            filedata = ""
            with open(self.campaign.qualification_script, 'r') as script:
                filedata = script.read()

                # Placeholders to replace in templates
                placeholders = {
                    "condition": condition_to_inject,
                    "functioncall": " && ".join(function_to_call)
                }
                template = Template(filedata)
                filedata = template.safe_substitute(placeholders)

            with open(self.campaign.qualification_script, 'w') as script:
                script.writelines(filedata)

        except Exception as e:
            self.e_handler.handle_exception(e)

    def create_dev_suit(self):
        '''
            Method to create basic dev test suits
        '''
        try:
            value_mapping = {
                "campaign name": self.campaign.full_campaign_name,
                "reviewed by": self.creator.name
            }
            work_bench = excel.load_workbook(
                constants.DUMMY_DEV_TEST_SUITE_PATH)
            for sheet_name, config_object in constants.SHEET_CONFIG["sheet names"].items():
                current_sheet = work_bench.get_sheet_by_name(sheet_name)
                for value_key, coordinate in config_object.items():
                    if value_key in value_mapping:
                        current_sheet[coordinate] = value_mapping[value_key]
            work_bench.save(self.campaign.test_suite_file)
        except Exception as e:
            self.e_handler.handle_exception(e)

    def get_condition_mapping(self):
        '''
            Method to return elibigility criteria and it's code mapping
            :returns: Dic["elibigility criteria":"Code"]
        '''
        return conditions.CRITERIA_CODE_MAPPING

    def assist(self):
        '''
            Method to do all the magic
        '''
        try:
            self.setup_folder()
            self.inject_files()
            self.populate_file()
            condition_mapping = self.get_condition_mapping()
            if self.campaign.conditions:
                for condition in self.campaign.conditions:
                    if condition not in condition_mapping:
                        raise ValueError(
                            "Invalid Condition {}".format(condition))
                self.inject_eligibility_criteria(self.campaign.conditions)
            return self.campaign.campaign_path
        except Exception as e:
            self.e_handler.handle_exception(e)
