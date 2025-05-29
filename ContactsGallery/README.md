
# Smart Contact Saver – Fully Serverless Web App on AWS

The **Smart Contact Saver** is a fully serverless web application built on top of AWS services. It allows users to **add**, **view**, **edit**, and **delete** contacts through a simple and elegant single-page interface. The backend is implemented using AWS Lambda, API Gateway, and DynamoDB, while the frontend is hosted on Amazon S3.

---

##  Features

*  Add new contacts with name, email, and phone.
*  View all saved contacts in a clean UI.
*  Edit contact information in-place.
*  Delete any contact with confirmation.
*  Search and sort contacts in real time.
*  Toast notifications for success and errors.
*  100% serverless and scalable architecture.
*  Modern responsive UI using HTML, CSS, and JavaScript.

---

##  Architecture Overview

**Frontend:**

* **Amazon S3** – Hosts a static single-page application (HTML/CSS/JS).

**Backend:**

* **Amazon API Gateway** – Exposes RESTful endpoints for CRUD operations.
* **AWS Lambda** – Four separate Lambda functions:

  * `CreateContact` – Adds a new contact to DynamoDB.
  * `GetContacts` – Retrieves all contacts from DynamoDB.
  * `UpdateContact` – Updates existing contact details.
  * `DeleteContact` – Deletes a contact from the table.
* **Amazon DynamoDB** – Stores contact data in a NoSQL table.

---

## 🛠️ Tech Stack

| Component        | Service Used                      |
| ---------------- | --------------------------------- |
| Frontend Hosting | Amazon S3                         |
| API Gateway      | REST API                          |
| Backend Logic    | AWS Lambda (Node.js / Python)     |
| Database         | Amazon DynamoDB                   |
| IAM              | Role-based permissions for Lambda |
| Notifications    | Toast alerts (JavaScript UI)      |

---



##  Live Demo

You can access the live web app here:
 [**Smart Contact Saver (Hosted on S3)**](http://contactgallery11.s3-website-us-east-1.amazonaws.com)


---

##  How It Works

1. **User Interaction:** Users interact with a simple web form to add or edit contacts.
2. **API Calls:** The frontend JavaScript uses `fetch()` to communicate with API Gateway endpoints.
3. **Lambda Execution:** Each endpoint invokes a separate Lambda function to perform the requested action.
4. **DynamoDB Integration:** Contacts are stored, updated, or removed from the DynamoDB table.
5. **Live UI Updates:** All changes reflect instantly in the UI with real-time feedback and animations.

---



##  Security & Permissions

* Fine-grained IAM roles were used to give Lambda functions access to only required DynamoDB actions (PutItem, GetItem, UpdateItem, DeleteItem).
* All endpoints are secured through API Gateway with controlled access.

---

##  Learning Outcomes

* Hands-on experience with serverless architecture.
* Practical use of core AWS services (S3, Lambda, API Gateway, DynamoDB).
* Frontend integration with REST APIs.
* Real-world CRUD application using fully managed infrastructure.

---



