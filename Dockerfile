FROM bitnami/pytorch

LABEL maintainer="Michael Morandi"

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install app
COPY *.py .
RUN mkdir cache

ENV HF_HOME=/app/cache
ENV PATH="${PATH}:/opt/bitnami/python/bin/"

# runtime config
EXPOSE 8000 
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]