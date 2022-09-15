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
        # Here is where you can add custom code to add dynamic attributes to an endpoint: 
        # Call a webservice, look up a value from a database, 
        # Call a CRM API to retrieve an offer for this endpoint. 
        # You can also remove endpoints to filter them out of the campaign.
        Attributes["CampaignHookField1"] = newField
        print(Attributes)
        print(endpoint['Attributes'])
    
    print(json.dumps(endpoints))

    return endpoints
