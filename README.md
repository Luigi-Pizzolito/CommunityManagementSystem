# CommunityManagementSystem
 A community management system for Shanghai Lingang competition.

## System Components
 This system uses *Docker Compose* in order to run all of its application components in containers. Below is the layout:
 ```txt
 Docker Containers
 ├── webserver
 │   └── NGINX static web server for web app.
 ├── apiserver
 │   └── WebSocket API server for web app.
 ├── database
 │   └── MongoDB database.
 ├── cctvparking-feed
 │   └── OpenCV/Tensorflow AI parking detection from CCTV video with CUDA acceleration.
 └── iotsensors-feed
     └── Bridge service to automatically import external IoT API feeds to DB.
  ```

## Running
 Start the entire stack by running \
 `docker-compose up`
 \
 Try scaling the CCTV parking feed container by running \
 `docker-compose up --scale cctvparking=3 -d` \
 If this works, try uncommenting the replicated mode from `cctvparking` container to natively run the scaling from `compose.yml`.