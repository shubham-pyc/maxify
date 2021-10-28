from maxify.modals.campaign import MaxymiserCampaign
from .campaign_assistant import CampaignAssistant
from maxify.services.exception_handler import ExceptionHander
from maxify.modals.user import User

user = User.getInstance()
exception_hander = ExceptionHander()

def creator(config):
    campaign = MaxymiserCampaign(configuration=config)
    campaign_assistant = CampaignAssistant(
        campaign, user, exception_hander)
    campaign.folder_path = campaign_assistant.assist()
