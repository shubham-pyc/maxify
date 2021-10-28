'''
    File containing boilerplate code for the files
'''


COMMON_CODE = """mmcore._$replace = {
    CAMPAIGN_NAME: "$campaign",
    VIRTUALPAGE: "D2.0 - - Stage",
    INCLUDE: false,
    CAMPAIGNREQUESTED: false,
    GA_METHOD: "send",
    GA_EVENT: "event",
    GA_CATEGORY: "Maxymiser PC",
    GA_EXCEPTION_CATEGORY: "DataGapTracking",
    GA_EXCEPTION_ACTION: "WebOptimization",
    EXCLUDE_REASON: ''
};

// Adding Datagap Handler Obj
mmcore._$replace.dataGapHandler = function(message, method_name, additional_info) {
    var dateObj = new Date(),
        current_timestamp = dateObj.getTime(),
        customLabel = {
            "campaign": mmcore._$replace.CAMPAIGN_NAME,
            "message": message,
            "method_name": method_name,
            "additional_info": additional_info,
            "time_stamp": current_timestamp
        };
    window.ga(mmcore._$replace.GA_METHOD, mmcore._$replace.GA_EVENT, mmcore._$replace.GA_EXCEPTION_CATEGORY, mmcore._$replace.GA_EXCEPTION_ACTION, JSON.stringify(customLabel));
};
"""


QUALIFICATION_CODE = """if (mmcore && mmcore.DO) {
    mmcore._$replace = mmcore.DO.getCampaignSettings("$campaign","D2.0 - - Stage");
    var DL_OBJ = mmcore._$replace

    function requestCampagin() {
        try {
            if ($functioncall) {
                DL_OBJ.INCLUDE = true;
            } else {
                DL_OBJ.EXCLUDE_REASON = 'excludeinelegible| Message';
            }
            visitor.setAttr("Customer", "" + DL_OBJ.INCLUDE);
            if (!DL_OBJ.CAMPAIGNREQUESTED) {
                renderer.getContent(DL_OBJ.VIRTUALPAGE).done(function () {
                    renderer.runVariantJs();
                });
                DL_OBJ.CAMPAIGNREQUESTED = true;
            }
        } catch (e) {
            DL_OBJ.dataGapHandler(e,"requestCampagin");
        }
    }

    // self-executable function which trigger the campaign
    (function triggerCampaign() {
        var passChecks = true;
        try {

            if (window.$ && typeof (window.$) === "function" && UA $condition) {
                requestCampagin();
                DL_OBJ.sendEligibilityStatus();

            } else {
                passChecks = false;
            }

            /* if did not pass checks, then recall function to check again after a specified time period */
            if (!passChecks) {
                setTimeout(triggerCampaign, 10);
            }
        } catch (e) {
            // statements
            DL_OBJ.dataGapHandler(e,"triggerCampaign");
        }
    })();
}
"""

VARIANT_CODE = """<script>
    
    var DL_OBJ = mmcore._$replace;
    
        function runVariant() {
            try {
                            
            } catch (e) {
                DL_OBJ.dataGapHandler(e,"runVariant");
            }
        }
        runVariant();
    
</script>
"""

ANALYTICS_CODE = """if (mmcore && mmcore.DO) {
    var DL_OBJ = mmcore._$replace;

    (function runScript() {
        var passChecks = true;
        try {

            if (window.$ && typeof (window.$) === "function" && window.ga && typeof (window.ga) === "function" && mmcore) {
                applyClickListeners();
                
            } else {
                passChecks = false;
            }

            /* if did not pass checks, then recall function to check again after a specified time period */
            if (!passChecks) {
                setTimeout(runScript, 10);
            }
        } catch (e) {
            DL_OBJ.dataGapHandler(e,"runScript");
        }
    })();


    function applyClickListeners() {
        var classLabelMapping = {
            "query":"label"
        };
        try {
            for (var query in classLabelMapping) {
                (function (cssQuery, currentLabel) {
                    $(document).on('click', cssQuery,function () {
                        try {
                            var label = currentLabel;
                            window.ga(DL_OBJ.GA_METHOD, DL_OBJ.GA_EVENT, DL_OBJ.GA_CATEGORY, DL_OBJ.CAMPAIGN_NAME, label);
                        } catch (e) {
                            DL_OBJ.dataGapHandler(e,"applyClickListeners");
                        }
                    })
                })(query, classLabelMapping[query]);
            }
        } catch (e) {
            DL_OBJ.dataGapHandler(e,"applyClickListeners");
        }
    }
}
"""


TASK_CODE = """{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "push",
            "type": "shell",
            "command": "maxify",
            "args": [
                // Ask msbuild to generate full paths for file names.
                "update",
                "-c",
                "${workspaceFolder}/maxymiser.json",
                "-f",
                "${fileDirname}/${fileBasename}"
            ],
            "group": "build",
            "presentation": {
                // Reveal the output only if unrecognized errors occur.
                "reveal": "silent"
            },
            // Use the standard MS compiler pattern to detect errors, warnings and infos
            "problemMatcher": "$msCompile"
        }
    ]
}
"""