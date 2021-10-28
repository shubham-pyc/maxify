from maxify.assistants.campaign_assistant import utils


def test_make_abreviation(mocker):
    result = utils.make_abbreviation("new_some_plan",booking_path=False)
    assert result == "NewSomPla"
    result = utils.make_abbreviation("new_some_plan")
    assert result == "BkPthNewSomPla"

def test_merge_conditions():
    args = [
        "UA.Booking.FlightSearch.currentResults.Flights",
        "UA.Booking.FlightSearch.currentResults",
        "UA.Confirmation",
        "UA.Confirmation.Cart",
        "UA.Booking.Confirmation"
    ]
    result = utils.merge_conditions(args)
    expected = " && UA.Booking && UA.Booking.FlightSearch && UA.Booking.FlightSearch.currentResults && UA.Booking.FlightSearch.currentResults.Flights && UA.Confirmation && UA.Confirmation.Cart && UA.Booking.Confirmation" 

    assert result == expected 