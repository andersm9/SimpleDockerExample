# SimpleDockerExample
//from directory above SimpleDockerExample

docker build -t myflask:v3 SimpleDockerExample
              (tag [name]:[tag] ) directory

docker image ls

  //provdes image ID

docker run -p 8000:5000 <Image_ID>
              (external: internal)


  // http://localhost:8000/
  
docker container ls
  //provides container ID

docker exec -it <container_ID> bash
  /// provides bash shell into container
