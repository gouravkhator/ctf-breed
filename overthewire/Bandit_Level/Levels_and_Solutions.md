# Bandit Levels & Solutions

> This Bandit Level covers Linux Bash commands with basic to intermediate difficulty level.

General note for all levels:
- Perform `ssh` to a particular bandit level, example if we are to login to level 4, then do SSH to `bandit4` user at `bandit.labs.overthewire.org` host, with the password we got from the previous level (ex- Level 3)
- Once we get the next level (ex- Level 5) password in this level's (ex- Level 4) system, we should copy the password and then exit out of the current ssh (ex- ssh of Level 4) by typing `exit`.
- Then, login to next level (ex- Level 5) by typing `ssh bandit5@bandit.labs.overthewire.org -p 2220`.

## Level 0

- Level Goal:
	
	The host to which you need to connect is bandit.labs.overthewire.org, on port 2220.
	
	The username is bandit0 and the password is bandit0.

- bandit0 Password (already given): `bandit0`

- Command Used to SSH:

	```sh
	ssh bandit0@bandit.labs.overthewire.org -p 2220
	```

## Level 0 → Level 1

- Level Goal:

	The password for the next level is stored in a file called **readme** located in the home directory.

	Use this password to log into bandit1 using SSH.

	Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

- Command Used:

	```sh
	cat readme
	```

- bandit1 Password: `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`

## Level 1 → Level 2

- Level Goal:

	The password for the next level is stored in a file called **-** located in the home directory.

- Command Used:

	```sh
	cat ./-
	```

- bandit2 Password: `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`

- More comments:

	The filename given is `-`.

	To cat this dashed filename, we need to specify full path, as this '-' argument is treated as stdin/stdout.

## Level 2 → Level 3

- Level Goal:

	The password for the next level is stored in a file called **spaces in this filename** located in the home directory.

- Command Used:

	```sh
	cat $(echo $(ls))
	```

- bandit3 Password: `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`

- More comments:

	The filename given is a spaced filename. So, we need to stringify it and then we can cat it.

## Level 3 → Level 4

- Level Goal:

	The password for the next level is stored in a hidden file in the inhere directory.

- Command Used:

	```sh
	cd inhere/
	ls -al
	cat .hidden
	```

- bandit4 Password: `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`

- More Comments:

	We have to show the contents of a hidden file here.

## Level 4 → Level 5

- Level Goal:

	The password for the next level is stored in the only human-readable file in the inhere directory.
	
	Tip: if your terminal is messed up, try the “reset” command.

- Command Used:

	```sh
	for file in $(ls)
	do
		echo $file; cat "./$file"; echo ""; 
	done
	```

- bandit5 Password: `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`

- More Comments:

	Here the filenames are `-file0`, `-file1` and so on, and there were around 9 to 10 files. And we had to cat each one of them, to check the contents of the file which has human-readable text in it.

	So, we printed the filename by `echo $file`, and thne we did `cat "./$file"`, as the filename starts with a dash, and dashes are taken as stdin/stdout arguments or flags in Linux. Then we printed a new line with `echo ""`.

## Level 5 → Level 6

- Level Goal:

	The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

	```
    human-readable
    1033 bytes in size
    not executable
	```

- Command Used:

	```bash
	# this function checks if the file is human-readable or not, by checking the file info in brief..
	function passLevel(){
		# $1 is the 1st argument passed to this function..
		# file -ib means file info in brief..
		if [[ $(file -ib $1) == "text/plain; charset=us-ascii" ]]; 
		then
			echo $1; 
		fi; 
	}

	export -f passLevel # exports the shell function so that we can use it..

	<<comments

	This is a multi-line comment in bash..

	Using find command to check the type file, which is of size 1033c (c means the bytes), and is not executable. Then execute the bash -c command, which executes the command which is present in the given string.

	This bash command will be passLevel function. 
	Its 1st argument will be {}, which refers to the file name in the find command. It is given in escaped double quotes, so that if the filename is spaced then also the command will work.
	
	find command should end with a '\;' which means command delimiter.

	comments

	find . -type f -size 1033c ! -executable -exec bash -c "passLevel \"{}\"" \;

	# the above find prints out the filename. Use cat to print the contents of that file..
	```

- bandit6 Password: `DXjZPULLxYr17uwoI01bNLQbtFemEgo7`

- More Comments:

	- Here, we learnt about `file` command with its options, and how to create shell functions.

	- Most of the comments for the working are given in shell script itself.

	- To call a shell function, we do like:

		```sh
		functionname arg0 arg1
		```

## Level 6 → Level 7

- Level Goal: 
	
	The password for the next level is stored somewhere on the server and has all of the following properties:

	```
    owned by user bandit7
    owned by group bandit6
    33 bytes in size
	```

- Command Used:

	```sh
	cd /
	find . -type f -size 33c -exec bash -c "ls -l \"{}\" | grep \"bandit7 bandit6\"" \;
	
	# then we get a file amongst many other permission denied errors..
	# whose filename was: ./var/lib/dpkg/info/bandit7.password

	cat ./var/lib/dpkg/info/bandit7.password
	```

- bandit7 Password: `HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs`

- More Comments:

	- We saw that in the home directory of bandit6, we don't see any important file.
	- So, we `cd` into the root directory `/`.
	- Now, we can use `find` command to search for 33 bytes file, whose `ls -l` will output `bandit7 bandit6`
	- `ls -l` outputs the permissions, then the number of links, then the file owner name, then the file owner group name, then the file size, then the last modified time, then the file/directory name.
	- So, we `grep`ped the output of `ls -l` to see whose owner and group are `bandit7 bandit6`
	- As this check was having space, so we used and escaped the double quotes.


## Level 7 → Level 8

- Level Goal: 
	
	The password for the next level is stored in the file **data.txt** next to the word **millionth**.

- Command Used:

	```sh
	cat data.txt | grep "millionth"
	```

- bandit8 Password: `cvX2JJa4CFALtqS87jk27qwqGhBM9plV`

## Level 8 → Level 9

- Level Goal:

	The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.

- Command Used:

	```sh
	sort data.txt | uniq -u
	```

- bandit9 Password: `UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR`

- More Comments:

	- `uniq -u` prints only unique lines, but requires sorted file to work properly.
	- So, we first sort the file and then pass the sorted output to stdin of `uniq -u`.

## Level 9 → Level 10

- Level Goal:

	The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several `=` characters.

- Command Used:

	```sh
	strings data.txt | grep "=="
	```

- bandit10 Password: `truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk`

- More Comments:

	- When we tried to do `ls -l data.txt`, we see that it is a huge file.
	- When trying `file -ib data.txt`, it shows that this file is a binary file.
	- When trying `grep "=" data.txt`, it only shows the output `Binary file data.txt matches`.
	- So, to get the human-readable string, we use `strings` command, as cat/grep shows just the `Binary file ... matches`.
	- `strings` command ignores the other binary data, and only prints the human-readable data present in the file.
	- We get 4 lines, which contains more than one `=`.
	- And when we try one of the passwords, prefixed with multiple `=`, then we get the bandit10 password as the mentioned one, which works.

## Level 10 → Level 11

- Level Goal:

	The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

- Command Used:

	```sh
	cat data.txt # this cat command prints a base64 encoded data..

	base64 -d data.txt
	# decodes the contents of data.txt using base64 -d, back to human-readable strings 
	```

- bandit11 Password: `IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR`

## Level 11 → Level 12

- Level Goal:

	The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

- Command Used:

	```sh
	cat data.txt | tr n-za-m a-z | tr N-ZA-M A-Z
	```

- bandit12 Password: `5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`

- More Comments:

	- `tr` command has the first parameter as the pattern/letters range to replace, and then the 2nd parameter is the letter range to be replaced with.
	- `n-za-m` to be replaced with `a-mn-z` meaning, replace n with a, replace o with b and so on. Similarly, replace a with n, and z (26) with m (13 that is 26 - 13)..

## Level 12 → Level 13

- Level Goal:

	The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed.
	
	For this level it may be useful to create a directory under `/tmp` in which you can work using mkdir. For example: `mkdir /tmp/myname123`.
	
	Then copy the datafile using `cp`, and rename it using `mv` (read the manpages!)

- Command Used:

	```sh
	mkdir -p /tmp/myname123
	cp data.txt /tmp/myname123
	xxd -r data.txt > data2
	cat data2 # get the crux of the file contents
	file -ib data2 # get properties of this binary file

	# we get that data2 is gzip
	mv data2 data2.gz
	gzip -d data2.gz # decompress gzip file
	
	# we get a decompressed file data2
	cat data2
	file -ib data2
	
	# we see that this is a bzip2 file
	mv data2 data2.bz2
	bzip2 -d data2.bz2

	# this process repeats again and again
	# in the midway, we also get a tar file format, and to untar it:
	# tar -xvf data.tar

	# we repeat above steps till the `file -ib data` gives us text ascii format as the output.
	cat output # to get the text file contents
	```

- bandit13 Password: `8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL`

- More Comments:

	- Firstly, when doing `ls -al`, I saw that there is a file named `data.txt`, as also said in the question.
	- This current folder cannot be copied, written, or edited. But, the file `data.txt` in this folder has following permissions:
		`-rw-r-----  1 bandit13 bandit12`

		It means, the file can be read by anyone in the group: `bandit12`, and current user is `bandit12` which is also in the group `bandit12`. SO, we can either read it, copy it t some other folder etc.

		We do have read and write permissions in the folder `/tmp/....`, so we copied this file to `/tmp/somerandomfolder`.

	- When I did `cat data.txt`, it showed a hexdump output. So, I reversed this hexdump to binary file by `xxd -r data.txt > reversed_hexdump`

	- Now, I checked the output of this by `cat reversed_hexdump`, and it was some binary format like below:

		```
		P^data2.bin=�BZh91AY&SYO�ڞOv�}?}����;4�h�F4LM..........
		```

	- I then did `file -ib reversed_hexdump`, and got the output as: `application/gzip; charset=binary`. So, I renamed this file to have suffix as gz, and then decompressed it using gzip. ANd then I got another binary compressed file which was bzip2, and I renamed that binary file to have suffix as .bz2, and decompressed it using bzip2. Doing this over and over again, I found a file which had properties of `text ascii`, and I printed its contents, to get the password.

	- In short, first check the file properties, then rename the file to that binary file format, and then decompress accordingly. And repeat this step until and unless we get a ascii text file format..
	
	> Admitting that for this level, I passed the xxd command by my own, but then for that binary file, I was not sure what to do. And I got hints from online for this level, then I proceeded myself.

## Level 13 → Level 14

- Level Goal:

	The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user bandit14. 
	
	For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. 
	
	Note: localhost is a hostname that refers to the machine you are working on.

- Command Used:

	```sh
	ssh -i sshkey.private bandit14@localhost

	cat /etc/bandit_pass/bandit14 # to get the bandit14 password
	```

- bandit14 Password: `4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e`

- More Comments:

	- As all users like bandit0 to bandit31 are created in the host `bandit.labs.overthewire.org`, but we were already logged in as bandit13 user in the same host, so we could do `ssh -i <the-identity-for-user-bandit14> bandit14@localhost`.

## Level 14 → Level 15

- Level Goal:

	The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

- Command Used:

	```sh
	nc localhost 30000 < /etc/bandit_pass/bandit14
	```

- bandit15 Password: `BfMYroe26WYalil77FoDi9qh59eK5xNr`

- More Comments:

	- Netcat command can be used to transfer arbitrary data over the network, so we use it to transfer password of bandit14 to localhost:30000, and we get back the reply as "Correct!", followed by the bandit15 password.

## Level 15 → Level 16

- Level Goal:

	The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

	Helpful note: Getting **HEARTBEATING** and **Read R BLOCK**? Use -ign_eof and read the **CONNECTED COMMANDS** section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

- Command Used:

	```sh
	
	```

- bandit16 Password: ``

- More Comments:

	- 
