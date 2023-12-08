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
