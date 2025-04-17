# API Tests – Place Details

This folder contains automated API tests using Python `requests` and `pytest`.

## ✅ Tests Included

- `test_place_details_fields`:  
  Validates expected fields from the response of the "get place details" endpoint.

- `test_name_field_negative_check`:  
  Intentional failure to check the behavior when a value does not match expectations (used for negative validation).

## 📎 Tech Stack

- Python 3
- `requests` library
- `pytest`

## 🚀 Run Tests

```bash
pytest tests/test_api/test_place_details.py -v
