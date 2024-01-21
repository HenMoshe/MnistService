# Build the MNIST gRPC Server Docker Image
echo "Building MNIST gRPC Server Docker Image..."
docker build -f Dockerfile.server -t mnist-grpc-server .

# Run the MNIST gRPC Server Container
echo "Running MNIST gRPC Server Container..."
docker run -d --name mnist-server -p 50051:50051 mnist-grpc-server

# Build the MNIST gRPC Client Docker Image
echo "Building MNIST gRPC Client Docker Image..."
docker build -f Dockerfile.client -t mnist-grpc-client .

# Run the MNIST gRPC Client Container
echo "Running MNIST gRPC Client Container..."
docker run -it --rm --name mnist-client --link mnist-server mnist-grpc-client