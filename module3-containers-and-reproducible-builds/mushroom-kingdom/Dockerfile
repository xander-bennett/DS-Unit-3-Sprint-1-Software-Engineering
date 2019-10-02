FROM debian
  
#To make logging/io work with Docker
ENV PYTHONUNBUFFERED=1

#Get our main python dependencies!
RUN apt update && apt upgrade -y && \
apt install python3-pip curl nano -y && \
pip3 install pandas numpy && \
pip3 install -i https://test.pypi.org/simple/ mushroom-kingdom==0.1.4 && \
python3 -c "import powerups; print('Success!')"
