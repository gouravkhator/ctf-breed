# PWN | Codechainz

A `Dockerfile` is provided and a sample empty `flag.txt` is given. 

## Work Tried

- I made the directory similar to what was asked in `Dockerfile` and then built the docker image.
- Then, ran the `app` inside the docker container. Note that there was a server already hosted with original flag file, and when we did `netcat` to it, it also ran the same `app` file.
- So, we need to crack this `app` file and then that exploit can be used in original challenge too.
- I tried but could not crack this file.
- We have to run this app as `./app` inside the docker container.
