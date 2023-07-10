import json

chinese = [
    {
        "eng":["you"],
        "nun":"ni3",
        "homoph":"",
        "cn":u"\u4f60 "
    },
    {
        "eng":["good", "well"],
        "nun":"hao3",
        "homoph":"",
        "cn":u"\u597d"
    },
    {
        "eng": ["hello", "hi"],
        "nun":"ni2hao3",
        "homoph":"",
        "cn":u"\u4f60\u597d"
    }
]

dumped = json.dumps(chinese, indent=4, sort_keys=True)

with open("chinese.json", "w") as outfile:
    outfile.write(dumped)
