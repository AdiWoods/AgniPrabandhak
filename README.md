# AgniPrabandhak

Video Demo: https://youtu.be/7otW8a-T-_E

## Description:
We participated in the NASA International Space Apps Challenge, selecting the challenge "Fire Management: Increasing Community-based Fire Management Opportunities." In just 48 hours, we developed "AgniPrabandhak," a powerful tool designed as our solution to this challenge. "Agni Prabandhak" serves as a tool for local community members to tackle the problem of forest fires. It offers the capability for individuals in these local communities to report fires including those of the smallest scale and size, which may not be detected by NASA satellites. This ground-level community-based reporting system plays a crucial role in enhancing the comprehensive monitoring of forest fire incidents. Our tool empowers community members by combining two essential features. Users can not only report forest fires but they can also proactively protect their areas of interest. By setting forest fire alerts, individuals receive timely notifications if a fire occurs in their chosen areas.

## What We've Built:
We've built a web application that enables individuals to report fire by uploading images of fire incidents, and these images undergo validation using our specialized "forest_fire" machine learning model. Users can not only report fires but also proactively safeguard their specified areas of interest. Through the establishment of forest fire alerts, individuals receive timely notifications via SMS to their mobile devices in the event of a fire occurring within their designated areas.

## How It Helps:
Our solutions help to tackle the problems in the following ways: 
* Collecting and Distributing Fire Information from Local Communities: It enables individuals to swiftly report fires, including those of smaller scales not readily detectable by satellites. This ground-level reporting complements satellite data, providing a comprehensive view of fire incidents.
* Validating and Managing Volunteer-Collected Image Data: The system employs a rigorous validation process for image data submitted by volunteers. This validation ensures the accuracy and reliability of reported fire incidents.
* Validating and Confirming Satellite Fire Detection on the Ground: In conjunction with satellite-based fire detection, our system serves as a confirmation mechanism from the ground. It verifies the presence of fires detected by satellites, reducing false alarms and increasing the reliability of fire alerts.

## How Does It Work:
* Upon opening the web application, users are presented with two options: 1] Report a Fire, 2] Set Fire Alert
* The user chooses between these options based on their intended actions.
* Reporting a Fire: When a user selects the "Report Fire" option, they are directed to a dedicated screen. Here, users can submit a forest fire report by uploading an image of the detected fire. The system employs a "Forest_Fire" machine-learning model to validate the image uploaded by the user. This model verifies whether the image depicts a forest fire or not. If the image does not portray a fire, a prompt message is displayed: "Fire not detected. Please upload a valid image." Furthermore, the data associated with the images is stored in our database. This dataset includes crucial information such as Longitude, Latitude, the user-uploaded Image, Date, and Time of the report. This rich dataset serves multiple purposes, including confirming satellite-detected fires. By cross-referencing with satellite data, we enhance the accuracy of fire alerts and reduce false alarms, establishing a vital ground-level validation mechanism. Additionally, we recognize the value of this data beyond our immediate needs. Therefore, it has the potential to be made accessible to the public, offering various use cases and opportunities for research, analysis, and community engagement.
* Setting a Fire Alert: Selecting "Set Fire Alert" directs users to a distinct screen. Here, users are prompted to give their contact phone number and designate the specific area for which they desire to receive fire alerts. In the event of a forest fire breaking out in the chosen area, users are promptly notified via SMS on their mobile devices. Our fire detection process leverages the NASA FIRMS API, ensuring the timely identification of fires. This data is meticulously cross-referenced and validated using the information collected from users who report fire incidents via our "Report Fire" feature, enhancing the precision of fire alerts. The seamless delivery of SMS notifications to users is facilitated through the integration of the Twilio API, ensuring swift communication during critical situations.

## Tools That We Have Used:
* We have used languages like Python, CSS, HTML and Javascript
* To build the machine learning model we have used the Python Language and various machine learning libraries like Pandas, NumPy, and TensorFlow and we have used the CNN model with various layers like the Dense layer, Conv2D layer, MaxPooling2D layer, Flatten layer, Dropout layer, SeprableConv2D layer and BatchNormalization layer.
* To collect the data for training the machine learning we have used BeautifulSoup Library.
* For the backend, we have used Django Framework.
* For making the Frontend we have used HTML, CSS, Bootstrap and Javascript.
* We have used NASA FIRMS APIs for collecting the data of fire active locations that we used to give alerts to the user.
