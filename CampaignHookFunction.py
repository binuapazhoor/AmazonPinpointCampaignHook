import json

def lambda_handler(event, context):
    
    # TODO implement
    print (json.dumps(event))
    endpoints = event['Endpoints']

    newField = []
    newField.append("Amazon")
    print(json.dumps(endpoints))
    endpointAttributes= []
    for id,endpoint in endpoints.items():
        print(id)
        Attributes = endpoint['Attributes']
        Attributes["CampaignHookField1"] = newField
        print(Attributes)
        print(endpoint['Attributes'])
    
    print(json.dumps(endpoints))

    return endpoints
