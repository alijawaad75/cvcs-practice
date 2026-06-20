import threading
from http.server import HTTPServer
import json
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

from backend.app import AppointmentRequestHandler, JsonlAppointmentDatabase


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_frontend_form_books_appointment_through_api(tmp_path):
    database = JsonlAppointmentDatabase(tmp_path / "appointments.jsonl")
    handler = type(
        "TestAppointmentRequestHandler",
        (AppointmentRequestHandler,),
        {"database": database},
    )
    server = HTTPServer(("127.0.0.1", 0), handler)
    host, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    frontend_path = PROJECT_ROOT / "frontend" / "appointment_form.html"

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            api_url = json.dumps(f"http://{host}:{port}/appointments")
            page.add_init_script(f"window.APPOINTMENT_API_URL = {api_url}")
            page.goto(frontend_path.as_uri())

            page.get_by_label("Patient name").fill("Ali Khan")
            page.get_by_label("Age").fill("25")
            page.get_by_label("Phone").fill("+923001234567")
            page.get_by_role("button", name="Book appointment").click()

            result = page.locator("#result")
            expect(result).to_contain_text('"status": 201')
            expect(result).to_contain_text('"will_attend": true')
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
