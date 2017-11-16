import boto3


def lambda_handler(request, context):
    rekognition = boto3.client('rekognition')

    if 'bucket' in request:
        bucket = request['bucket']
    else:
        raise Exception('Bucket name not provided!')

    if 'key' in request:
        key = request['key']
    else:
        raise Exception('Key not provided!')

    try:
        return rekognition.detect_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    except Exception as e:
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
