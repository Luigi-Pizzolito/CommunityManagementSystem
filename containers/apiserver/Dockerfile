# syntax=docker/dockerfile:1
# -- Base image
FROM golang:alpine
WORKDIR /src
# -- Copy files to container
COPY . .
# -- Install dependencies
RUN go mod download
RUN go build -o /bin/apiserver ./src
# -- Start program
ENTRYPOINT ["/bin/apiserver"]