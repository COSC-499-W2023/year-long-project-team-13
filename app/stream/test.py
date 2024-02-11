import boto3
from PIL import Image, ImageDraw, ImageFont

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

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
    draw = ImageDraw.Draw(image)

    line_width = 3
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

        draw.rectangle(((left, top), (width, height)),
                    outline='red', width=line_width)

        face_emotion_confidence = 0
        face_emotion = None
        for emotion in item.get('Emotions'):
            if emotion.get('Confidence') >= face_emotion_confidence:
                face_emotion_confidence = emotion['Confidence']
                face_emotion = emotion.get('Type')

        draw.text((left, top), face_emotion, 'white', font=font)

    return image

result_1 = detect_faces_and_emotions('./IMG_9958.jpg')
# save the result into a result.file

result_1.save('result_1.jpg')

