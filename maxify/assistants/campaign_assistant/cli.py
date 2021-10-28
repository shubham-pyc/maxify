import argparse
from .lib import criteria


def str_to_bool(string):
    if string.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif string.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="type")

    parser_create = subparsers.add_parser('create', help="create help")

    parser_create.add_argument(
        '-variants', type=int, help="Number of variants for the campaign", default=1)
    parser_create.add_argument(
        '-name', type=str, required=True, help="Name of the campaign")
    parser_create.add_argument('-bookingpath', type=str_to_bool,
                               help="Removes BookingPath_ from files", default=True)
    parser_create.add_argument(
        '-debug', type=bool, help="flag for testing purposes", default=False)
    parser_create.add_argument('-conditions', type=str, nargs="+", default=None,
                               help="[ {} ]".format(" , ".join(criteria.CRITERIA_CODE_MAPPING)))

    parser_update = subparsers.add_parser('update', help="update help")

    parser_update.add_argument('-config', type=str, help="maxymiser.json path")
    parser_update.add_argument('-file', type=str, help="file to update")


    parser_clone = subparsers.add_parser('clone', help="clone help")
    parser_clone.add_argument('-name', type=str, help="Name of the campaign to clone")

    arguments = parser.parse_args()
    return arguments
