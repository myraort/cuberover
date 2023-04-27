sudo docker buildx build --platform linux/arm64 -t rpi_pc_server --load .
sudo docker tag rpi_pc_server:latest bretwitt/rpi_pc_server:latest
sudo docker push bretwitt/rpi_pc_server:latest 
