import boto3

# Initialize Boto3 client for Amazon Rekognition
rekognition_client = boto3.client('rekognition', region_name='ca-central-1')  # Replace with your desired region

def analyze_video(video_s3_bucket, video_s3_key):
    try:
        # Start label detection for the video
        response = rekognition_client.start_label_detection(
            Video={
                'S3Object': {
                    'Bucket': video_s3_bucket,
                    'Name': video_s3_key
                }
            },
            MinConfidence=50,  # Adjust confidence threshold as needed
        )

        job_id = response['JobId']
        print(f"Video analysis started. JobId: {job_id}")

        # Wait for label detection completion
        rekognition_client.get_waiter('label_detection_completed').wait(JobId=job_id)

        # Get label detection results
        result = rekognition_client.get_label_detection(JobId=job_id)
        labels = result['Labels']

        print("Detected labels:")
        for label in labels:
            print(f"Label: {label['Label']['Name']} (Confidence: {label['Label']['Confidence']:.2f})")

        # Now let's detect faces in the video
        response_faces = rekognition_client.start_face_detection(
            Video={
                'S3Object': {
                    'Bucket': video_s3_bucket,
                    'Name': video_s3_key
                }
            },
            FaceAttributes='ALL',  # Retrieve all face attributes
        )

        job_id_faces = response_faces['JobId']
        print(f"Face detection started. JobId: {job_id_faces}")

        # Wait for face detection completion
        rekognition_client.get_waiter('face_detection_completed').wait(JobId=job_id_faces)

        # Get face detection results
        result_faces = rekognition_client.get_face_detection(JobId=job_id_faces)
        faces = result_faces['Faces']

        print("Detected faces:")
        for face in faces:
            print(f"Face ID: {face['Face']['FaceId']}")

        # Finally, extract text from the video
        response_text = rekognition_client.start_text_detection(
            Video={
                'S3Object': {
                    'Bucket': video_s3_bucket,
                    'Name': video_s3_key
                }
            }
        )

        job_id_text = response_text['JobId']
        print(f"Text detection started. JobId: {job_id_text}")

        # Wait for text detection completion
        rekognition_client.get_waiter('text_detection_completed').wait(JobId=job_id_text)

        # Get text detection results
        result_text = rekognition_client.get_text_detection(JobId=job_id_text)
        text_detections = result_text['TextDetections']

        print("Detected text:")
        for text in text_detections:
            print(f"Text: {text['DetectedText']} (Confidence: {text['Confidence']:.2f})")

    except Exception as e:
        print(f"Error analyzing video: {str(e)}")

if __name__ == "__main__":
    video_bucket_name = 'elasticbeanstalk-ca-central-1-841071745826'
    video_object_key = 'girl_-_45132 (1080p).mp4'

    analyze_video(video_bucket_name, video_object_key)
