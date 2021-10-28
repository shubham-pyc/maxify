from .utils import get_element_id_and_variant_id_from_path, get_script_id_from_path, read_file, is_script_path
from .maximizer import MaximizerAssistant


from maxify.modals.user import User

creator = User.getInstance()


def update_variant(args):
    '''
        Function to update pertifular file on maxymiser
        :Param args: cli arguments
    '''
    configurations = read_file(args.config, as_json=True)
    assistant = MaximizerAssistant(configurations, creator)
    content = read_file(args.file)
    if is_script_path(args.file):
        script_id = get_script_id_from_path(args.file)
        assistant.update_campaign_script(script_id, content)
    else:
        element_id, variant_id = get_element_id_and_variant_id_from_path(
            args.file)
        assistant.update_variant_script(element_id, variant_id, content)


def get_maxymiser_json(args):
    '''
        Function to get campaign json object from maxymiser
        :Param args: cli arguments
        :Returns configurations: JSON object
    '''
    assistant = MaximizerAssistant(None, creator)
    configurations = assistant.get_campaign_json(args.name)
    return configurations
