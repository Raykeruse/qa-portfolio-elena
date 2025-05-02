# BUG_001 – DELETE /users/{uuid} returns 500 Internal Server Error

**Summary:**  
When attempting to delete a valid user via DELETE `/users/{uuid}`, the server returns a 500 Internal Server Error instead of the expected 204 No Content response.

---

## 📝 Steps to Reproduce:

1. Send a GET request to `/users` to retrieve a list of users.
2. Copy the UUID of any user from the list.
3. Send a DELETE request to `/users/{uuid}` using the copied UUID.

---

## Expected Result:

- Status code `204 No Content`
- User is removed from the list of users

---

## Actual Result:

- Status code `500 Internal Server Error`
- User is not removed

---

## Environment:

- **API Base URL:** `https://dev-gs.qa-playground.com/api/v1`
- **Authorization:** Valid Bearer token (see TC_001)
- **X-Task-Id:** API-1
- **OS:** macOS 15.3.1 (24D70)
- **Browser:** Chrome 135.0.7049.115 (x86_64)
- **Test Tool:** Swagger + Python `requests`

---

## Notes:

- This issue has been consistently reproducible.
- Confirmed that the UUID sent in DELETE request is valid and exists.
- The bug prevents passing of test case [TC_001_Delete_User.md](../manual_test_cases/TC_001_Delete_User.md)
> Known Issue: [BUG_001](BUG_001_DeleteUser_500.md) — DELETE request returns 500.

---

**Severity:** High  
**Status:** Open  
**Reported by:** Elena (Raykeruse)  
**Date:** 2025-05-03
