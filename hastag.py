import streamlit as st
import boto3
import uuid
import json

# AWS Configuration
aws_lambda = boto3.client('lambda', region_name='eu-north-1')
dynamodb = boto3.client('dynamodb', region_name='eu-north-1')

# Streamlit app
st.title("Post Composer")

post_text = st.text_area("Write your post here")
hashtags = st.text_input("Enter hashtags separated by commas")

if st.button("Publish"):
    if post_text and hashtags:
        post_id = str(uuid.uuid4())
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
        st.error("Please enter both text and hashtags")

# Display trending hashtags
st.title("Trending Hashtags")
response = dynamodb.scan(TableName='Posts')
items = response['Items']

hashtags_count = {}
for item in items:
    hashtags_list = item['Hashtags']['S'].split(',')
    for hashtag in hashtags_list:
        if hashtag not in hashtags_count:
            hashtags_count[hashtag] = 1
        else:
            hashtags_count[hashtag] += 1

sorted_hashtags = sorted(hashtags_count.items(), key=lambda x: x[1], reverse=True)

for hashtag, count in sorted_hashtags[:10]:
    st.write(f"{hashtag}: {count} posts")
