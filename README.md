# MNIST gRPC Service - Project Setup Guide

This guide provides detailed instructions on how to set up and run the MNIST gRPC service, which is designed to stream MNIST dataset samples to a client. You can run the service locally, via Docker containers, or using a provided script.

## Prerequisites

Before proceeding, ensure you have the following installed:

- Python 3.8 or higher
- Docker (for containerized setup)

## Running with Docker Containers

### Using the Script

1. Navigate to the project's root directory.
2. Run the following command to execute the `runContainers.sh` script:
   ```bash
   ./runContainers.sh


## Manual Docker Setup

In case the script doesn't work as intended, follow these steps to build and run Docker containers manually:

### Building and Running the Server

  1. Build the server Docker image:
     ```bash
     docker build -f Dockerfile.server -t mnist-grpc-server --no-cache .

  2. Run the server container:
     ```bash
     docker run -d --name mnist-server -p 50051:50051 mnist-grpc-server
		
### Building and Running the Client

	1. Build the client Docker image:
  	 ```bash
  	 docker build -f Dockerfile.client -t mnist-grpc-client --no-cache .


	2. Run the client container:
  	 ```bash
  	 docker run -it --rm --name mnist-client --link mnist-server mnist-grpc-client

## Running Locally Without Docker
To run the MNIST gRPC service locally without Docker, follow these steps:

### Server Setup
Make sure you are in the project main directory (/MnistService).

  1. Install required dependencies:
  	 ```bash
     pip install -r requirements_server.txt

  2. Run the server:
  	 ```bash
     python mnistServerRun.py

### Client Setup
Make sure you are in the project main directory (/MnistService).

	1.Install required dependencies:
		```bash
  	pip install -r requirements_client.txt

	2.Run the client:
		```bash
  	python MnistClientRun.py
