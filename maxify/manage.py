import sys
from maxify.modals.campaign import CLICampaign
from maxify.modals.user import User
from maxify.assistants.campaign_assistant.campaign_assistant import CampaignAssistant
from maxify.assistants.campaign_assistant.cli import get_arguments
from maxify.assistants.campaign_assistant.main import creator
from maxify.assistants.maxymise_assistant.maximizer import MaximizerAssistant
from maxify.assistants.maxymise_assistant.main import update_variant as updater, get_maxymiser_json
from maxify.assistants.maxymise_assistant.utils import read_file
from maxify.services.exception_handler import ExceptionHander


def main():
    try:
        exception_hander = ExceptionHander()
        arguments = get_arguments()
        user = User.getInstance()

        if arguments.type == "create":
            campaign_name = arguments.name
            variants = arguments.variants
            debug = arguments.debug
            conditions = arguments.conditions
            booking_path = arguments.bookingpath
            campaign = CLICampaign(name=campaign_name, conditions=conditions,
                                   variants=variants, is_booking_path=booking_path)

            campaign_assistant = CampaignAssistant(
                campaign, user, exception_hander)
            campaign.folder_path = campaign_assistant.assist()

        elif arguments.type == "clone":
            config = get_maxymiser_json(arguments)
            creator(config)

        elif arguments.type == "update":
            updater(arguments)

    except Exception as e:
        exception_hander.handle_exception(e)
