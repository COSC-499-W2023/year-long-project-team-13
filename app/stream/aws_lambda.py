import boto3
import os

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key_name = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key_name
            }
        },
        Attributes=['DEFAULT']
    )
    image = {
        'S3Object': {
            'Bucket': bucket_name,
            'Name': key_name
        }
    }
    # Get image dimensions
    image_info = s3.head_object(Bucket=bucket_name, Key=key_name)
    width = image_info['Metadata']['width']
    height = image_info['Metadata']['height']
    # Blur faces
    for face in response['FaceDetails']:
        box = face['BoundingBox']
        left = int(box['Left'] * width)
        top = int(box['Top'] * height)
        w = int(box['Width'] * width)
        h = int(box['Height'] * height)
        # Blur face
        command = f"convert -gravity center -crop {w}x{h}+{left}+{top} \
                   -blur 0x8 -resize {w}x{h}! -gravity center \
                   -extent {w}x{h} {key_name} {key_name}"
        os.system(command)
    # Save image back to S3
    s3.upload_file(key_name, bucket_name, key_name)
    return {
        'statusCode': 200,
        'body': 'Faces blurred successfully.'
    }
