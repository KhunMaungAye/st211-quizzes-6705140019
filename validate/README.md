# Validate

This folder is a validation exercise for testing reusable input-checking helpers. It emphasizes positive and negative examples for email addresses and age values.

The tests describe the expected behavior of `validate_email()` and `validate_age()`:

- valid email and age inputs should return `True`;
- invalid email formats and age inputs should raise `ValueError`;
- type mismatches and out-of-range values should also be rejected.
