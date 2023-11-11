import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Specify the S3 bucket and object key
    bucket = 'sqs-s3s'
    object_key = 'your-prefix/SQS.json'

    try:
        # Read the content of the S3 object
        response = s3_client.get_object(Bucket=bucket, Key=object_key)
        content = response['Body'].read().decode('utf-8')

        # Print the content
        print("File content:")
        print(content)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File content printed successfully"
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
