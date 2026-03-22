# Mock ATS Client (no external API calls)

def get_jobs_from_ats(page=1):
    return {
        "jobs": [
            {
                "id": "1",
                "title": "Software Engineer",
                "location": "Remote",
                "status": "OPEN",
                "url": "http://example.com/job/1"
            },
            {
                "id": "2",
                "title": "Backend Developer",
                "location": "Delhi",
                "status": "OPEN",
                "url": "http://example.com/job/2"
            }
        ]
    }


def create_candidate_in_ats(data):
    return {
        "id": "123",
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "resume_url": data.get("resume_url")
    }


def attach_candidate_to_job(candidate_id, job_id):
    return {
        "application_id": "app_456",
        "candidate_id": candidate_id,
        "job_id": job_id,
        "status": "APPLIED"
    }


def get_applications_from_ats(job_id):
    return {
        "applications": [
            {
                "id": "app_456",
                "name": "Test User",
                "email": "test@example.com",
                "status": "APPLIED"
            },
            {
                "id": "app_789",
                "name": "Jane Doe",
                "email": "jane@example.com",
                "status": "SCREENING"
            }
        ]
    }