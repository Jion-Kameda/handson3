# Non-Functional Requirements

## 1. Platform and Hosting
- The system shall run on Azure Functions.
- Hosting plan shall be Azure Functions Consumption Plan.
- Deployment region shall be Azure Japan East.

## 2. Technology Stack
- Development language shall be Python 3.11.

## 3. Availability and Operations (Recommended Baseline)
- Function App shall emit execution logs for success and failure cases.
- Basic monitoring shall be enabled to track requests, failures, and latency.

## 4. Security (Recommended Baseline)
- API access policy (anonymous vs key-protected) shall be defined before production use.
- Input validation shall be implemented for all query parameters.

## 5. Performance (Recommended Baseline)
- API design shall remain lightweight to fit Consumption Plan cold start behavior.
- Expected response time target should be defined (for example, under 3 seconds under normal conditions).

## 6. Cost (Recommended Baseline)
- Monthly cost monitoring should be enabled to avoid unexpected Consumption Plan charges.

## 7. Maintainability (Recommended Baseline)
- Source code and tests should be separated into dedicated folders (`src`, `tests`).
- API behavior and error rules should be documented in this `doc` directory.

## 8. To Confirm
- Required SLA/availability target is not yet defined.
- Maximum request volume/concurrency target is not yet defined.
- Required log retention period is not yet defined.
- Production authentication requirement is not yet defined.
