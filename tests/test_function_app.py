import sys
from pathlib import Path

import azure.functions as func

# Ensure imports work when pytest is executed from repository root (CI/GitHub Actions).
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from function_app import divide, multiply  # noqa: E402


def _request(params: dict[str, str]) -> func.HttpRequest:
    return func.HttpRequest(
        method="GET",
        url="http://localhost/api/test",
        params=params,
        body=b"",
    )


def _body_text(response: func.HttpResponse) -> str:
    return response.get_body().decode("utf-8")


def test_multiply_success_with_integer_inputs() -> None:
    response = multiply(_request({"A": "2", "B": "3"}))

    assert response.status_code == 200
    assert _body_text(response) == "6"


def test_multiply_success_with_decimal_inputs() -> None:
    response = multiply(_request({"A": "2.5", "B": "4"}))

    assert response.status_code == 200
    assert _body_text(response) == "10"


def test_divide_success_with_decimal_result() -> None:
    response = divide(_request({"A": "7", "B": "2"}))

    assert response.status_code == 200
    assert _body_text(response) == "3.5"


def test_error_when_query_parameter_is_missing() -> None:
    response = multiply(_request({"A": "2"}))

    assert response.status_code == 400
    assert _body_text(response) == "Query parameters A and B are required."


def test_error_when_query_parameter_is_not_numeric() -> None:
    response = multiply(_request({"A": "abc", "B": "2"}))

    assert response.status_code == 400
    assert _body_text(response) == "Query parameters A and B must be numeric."


def test_error_when_dividing_by_zero() -> None:
    response = divide(_request({"A": "10", "B": "0"}))

    assert response.status_code == 400
    assert _body_text(response) == "Parameter B must not be zero for division."
