def json(data):
    json_naive = {
        "<start>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"'],
    }

    json_basic = {
        "<start>":
            ["<type>"],
        "<type>":
            ["<basic_dict>", "<basic_list>", "<basic_string>", "<basic_number>", "null", "<boolean>"],
        "<basic_dict>":
            ["{<elements>}"],
        "<elements>":
            ["<element>", "<element>, <elements>"],
        "<element>":
            ["<id>: <value>"],
        "<basic_list>":
            ["[<values>]"],
        "<values>":
            ["<value>", "<value>, <values>"],
        "<basic_string>":
            ["<value>"],
        "<basic_number>":
            ["<integer>", "<float>"],
        "<integer>":
            ["RANDOM_INT"],
        "<float>":
            ["<integer>.<integer>"],
        "<boolean>":
            ["true", "false"],
        "<value>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"'],
        "<id>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"'],
    }
    json_complex = {
        "<start>":
            ["<type>"],
        "<type>":
            ["<basic_dict>",  "<basic_list>"],
        "<basic_dict>":
            ["{<elements>}"],
        "<elements>":
            ["<element>", "<element>, <elements>"],
        "<element>":
            ["<id>: <value>"],
        "<value>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"', "<basic_dict>", "<basic_list>"],
        "<id>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"', "<basic_dict>"],
        "<basic_list>":
            ["[<values>]"],
        "<values>":
            ["<value_list>", "<value_list>, <values>"],
        "<value_list>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"', "<basic_list>"],
    }

    json_param_specific = {
        "<start>":
            ["<type>"],
        "<type>":
            ["<basic_dict>"],
        "<basic_dict>":
            ["{<elements>}"],
        "<elements>":
            ["<element>", "<element>, <elements>"],
        "<element>":
            ["\"<param_id>\" : <value>"],
        "<value>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"', "<basic_dict>", "<basic_list>"],
        "<param_id>":
            ["id", "gopSignaling", "name", "brand", "gopDuration", "inputId", "duration", "recorderPreset", "type",
             "serviceId", "accessUrl", "playlist"],
        "<basic_list>":
            ["[<values>]"],
        "<values>":
            ["<value_list>", "<value_list>, <values>"],
        "<value_list>":
            ['"' + "RANDOM_GRAMMAR_STRING" + '"', "<basic_list>"],
    }

    if data == "json_naive":
        return json_naive
    elif data == "json_basic":
        return json_basic
    elif data == "json_complex":
        return json_complex
    else:
        return json_param_specific
