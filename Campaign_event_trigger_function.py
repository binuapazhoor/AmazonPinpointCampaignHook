import boto3
import datetime
import time
import json


client = boto3.client('pinpoint')

def lambda_handler(event, context):
    
    print(json.dumps(event))
    
    application_id = event['application_id']
    event_type = event['event_type']
    nextTestDate = event['nextTestDate']
    endpoint_id = event['event_type']
    FirstName = event['endpoint_id']
    email = event['email']
    userid = event['userid']

    response = client.put_events(
            ApplicationId = application_id,
            EventsRequest={
                'BatchItem': {
                    endpoint_id: {
                        'Endpoint': {
                            'Address': email,
                            'ChannelType': 'EMAIL',
                            'OptOut': 'NONE',
                            'Attributes': {
                                'FirstName': [
                                    FirstName,
                                    ],
                                'nextTestDate': [
                                    nextTestDate,
                                    ],
                                'nextTestTime': [
                                    '10:00'
                                    ],
                                'EventType': [event_type]
                            },
                            'User': {
                                "UserId": userid,
                                "UserAttributes" : {
                                    'FirstName' : [FirstName]
                                    }
                                }
                        },
                        'Events':{
                            'registration_success': {
                                'EventType': event_type,
                                'Timestamp': datetime.datetime.fromtimestamp(time.time()).isoformat()
                            }
                        }
                    }
                } 
            }
        )

    return response
