# Mocking Practice

This folder contains small Python exercises for testing code with controlled
dependencies. The tests use `pytest` as the test runner and
`unittest.mock` (`Mock` and `patch`) to replace collaborators, configure
return values, simulate different outcomes, and verify calls.

## What is covered

- **Basic mocks** in `test_mock_basic.py`: configure a return value, use mock
  attributes, and make calls to mock methods.
- **Return values and side effects** in `test_return_values.py`: provide
  different values for consecutive calls.
- **Call verification** in `test_verify_calls.py`: check that a method was
  called, and that it was called once.
- **Dependency injection** in `payment.py` and `test_payment.py`: pass a
  gateway into `OrderProcessor` and replace it with a mock in the test.
- **Patching a module dependency** in `notifications.py` and
  `test_notifications.py`: replace the email-sending function so the test
  does not contact an email server.
- **Service testing** in `user_service.py` and `test_user_service.py`: use a
  mock database to test how `UserService` retrieves a username.
- **Patching a function** in `date_utils.py` and `test_date_utils.py`: control
  the year used to create a report name.
- **Weather classification** in `weather.py` and `test_weather.py`: replace
  the temperature function to test both supported outcomes without depending
  on a real temperature source.
- **Additional mock exercises** in `Lab_Mock_Obj/`: practice comparisons,
  return values, side-effect lists/functions, and exceptions.

## Weather example

`describe_weather()` calls `get_temperature()`. In the current example,
`get_temperature()` returns `20`, and `describe_weather()` returns
`"Pleasant"` for temperatures of 15 or higher and `"Cold"` otherwise.

The tests patch `weather.get_temperature`, which is the name looked up by
`describe_weather()` in the `weather` module. The cold-weather test previously
used the misspelled target `weather.get_tempeature`. `patch` could not find
that attribute, so the test failed before its assertion ran. The target is
now spelled correctly.

## Run the tests

Run all tests in this folder, including the nested exercises:

```bash
python3 -m pytest mock -q
```

Run only the weather tests:

```bash
python3 -m pytest mock/test_weather.py -q
```

Install `pytest` if it is not already available:

```bash
python3 -m pip install pytest
```

`unittest.mock` is part of Python's standard library, so it does not need a
separate installation.
