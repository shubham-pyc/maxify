
# OBJECTS RELATED TO ELIGIBILITY CRITERIA
'''
    IMPORTANT:

    To add new Critiera add code into this format
    Create A new directory with keys
    {
        "requirement":"Check for the obj ex: bootstrapper.dataOject.page.flightSearch"
        "call":"name of function to call ex: isSinglePax()",
        "code":"Acutal code of the function"
    }

    Finally map this object with the codition name into CRITERIA_CODE_MAPPING variable at the bottom of this file
'''


IS_SINGLE_PAX = {
    "requirement": "Bootstrapper.dataObject.page.flightSearch",
    "call": "isSinglePax()",
    "code": """// Validate for single Pax
function isSinglePax() {
    var flag = false;
    try {
        // Pax count already checked in Parent method "runVariant" 
        var paxCount = Bootstrapper.dataObject.page.flightSearch.paxCount;
        if (paxCount == 1) {
            flag = true;
        } else {
            DL_OBJ.EXCLUDE_REASON = "excludeIneligible|Pax count "+ paxCount;
        }
    } catch (e) {
        DL_OBJ.dataGapHandler(e,"isSinglePax");
    }
    return flag;
}
"""
}

IS_USER_LOGIN = {
    "requirement": "UA.AppData.Data.Session",
    "call": "isUserLogin()",
    "code": """//Function to check if the user is login
function isUserLogin(){
    var retValue = false;
    try{
        retValue = UA.AppData.Data.Session.IsSignedIn;
    } catch(e){
        DL_OBJ.dataGapHandler(e,"isUserLogin");
    }
    return retValue;
}

"""
}

'''
    Functions to Trip types
'''

IS_ROUND_TRIP = {
    "requirement": "UA.AppData.Data.Search",
    "call": "isTripTypeRoundTrip()",
    "code": """//Function to check if round trip selected
function isTripTypeRoundTrip() {
    var flag = false;
    try {
        var tripType = UA.AppData.Data.Search.SearchMethod;
        if (tripType == 'roundTrip') {
            flag = true;
        } else {
            DL_OBJ.EXCLUDE_REASON = "excludeIneligible|search type "+ tripType;
        }
    } catch (e) {
        DL_OBJ.dataGapHandler(e,"isTripTypeRoundTrip");
    }
    return flag;
}

"""
}

IS_TRIP_ONE_WAY = {
    "requirement": "UA.AppData.Data.Search",
    "call": "isTripTypeOneWay()",
    "code": """//Function to check if oneWay trip selected
function isTripTypeOneWay() {
    var flag = false;
    try {
        var tripType = UA.AppData.Data.Search.SearchMethod;
        if (tripType == 'oneWay') {
            flag = true;
        } else {
            DL_OBJ.EXCLUDE_REASON = "excludeIneligible|search type "+ tripType;
        }
    } catch (e) {
        DL_OBJ.dataGapHandler(e,"isTripTypeOneWay");
    }
    return flag;
}

"""
}

IS_DOMESTIC_SEARCH = {
    "requirement": "UA.AppData.Data.Search",
    "call": "isDomestic()",
    "code": """function isDomesticSearch() {
    var isDomestic = false,
        countryType = '';
    try {
        // countryType = (UA.AppData.Data.Search.SearchMethod == 'multiCity') ? "Domestic" : getMarketType();
       
        countryType = (UA.AppData.Data.Search.SearchMethod == 'multiCity') ? false : getMarketType();

        if (countryType == "Domestic") {
            isDomestic = true;
        } else {
            var label = "excludeIneligible|International search";
            window.ga(DL_OBJ.GA_METHOD, DL_OBJ.GA_EVENT, DL_OBJ.GA_CATEGORY,  DL_OBJ.CAMPAIGN_NAME, label);
        }
    } catch (e) {
        DL_OBJ.dataGapHandler(e,"isDomestic");
    }
    return isDomestic;
}

function getMarketType(){
    var marketType = "--";
    var methodName = "getMarketType";
    try{        
        var tripObject = (Bootstrapper.dataObject.getData("Trips", "srchRslts", "page") && Bootstrapper.dataObject.getData("Trips", "srchRslts", "page").length) ? Bootstrapper.dataObject.getData("Trips", "srchRslts", "page")[0] : "";
        if(tripObject){
            marketType = Bootstrapper.processMarketTypeValue(tripObject);
        }
    } catch (e) {
        DL_OBJ.dataGapHandler(e,"getMarketType");
    }
    return marketType;
}

"""
}


CRITERIA_CODE_MAPPING = {
    "roundtrip": IS_ROUND_TRIP,
    "oneway": IS_TRIP_ONE_WAY,
    "singlepax": IS_SINGLE_PAX,
    "userlogin": IS_USER_LOGIN,
    "domesticflight": IS_DOMESTIC_SEARCH
}
