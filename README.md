# Entity_Extractor_EC2
deployment of Entity Extractor application on EC2 instance with Docker.

# steps to follow

1- start EC2 instance:<br>
```bash

ssh -i flask.pem ubuntu@IP ADDRESS

```

2-Once in instance, add dependencies: <br>



```bash

sudo apt-get update 

```

```bash

docker

```
(to check if we have docker installed)
<br>
3- clone git by:<br>



```bash

git clone (url)

```

4-Install docker using: <br>



```bash

sudo apt-get install docker-compose



```

5- check again docker image: <br>



```bash

docker <br>

docker-compose 

```

6- Install pip : <br>


```bash

sudo apt install python3-pip

```

7- Run requirements.txt : <br>

```bash

pip3 install -r requirements.txt

```

8- Check if all needed dependencies are there<br>

```bash

pip3 freeze

```
9-Check if we have docker images:<br>

```bash

sudo docker images

```
10-Build docker image : <br>


```bash

sudo docker-compose build

OR

sudo apt-get install docker-compose -y

```

11-check again docker images : <br>

```bash

sudo docker images

```

12-To run this image:<br>

```bash

sudo docker-compose up --build -d

```
13- Check current running images by:<br>
```bash
sudo docker ps

```
14-Remember to open ports from "Security Groups":<br>

```bash

port 8000, 8080 
```

15- Associate Elastic IP

16- Setup SSL certificate into your AWS EC2 instance i.e using https with elastic IP

- ^On a side note, we can use vim editor by using<br>

```bash

sudo vim fliename
```
- ^ for deleting docker image: <br>

https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/

17- To Install AWS CLI v2 & configure IAM role

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awsclivs.zip"
# Results

### Output from raw text

!["User Interface"](images/1.png)

!["User Interface"](images/2.png)

### Output from loaded test text file

!["User Interface"](images/3.png)

!["User Interface"](images/4.png)

# References

- https://www.youtube.com/watch?v=2tQ_Yn6O3f4&list=PL5KTLzN85O4K3zhnNPNCgE_Lt-pUsY7YO

- https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/

- https://www.youtube.com/watch?v=rNoRB_7pANo&list=PL5KTLzN85O4I4ljDgueVff0UxIKXtzi-8&index=3
