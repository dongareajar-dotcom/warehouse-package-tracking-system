# 📦 AWS Serverless Warehouse Package Tracking & Notification System

## Project Overview

This project demonstrates a fully serverless package tracking and warehouse notification system built on AWS.

Package information is stored in Amazon DynamoDB. When a package is processed, AWS Lambda is automatically triggered to retrieve package details, generate voice announcements using Amazon Polly, store audio files in Amazon S3, publish events through Amazon EventBridge, and send email notifications using Amazon SNS.

Amazon API Gateway provides REST APIs for package registration and package tracking.

---

# Architecture Diagram

<img width="1408" height="768" alt="arc" src="https://github.com/user-attachments/assets/1c2a3b99-9093-4739-a1f2-4c4e5c302d2b" />


---

# Architecture Workflow

1. User registers a package through API Gateway.
2. Package information is stored in DynamoDB.
3. Package processing triggers AWS Lambda.
4. Lambda retrieves package details from DynamoDB.
5. Amazon Polly generates voice announcements.
6. Generated audio files are stored in Amazon S3.
7. EventBridge publishes package status events.
8. Amazon SNS sends email notifications.
9. Users can track package status through API Gateway APIs.

---

# AWS Services Used

* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* Amazon Polly
* Amazon S3
* Amazon EventBridge
* Amazon SNS
* AWS IAM

---

# API Details

### Register Package API

**Method:** POST

**Endpoint:**

```text
https://c4jd7eoes1.execute-api.ap-south-1.amazonaws.com/register-package
```

### Sample Request

```json
{
  "packageId": "PKG1001",
  "customerName": "Rahul Sharma",
  "email": "rahul@example.com",
  "status": "Received"
}
```

### Sample Response

```json
{
  "message": "Package registered successfully"
}
```

---

# Screenshots

## DynamoDB Table

<img width="1042" height="682" alt="Screenshot 2026-06-20 123115" src="https://github.com/user-attachments/assets/e5e04636-82db-412c-ab6e-6d7046382a1e" />


---

## Lambda Function

<img width="1230" height="705" alt="Screenshot 2026-06-20 123224" src="https://github.com/user-attachments/assets/d587efde-00c6-4ad1-8be3-ecc1d3b5a944" />


---

## API Gateway

<img width="1867" height="751" alt="Screenshot 2026-06-20 123323" src="https://github.com/user-attachments/assets/ecb2a74c-469e-4cd3-9fba-bcd72f84bdf1" />


---

## Amazon SNS Topic

<img width="1912" height="767" alt="Screenshot 2026-06-20 123447" src="https://github.com/user-attachments/assets/b0198d70-c9bf-4ace-9d84-aa5b231cf6c4" />


---

## Amazon EventBridge Rule

<img width="1890" height="765" alt="Screenshot 2026-06-20 123635" src="https://github.com/user-attachments/assets/2fd51538-964d-43a7-9574-c2b9496c4ddb" />


---

## Amazon S3 Audio Storage

<img width="1882" height="663" alt="Screenshot 2026-06-20 123804" src="https://github.com/user-attachments/assets/c9c0e141-ad6c-49f9-a6fa-bb6e26babee7" />


---

## Amazon Polly Configuration

<img width="1557" height="587" alt="Screenshot 2026-06-20 123959" src="https://github.com/user-attachments/assets/8f84aea0-806b-4087-8c30-1ea690d6e8ae" />


## SNS alert in email
<img width="1482" height="468" alt="Screenshot 2026-06-20 124254" src="https://github.com/user-attachments/assets/81bfb811-135a-4250-8cf9-4c0869faced7" />



---

# Key Features

* Serverless Architecture
* Event-Driven Processing
* Package Registration and Tracking APIs
* Automated Voice Announcements
* Automated Email Notifications
* Audio File Storage
* Package State Management
* Scalable AWS Solution

---

# Project Outcome

Successfully built an event-driven serverless logistics tracking system that automates package processing, voice notifications, event publishing, and customer communication while reducing manual warehouse operations.

---

# Author

Sahil Dongare


