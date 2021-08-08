### Build and install packages
FROM python:3.8 as build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /tags/
WORKDIR /tags
RUN pip install -r requirements.txt

### Final image
FROM python:3.8-slim

RUN apt-get update \
  && apt-get install -y \
  libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY --from=build-python /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY ./tags /tags
WORKDIR /tags

EXPOSE 8000
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "tags.asgi:application"]
