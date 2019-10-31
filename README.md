# Description
Python application that streams 2 videos while adding random number of rectangels on each frame (simulate motion detection)
via websockets and also displays plots of rectangels count per frame.

Videos used: 
- https://www.youtube.com/watch?v=FIxYCDbRGJc
- https://www.youtube.com/watch?v=6zUc-mpMGrs

# Run 

From project directory:
 ```console
   :~$ docker image build -t videos .
   :~$ docker container run --publish 8000:8000 --detach videos
 ```
 
 App will be available at `0.0.0.0:8000`
