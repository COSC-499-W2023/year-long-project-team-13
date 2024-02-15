import boto3

rekognition_client = boto3.client('rekognition', region_name='ca-central-1')  # Replace with your desired region

def analyze_video(video_s3_bucket, video_s3_key):
    try:
        response = rekognition_client.start_label_detection(
            Video={
                'S3Object': {
                    'Bucket': video_s3_bucket,
                    'Name': video_s3_key
                }
            },
            NotificationChannel={
                'SNSTopicArn': 'arn:aws:sns:ca-central-1:841071745826:video-analysis-completion',
                'RoleArn': 'arn:aws:iam::841071745826:role/service-role/rekognitionRole'  # Replace with your IAM role ARN
            }
        )

        job_id = response['JobId']
        print(f"Video analysis started. JobId: {job_id}")

        rekognition_client.get_waiter('label_detection_completed').wait(JobId=job_id)

        result = rekognition_client.get_label_detection(JobId=job_id)
        labels = result['Labels']

        for label in labels:
            print(f"Label: {label['Label']['Name']} (Confidence: {label['Label']['Confidence']:.2f})")

    except Exception as e:
        print(f"Error analyzing video: {str(e)}")

if __name__ == "__main__":
    video_bucket_name = 'elasticbeanstalk-ca-central-1-841071745826'
    video_object_key = 'girl_-_45132 (1080p).mp4'

    analyze_video(video_bucket_name, video_object_key)
