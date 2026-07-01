# Functional Requirements

## 1. API Endpoints
- The system shall provide two HTTP API endpoints:
  - Multiply API
  - Divide API

## 2. Request Parameters
- Both APIs shall receive input values using query string parameters:
  - `A`
  - `B`
- `A` and `B` are treated as numeric input values.

## 3. Multiply API Behavior
- The Multiply API shall return the result of `A * B`.

## 4. Divide API Behavior
- The Divide API shall return the result of `A / B`.

## 5. Browser Accessibility
- A user shall be able to call each API by entering the URL in a browser.
- The API shall return the calculation result in the HTTP response body so it can be viewed directly in the browser.

## 6. HTTP Interface
- The APIs shall be exposed as HTTP-triggered Azure Functions.
- The APIs shall support direct invocation via URL.

## 7. Error Handling (Baseline)
- If `A` or `B` is missing, the API shall return a client error response.
- If `A` or `B` is not numeric, the API shall return a client error response.
- For Divide API, if `B = 0`, the API shall return a client error response.

## 8. Assumptions / To Confirm
- HTTP method is assumed to be `GET`.
- Response format is assumed to be plain text or JSON with a single result field.
- Numeric type (integer-only vs decimal support) is not yet fixed.
- Rounding/precision rules for division are not yet fixed.
- Exact status codes and error message format are not yet fixed.
