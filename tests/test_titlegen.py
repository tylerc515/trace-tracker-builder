from app.titlegen import generate_title


def test_generate_title_example():
    title = generate_title("International Paper", "Mansfield, LA", "Recovery Boiler #2", "June 2026")
    assert title == "IP MANSFIELD RB2 — 2026 OUTAGE NDE TRACKSHEET"


def test_generate_title_no_comma_location():
    title = generate_title("International Paper", "Mansfield", "Recovery Boiler #2", "June 2026")
    assert title.startswith("IP MANSFIELD RB2")


def test_boiler_abbreviation_fallback_without_digits():
    title = generate_title("Acme Co", "Springfield, IL", "Main Boiler", "March 2025")
    assert "MAIN BOILER" in title or "Main Boiler" in title
    assert "2025" in title
