# 🟦 AWS Serverless Inventory Processing Lab  

This project implements a fully serverless architecture on AWS to process inventory files, store data in DynamoDB, and send low-stock alerts using Amazon SNS.  
The pipeline is completely serverless—no EC2, no servers to manage.

---

## 🚀 **Architecture Overview**

The solution uses the following AWS services:

- **Amazon S3** → Upload inventory CSV files  
- **AWS Lambda** → Processes the file and inserts items into DynamoDB  
- **Amazon DynamoDB** → Stores inventory data  
- **Amazon SNS** → Sends email alerts for low-stock items  
- **Amazon CloudWatch** → Logs and monitoring  

---

## 📦 **How It Works**

1. User uploads `items.csv` to an S3 bucket.  
2. S3 event triggers a Lambda function.  
3. Lambda reads the CSV file, parses items, and inserts them into DynamoDB.  
4. If any item's quantity is **below 10**, Lambda sends an alert via SNS.  
5. Everything is logged in CloudWatch.

---

## 📁 **Project Structure**

---

## 🧪 Sample CSV

---

## 🔧 Technologies Used

- AWS Lambda  
- Amazon S3  
- DynamoDB  
- SNS  
- CloudWatch  
- Python  

---

## 👨‍💻 Author

Ahmed Hamed  
Serverless Inventory Lab
