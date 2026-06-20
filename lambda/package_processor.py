import json
import boto3

dynamodb = boto3.resource('dynamodb')
polly = boto3.client('polly')
s3 = boto3.client('s3')
sns = boto3.client('sns')

TABLE_NAME = 'PackageTracking'
BUCKET_NAME = 'smart-logistics-storage'

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:060255765613:PackageStatusAlerts'

def lambda_handler(event, context):

    tracking_id = "PKG1001"

    table = dynamodb.Table(TABLE_NAME)

    response = table.get_item(
        Key={
            'TrackingID': tracking_id
        }
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'body': 'Package not found'
        }

    message = f"Package {tracking_id} for {item['CustomerName']} has arrived at {item['Destination']}"

    audio = polly.synthesize_speech(
        Text=message,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"audio-alerts/{tracking_id}.mp3",
        Body=audio['AudioStream'].read(),
        ContentType='audio/mpeg'
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject='Package Arrival Alert',
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
