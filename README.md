# Capstone-Project-2
<h1>Social Media Hashtag Trend Analyzer Application<br/></h1>

**Problem Statement:** <br/> In the era of social media dominance, users crave platforms that offer seamless posting experiences while also providing insights into trending topics. To address this need, we aim to develop a Streamlit application that allows users to compose and publish posts, same as popular social media platforms. This application will integrate with AWS Lambda and DynamoDB to facilitate post processing and hashtag analysis.<br/>

**Technologies Used:** <br/> Python, AWS Lambda, Dynamodb, Streamlit.<br/>

**Project Workflow:** <br/>The project involves developing a Streamlit application that allows users to create and publish posts with hashtags, integrates AWS Lambda for processing and storing data in DynamoDB, and includes real-time analysis of trending hashtags. The application should update the trending hashtags dynamically as and when the new posts are submitted. 

**Task performed to complete the project:** <br/> **1. Set up the Streamlit Application** - Install required python libraries and configure AWS for the project.
Create the user interface to allow users to compose posts with text and hashtags.<br/>
**2. AWS Lambda Integration** - Set up AWS Lambda functions to handle the processing of posts submitted through Streamlit.
Configure the Lambda function to interact with DynamoDB for storing post data. <br/>
**3. DynamoDB Setup** - Create a DynamoDB table to store posts and associated hashtags.
Ensure the table structure supports efficient querying of trending hashtags. <br/>
**4. Post Data Handling** - Implement functionality in the Lambda function to receive posts from Streamlit and store them in DynamoDB using the PutItem operation. <br/>
**5. Trending Hashtags Analysis** - Develop logic to analyze the DynamoDB table to identify trending hashtags.
Implement real-time updates of trending hashtags in the Streamlit app as new posts are submitted. <br/>

**hastag.py** - This file contains code that stores post details, integrates AWS Lambda for data processing and storage in DynamoDB, and uses Streamlit to display trending hashtags.
