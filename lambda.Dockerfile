FROM python:3.9.16-slim-bullseye

WORKDIR /function

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

RUN pip install --upgrade pip

# Copy function code
COPY . .

# Install the function's dependencies
RUN pip install -r requirements.txt
RUN playwright install-deps
RUN playwright install firefox

RUN pip install awslambdaric

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]