# SimpleDockerExample
//from directory above SimpleDockerExample

docker build -t MyFask:v3 SimpleDockerExample

docker image ls

  //provdes image ID

docker run -p 8000:5000 <Image_ID>

docker exec -it <image_ID> bash
