import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from backend.model import predict_attendance
from backend.validation import validate_appointment_payload


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = PROJECT_ROOT / "database" / "appointments.jsonl"


class JsonlAppointmentDatabase:
    def __init__(self, path=DEFAULT_DB_PATH):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, record):
        existing_count = 0
        if self.path.exists():
            existing_count = sum(1 for line in self.path.read_text().splitlines() if line.strip())

        saved_record = {
            "id": existing_count + 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            **record,
        }
        with self.path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(saved_record) + "\n")
        return saved_record


def handle_appointment_request(payload, db=None):
    errors = validate_appointment_payload(payload)
    if errors:
        return {"status": 400, "errors": errors}

    prediction = predict_attendance(payload)
    saved = (db or JsonlAppointmentDatabase()).save(
        {
            "name": payload["name"].strip(),
            "age": payload["age"],
            "phone": payload["phone"].strip(),
            "prediction": prediction,
        }
    )
    return {"status": 201, "data": saved}


class AppointmentRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, body):
        response = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_POST(self):
        if self.path != "/appointments":
            self._send_json(404, {"error": "Not found"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json(400, {"errors": {"body": "Request body must be valid JSON"}})
            return

        result = handle_appointment_request(payload)
        self._send_json(result["status"], result)


def run_server(host="127.0.0.1", port=8000):
    server = HTTPServer((host, port), AppointmentRequestHandler)
    print(f"AI Appointment API running at http://{host}:{port}")
    print("POST JSON to /appointments")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

