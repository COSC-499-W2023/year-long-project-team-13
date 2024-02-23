import boto3
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Let's use Amazon S3
s3 = boto3.resource('s3')

# s3.Bucket('elasticbeanstalk-ca-central-1-841071745826').download_file('mountain.jpg', 'mountain.jpg')
s3.Bucket('elasticbeanstalk-ca-central-1-841071745826').upload_file('IMG_9958.jpg', 'IMG_9958.jpg')

rekognition = boto3.client('rekognition')
font = ImageFont.truetype('arial.ttf', 30)

def detect_faces_and_emotions(image_name: str):
    with open(image_name, 'rb') as image_data:
        response_content = image_data.read()

    rekognition_response = rekognition.detect_faces(
        Image={'Bytes': response_content}, Attributes=['ALL'])

    print(rekognition_response)

    image = Image.open(image_name)
    image_width, image_height = image.size

    for item in rekognition_response.get('FaceDetails'):
        bounding_box = item['BoundingBox']
        width = image_width * bounding_box['Width']
        height = image_height * bounding_box['Height']
        left = image_width * bounding_box['Left']
        top = image_height * bounding_box['Top']

        left = int(left)
        top = int(top)
        width = int(width) + left
        height = int(height) + top

        mask = Image.new('L',image.size)
        draw = ImageDraw.Draw(mask)

        draw.ellipse(((left, top), (width, height)),fill=255)

        blurred = image.filter(ImageFilter.GaussianBlur(radius=50))

        comp = Image.composite(blurred, image, mask)
        comp.save(image_name.split('.')[0] + '_blurred_1.jpg')

detect_faces_and_emotions('IMG_9958.jpg')
