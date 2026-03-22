import json
from ats_client import *

def response(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body)
    }


# ✅ GET /jobs
def get_jobs(event, context):
    try:
        data = get_jobs_from_ats()

        jobs = []
        for job in data.get("jobs", []):
            jobs.append({
                "id": job.get("id"),
                "title": job.get("title"),
                "location": job.get("location"),
                "status": job.get("status", "OPEN"),
                "external_url": job.get("url")
            })

        return response(200, jobs)

    except Exception as e:
        return response(500, {"error": str(e)})


# ✅ POST /candidates
def create_candidate(event, context):
    try:
        body = json.loads(event["body"])

        candidate_payload = {
            "name": body["name"],
            "email": body["email"],
            "phone": body["phone"],
            "resume_url": body["resume_url"]
        }

        candidate = create_candidate_in_ats(candidate_payload)

        attach_candidate_to_job(candidate["id"], body["job_id"])

        return response(201, {"message": "Candidate created successfully"})

    except Exception as e:
        return response(500, {"error": str(e)})


# ✅ GET /applications
def get_applications(event, context):
    try:
        job_id = event["queryStringParameters"]["job_id"]

        data = get_applications_from_ats(job_id)

        apps = []
        for app in data.get("applications", []):
            apps.append({
                "id": app.get("id"),
                "candidate_name": app.get("name"),
                "email": app.get("email"),
                "status": app.get("status", "APPLIED")
            })

        return response(200, apps)

    except Exception as e:
        return response(500, {"error": str(e)})