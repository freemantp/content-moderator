# AI Content moderation service
This service classifies text into offensive speech categories via a REST interface, leveraging the KoalaAI/Text-Moderation model for content analysis.

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
- Hardware (GPU/TPU) should be used inference where available
- Currently the model is pulled from the web on statup -> make it available offline
- Add authentication and transport encryption, eg. through an API gateway
- Use an external monitoring system (eg. Grafana) to determine _rps_ across several instances of this service
