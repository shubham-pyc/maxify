from maxify.assistants.campaign_assistant.campaign_assistant import CampaignAssistant
from maxify.services.exception_handler import ExceptionHander
from maxify.modals.user import User
from maxify.modals.campaign import CLICampaign
from maxify.modals.constants import DEBUG_FOLDER_PATH
import os
import pytest

user = User.getInstance()
handler = ExceptionHander()

@pytest.fixture(scope='function')
def _campagin(mocker,fs):
    fs.create_dir("/home")
    fs.create_dir("/home/impadmin")
    fs.create_dir("/home/impadmin/Desktop")
    return CLICampaign()


def test_campagin_assistant_create_folder(_campagin, mocker, fs):
    expected = [
        'QA - BookingPath_Default',
        'QA - BookingPath_Default/Requirement',
        'QA - BookingPath_Default/Source File',
        'QA - BookingPath_Default/Source File/campaign scripts',
        'QA - BookingPath_Default/Source File/.vscode',
        'QA - BookingPath_Default/Dev test suite',
        'QA - BookingPath_Default/Source File/variant script',
    ]
    expected = [ os.path.join(DEBUG_FOLDER_PATH,x) for x in expected]

    assistant = CampaignAssistant(_campagin, user, handler)
    assistant.setup_folder()
    for path in expected:
        assert os.path.exists(path) == True




def test2(fs):
    print(fs)
    # assert 2 == 3
