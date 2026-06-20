import json
import sys
import threading
import time
from http.server import HTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.app import AppointmentRequestHandler, JsonlAppointmentDatabase


def main():
    database = JsonlAppointmentDatabase(PROJECT_ROOT / "database" / "demo-appointments.jsonl")
    handler = type(
        "DemoAppointmentRequestHandler",
        (AppointmentRequestHandler,),
        {"database": database},
    )
    server = HTTPServer(("127.0.0.1", 0), handler)
    host, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    frontend_path = PROJECT_ROOT / "frontend" / "appointment_form.html"
    api_url = json.dumps(f"http://{host}:{port}/appointments")

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, slow_mo=700)
            page = browser.new_page()
            page.add_init_script(f"window.APPOINTMENT_API_URL = {api_url}")
            page.goto(frontend_path.as_uri())

            page.get_by_label("Patient name").fill("Ali Khan")
            page.get_by_label("Age").fill("25")
            page.get_by_label("Phone").fill("+923001234567")
            page.get_by_role("button", name="Book appointment").click()

            page.locator("#result").wait_for()
            time.sleep(5)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
