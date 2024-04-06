# Content moderation service

This service provides a REST interface to classify text into different categories of offensiveness. It uses the *KoalaAI/Text-Moderation* model to make predictions.

See the OpenAPI documentation under `/docs` for details on how to use it

## Monitoring
Prometheus is used to collect metrics of this service during runtime. They are exposed via `/metrics` 

#### Requests per second
The service also tracks the incoming requests per seconds. The metrics 
endpoint can be queried to get the current value of 
`requests_per_second`

## Improvements
To run this service in a productive environment, more work is needed.

* Make sure hardware (GPU/TUP) is used for inference where available
* Currently he model is pulled from the web on statup -> make it available offline
* Dockerize the application to be run in a containerized environment
* Add Authentication and transport encryption, eg. throgh an API gateway
* Use an external monitoring system (eg. Prometheus) to determine rps across several instances of this service

## Start the application
`uvicorn main:app`