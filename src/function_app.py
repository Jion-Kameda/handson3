from decimal import Decimal, InvalidOperation

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def _parse_query_numbers(req: func.HttpRequest):
    a_raw = req.params.get("A")
    b_raw = req.params.get("B")

    if a_raw is None or b_raw is None:
        return None, None, "Query parameters A and B are required."

    try:
        a = Decimal(a_raw)
        b = Decimal(b_raw)
    except InvalidOperation:
        return None, None, "Query parameters A and B must be numeric."

    return a, b, None


def _decimal_to_text(value: Decimal) -> str:
    normalized = value.normalize()

    if normalized == normalized.to_integral():
        return format(normalized.quantize(Decimal("1")), "f")

    text = format(normalized, "f")
    return text.rstrip("0").rstrip(".")


@app.route(route="multiply", methods=["GET"])
def multiply(req: func.HttpRequest) -> func.HttpResponse:
    a, b, error = _parse_query_numbers(req)

    if error is not None:
        return func.HttpResponse(error, status_code=400, mimetype="text/plain")

    result = a * b
    return func.HttpResponse(_decimal_to_text(result), status_code=200, mimetype="text/plain")


@app.route(route="divide", methods=["GET"])
def divide(req: func.HttpRequest) -> func.HttpResponse:
    a, b, error = _parse_query_numbers(req)

    if error is not None:
        return func.HttpResponse(error, status_code=400, mimetype="text/plain")

    if b == 0:
        return func.HttpResponse("Parameter B must not be zero for division.", status_code=400, mimetype="text/plain")

    result = a / b
    return func.HttpResponse(_decimal_to_text(result), status_code=200, mimetype="text/plain")
