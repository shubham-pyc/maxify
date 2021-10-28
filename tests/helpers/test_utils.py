from maxify.helpers import utils

def test_get_platform_for_mac(mocker):
    mocker.patch('maxify.helpers.utils.get_system_platform',return_value="darwin")
    assert utils.get_platform() == "mac"

def test_get_platform_for_linux(mocker):
    mocker.patch('maxify.helpers.utils.get_system_platform',return_value="unix")
    assert utils.get_platform() == "linux"

def test_get_platform_for_windows(mocker):
    mocker.patch('maxify.helpers.utils.get_system_platform',return_value="windows")
    assert utils.get_platform() == "windows"