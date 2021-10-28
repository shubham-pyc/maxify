import maxify.modals.constants as constants
import os
import re


class CLICampaign(object):
    def __init__(self, name="Default", variants=1, debug=True, is_booking_path=True, conditions=[], full_campaign_name=None):
        self.name = name
        self.elements_folders = []
        self.variant_script_files = []
        self.site_scripts = []
        self.variants = variants
        self.debug = debug
        self.is_booking_path = is_booking_path
        self.conditions = conditions
        self.folder_path = None
        self.campaign_name = self.name
        self.destination_folder = constants.ORIGINAL_FOLDER_PATH

        if self.debug:
            self.destination_folder = constants.DEBUG_FOLDER_PATH
        self.name_prefix = "QA - {}"
        if not self.is_booking_path:
            self.name_prefix = self.name_prefix.format("")
        else:
            self.name_prefix = self.name_prefix.format("BookingPath_")

        if full_campaign_name:
            self.full_campaign_name = full_campaign_name
        else:
            self.full_campaign_name = self.name_prefix + self.campaign_name


        
        #Folders

        self.campaign_path = os.path.join(
            self.destination_folder, self.full_campaign_name)
        self.requirment_folder = os.path.join(
            self.campaign_path, "Requirement")
        self.source_folder = os.path.join(self.campaign_path, "Source File")
        self.test_suite_folder = os.path.join(
            self.campaign_path, "Dev test suite")
        self.campaign_scripts_folder = os.path.join(
            self.source_folder, "campaign scripts")
        self.variant_scripts_folder = os.path.join(
            self.source_folder, "variant script")
        
        self.vscode_folder = os.path.join(self.source_folder,".vscode")


        #Files

        self.configuration_file = os.path.join(
            self.source_folder, "maxymiser.json")

        self.common_script = os.path.join(
            self.campaign_scripts_folder, "common.js")
        self.qualification_script = os.path.join(
            self.campaign_scripts_folder, "qualification.js")
        self.analytics_script = os.path.join(
            self.campaign_scripts_folder, "analytics.js")
        self.variant_script_file = os.path.join(
            self.variant_scripts_folder, "variant$.html")

        self.test_suit_name = self.campaign_name + " test suits.xlsx"
        self.test_suite_file = os.path.join(
            self.test_suite_folder, self.test_suit_name)
        
        self.vscode_task_file = os.path.join(self.vscode_folder,"tasks.json")

        self.is_folder_setup = False


class MaxymiserCampaign(CLICampaign):
    def __init__(self, configuration):
        super(MaxymiserCampaign, self).__init__(
            full_campaign_name=configuration["name"], is_booking_path=False)

        self.configurations = configuration

        self.script_content_mapping = {}

        for element in configuration["elements"]:
            element_name = "{}-{}".format(element["name"], element["id"])
            element_path = os.path.join(self.source_folder, element_name)
            
            for variant in element["variants"]:

                if variant["name"].find("variant") != -1:
                    variant_name = "{}-{}-.html".format(
                        variant["name"], variant["id"])
                    variant_path = os.path.join(element_path, variant_name)
                    self.variant_script_files.append(variant_path)
                    self.script_content_mapping[variant_path] = variant["content"]
            self.elements_folders.append(element_path)

        for site_script in configuration["scripts"]:
            
            script_name = "{}-{}-.js".format(
                site_script["name"], site_script["id"])
            script_path = os.path.join(
                self.campaign_scripts_folder, script_name)
            self.script_content_mapping[script_path] = site_script["content"]
            if re.search(r'^qualification-.*-\.js$', script_name, re.IGNORECASE):
                self.qualification_script = script_path
            elif re.search('analytics', script_name, re.IGNORECASE):
                self.analytics_script = script_path
            else:
                self.site_scripts.append(script_path)
