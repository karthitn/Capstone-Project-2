import streamlit as st
import boto3
import uuid
import json

# AWS Configuration
aws_lambda = boto3.client('lambda', region_name='eu-north-1')
dynamodb = boto3.client('dynamodb', region_name='eu-north-1')

#Presentation
st.title(":blue[Social Media Hashtag Trend Analyzer Application]")
st.header(":rainbow[Problem Statement]")
st.markdown("In the era of social media dominance, users crave platforms that offer seamless posting experiences while also providing insights into trending topics. To address this need, we aim to develop a Streamlit application that allows users to compose and publish posts, same as popular social media platforms. This application will integrate with AWS Lambda and DynamoDB to facilitate post processing and hashtag analysis.")    
st.subheader(":orange[Technologies Used:]")
st.markdown("Python, AWS Lambda, Dynamodb, Streamlit")    
st.subheader(":orange[Project Workflow:]")
st.markdown("The project involves developing a Streamlit application that allows users to create and publish posts with hashtags, integrates AWS Lambda for processing and storing data in DynamoDB, and includes real-time analysis of trending hashtags. The application should update the trending hashtags dynamically as new posts are submitted.")   
st.subheader(":orange[Task performed to complete the project:]")
st.markdown("""
- **:green[Set up the Streamlit Application]** - Install required python libraries and configure AWS for the project.Create the user interface to allow users to compose posts with text and hashtags.
- **:green[AWS Lambda Integration]** - Set up AWS Lambda functions to handle the processing of posts submitted through Streamlit.
Configure the Lambda function to interact with DynamoDB for storing post data.
- **:green[DynamoDB Setup]** - Create a DynamoDB table to store posts and associated hashtags.
Ensure the table structure supports efficient querying of trending hashtags.
- **:green[Post Data Handling]** - Implement functionality in the Lambda function to receive posts from Streamlit and store them in DynamoDB using the PutItem operation.
- **:green[Trending Hashtags Analysis]** - Develop logic to analyze the DynamoDB table to identify trending hashtags.
Implement real-time updates of trending hashtags in the Streamlit app as and when new posts are submitted.                                               
""")   

# Streamlit app
# Extract hashtags from the text content
def extract_hashtags(post_text):
    return re.findall(r'#\w+', post_text)

st.title(":blue[Compose and Publish Post]")

# Single text area for both text content and hashtags
post_text = st.text_area(":violet[Compose your post]",placeholder="Write your post and include #hashtags")

if st.button("Publish"):
    if post_text:
        post_id = str(uuid.uuid4())
        hashtags = extract_hashtags(post_text)
        response = aws_lambda.invoke(
            FunctionName='hastag',
            InvocationType='RequestResponse',
            Payload=json.dumps({
                'PostID': post_id,
                'Text': post_text,
                'Hashtags': hashtags
            })
        )
        st.success("Post published successfully!")
    else:
        st.error("Please enter text with hashtags")

# Display trending hashtags
st.title(":blue[Trending Hashtags]")
response = dynamodb.scan(TableName='Posts')
items = response['Items']

hashtags_count = {}
for item in items:
    hashtags_list = item['Hashtags']['S']
    for hashtag in json.loads(hashtags_list):
        if hashtag not in hashtags_count:
            hashtags_count[hashtag] = 1
        else:
            hashtags_count[hashtag] += 1

sorted_hashtags = sorted(hashtags_count.items(), key=lambda x: x[1], reverse=True)

for hashtag, count in sorted_hashtags[:10]:
    st.write(f"{hashtag}: {count} posts")
