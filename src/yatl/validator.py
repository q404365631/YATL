from requests import Response


class ResponseValidator:
    def __init__(self, response: Response, expect_spec: dict):
        self.response = response
        self.expect_spec = expect_spec

    def _validate_json_response(self, data: dict, expected_json: dict):
        for key, value in expected_json.items():
            if key not in data:
                raise AssertionError(f"Key '{key}' is missing in response")
            if type(data[key]) is dict:
                self._validate_json_response(data[key], value)
            if data[key] != value:
                raise AssertionError(
                    f"For key '{key}' expected '{value}', got '{data[key]}'"
                )

    def check_expectations(self):
        expected_status = self.expect_spec.get("status")
        if expected_status is not None and self.response.status_code != expected_status:
            raise AssertionError(
                f"Expected status {expected_status}, got {self.response.status_code}"
            )
        body: dict = self.expect_spec.get("body")
        if body is None:
            return
        expected_json: dict = body.get("json")
        if self.expect_spec and not self.response.json():
            raise AssertionError("Response is not JSON, but JSON was expected")
        data = self.response.json()
        if expected_json is not None:
            self._validate_json_response(data, expected_json)
