import boto3
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InventoryTable')

sns = boto3.client('sns')
topic_arn = "arn:aws:sns:us-east-1:708716444370:low-stock-topic"

def lambda_handler(event, context):
    # Get bucket and file info from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Received file: {key} from bucket: {bucket}")

    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8').splitlines()
    print("File content read successfully.")

    # Read CSV
    reader = csv.DictReader(file_content)

    for row in reader:
        item_id = row['itemId']
        name = row['name']
        quantity = int(row['quantity'])

        # Insert into DynamoDB
        table.put_item(
            Item={
                'itemId': item_id,
                'name': name,
                'quantity': quantity
            }
        )

        print(f"Inserted item: {{'itemId': '{item_id}', 'name': '{name}', 'quantity': {quantity}}}")

        # Check low stock
        if quantity < 3:
            message = f"Low inventory alert for item {name}! (ID: {item_id}) - Quantity left: {quantity}"
            sns.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject="Low Inventory Alert"
            )
            print(f"Low stock alert sent for item {item_id}")

    return {
        'statusCode': 200,
        'body': 'Inventory processed successfully.'
    }