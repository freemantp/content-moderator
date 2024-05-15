# Content moderation service

This service provides a REST interface to classify text into different categories of offensive speech. It uses the _KoalaAI/Text-Moderation_ model to make predictions.

See the OpenAPI documentation under `/docs` for details on how to use it

## Monitoring

Prometheus is used to collect metrics of this service during runtime and exposed via `/metrics`

#### Requests per second

The service also tracks the incoming requests per seconds (rps). The metrics
endpoint can be queried to get the current value of `requests_per_second`

## Start the application

1. Run the server with `uvicorn main:app`
2. Open a browser window and naviagte to <http://127.0.0.1:8000/>

### Prerequisites

- Install dependencies: `pip install -r requirements.txt`

## Further improvements

To run this service in a productive environment, more work is needed:

- Make sure hardware (GPU/TUP) is used for inference where available
- Currently he model is pulled from the web on statup -> make it available offline
- Dockerize the application to be run in a containerized environment
- Add Authentication and transport encryption, eg. throgh an API gateway
- Use an external monitoring system (eg. Grafana) to determine _rps_ across several instances of this service
