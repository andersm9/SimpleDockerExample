# SimpleDockerExample
docker build -t MyfFask:v3 Myflask_Version

docker image ls

  //provdes image ID

docker run -p 8000:5000 <Image_ID>

docker exec -it <image_ID> bash
