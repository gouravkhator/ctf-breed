# OverTheWire -- Practising Security Concepts

The wargames offered by the [OverTheWire](https://overthewire.org/wargames/) community can help us to learn and practice security concepts in the form of fun-filled games.

I will not make this repo public, as it has the levels solutions, which might destroy the purpose of OverTheWire.

This repo has all the commands/solutions, that I googled and researched via the usage of the commands, but did not try to copy the main solution from anywhere.

## Personal CyberSec Setup

We are using kali docker image, and then installing all kali tools, then creating a sudoer so that we do all stuffs whilst in the normal user.

Kali docker image `root` user's password is not present actually.

### Installation

- Install docker on the main host machine and then run the below commands:

    ```sh
    docker pull kalilinux/kali-rolling
    docker create -it --name kali kalilinux/kali-rolling
    docker exec -it kali bash
    ```

- We are logged in as `root` user already. Now, we update the repositories and install all the tools required from a metapackage in kali named: `kali-linux-headless`.

    ```sh
    apt update
    apt install kali-linux-headless
    ```

-------------

### Kali Package Installation Notes

- This metapackage installs a loads of stuffs and frameworks. Some packages prompt us for some inputs of Yes/No. Just read the question and act accordingly.

- Keyboard Layout when asked for will be: `English (US)`

- Character set when asked for will be: `UTF-8`

- This metapackage also installs Kismet framework which is a wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.

- And to use Kismet as a normal user, we need to add that user to newly created group named `kismet`.

-------------

### Create a Sudoer

Create a new user named `gourav` and then make him a sudoer.

```sh
adduser gourav
usermod -aG sudo gourav # adding gourav user to the group: sudo
usermod -aG kismet gourav # adding gourav user to the group: kismet
su gourav # to switch user to gourav 
```

When in the `gourav` user, we can switch back to `root` user by doing:
```sh
sudo su
```

This lets `gourav` user enter his sudo password to switch user to root..

-------------

### Start/Stop the Existing Container

- We can `Ctrl+D` to exit out of each shell, and then stop the container by the following commands:

    ```sh
    docker stop kali
    ```

- We can start the container again by the following commands:

    ```sh
    docker ps -a # check if the container named kali is present already or not
    docker start kali
    docker exec -it kali bash
    su gourav
    ```
