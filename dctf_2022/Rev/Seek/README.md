# Reverse Engineering | Seek

In `seek.c` challenge file, main code is for reading a flag file, and similar to below code is run multiple times:

```c
fseek(fp, 5, SEEK_SET);
char c = fgetc(fp);
if(c != 32){
  oops();
}

fseek(fp, 60, SEEK_SET);
c = fgetc(fp);
if(c != 95){
  oops();
}

printf("Correct");
```

### Code Analysis

- It reads 5 characters from file, and then using fgetc it reads 6th character into c.
  If c == 32, it goes ahead. 

- Then, it reads 60 characters from file (from the starting as SEEK_SET is used), and then it reads 61st character of file into c.
  If c == 65, then we proceed.

- So, we know that if the file has space (ASCII: 32) at the 6th character, and 'A' (ASCII: 65) at the 61st character.

- Then, we have the flag.. And we can construct the sentence from this character position and the respective character.

- We have copied all those fseek lines from c file and then replaced all non-important characters with empty character in VSCode, leaving behind a comma-separated file format with position and character'S ASCII numbers.

- Now, we read the csv file in the `script.py` and construct a list of characters with the respective position.

- We then print that list of chars as a string, which is the actual flag `dctf{found}` written only using pipe, braces and dashes.

## Flag

`dctf{found}`
