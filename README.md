ATS Integration Microservice
📌 Overview

This project is a serverless microservice built using Python and the Serverless Framework. It provides a unified API to interact with an Applicant Tracking System (ATS).

The service exposes endpoints to:

Fetch jobs
Create candidates
Retrieve applications
🚀 Tech Stack
Python
Serverless Framework
AWS Lambda (offline mode)
Postman (for API testing)
⚙️ Setup Instructions
1. Clone the repository
git clone <your-repo-link>
cd ats-integration
2. Install dependencies
pip install -r requirements.txt
npm install
3. Set environment variables
Windows (PowerShell):
$env:ATS_API_KEY="demo_key"
$env:ATS_BASE_URL="https://mock-api.com"
4. Run the service
serverless offline

Service will run at:

http://localhost:3000
📡 API Endpoints
🔹 GET /dev/jobs

Fetch all jobs

Response:

[
  {
    "id": "1",
    "title": "Software Engineer",
    "location": "Remote",
    "status": "OPEN",
    "external_url": "http://example.com/job/1"
  }
]
🔹 POST /dev/candidates

Request Body:

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "resume_url": "http://resume.com",
  "job_id": "1"
}

Response:

{
  "message": "Candidate created successfully"
}
🔹 GET /dev/applications?job_id=1

Response:

[
  {
    "id": "app_456",
    "candidate_name": "John Doe",
    "email": "john@example.com",
    "status": "APPLIED"
  }
]
🧪 Testing with Postman
Open Postman
Create a new request
Use the endpoints listed above
For POST requests:
Select Body → raw → JSON
Paste request body
⚠️ Notes
This project uses a mock ATS implementation for demonstration.
In a real-world scenario, this can be connected to APIs like Greenhouse, Lever, or Workable.
Environment variables are used for secure configuration.

✅ Features Implemented
REST API endpoints
Serverless deployment setup
Environment variable handling
Error handling
Mock ATS integration
Postman testing support
## 📬 Postman Collection

You can import the Postman collection to test APIs easily:

1. Open Postman
2. Click Import
3. Select the file: ATS_Integration_APIs.postman_collection.json

This will load all API endpoints with pre-configured requests.