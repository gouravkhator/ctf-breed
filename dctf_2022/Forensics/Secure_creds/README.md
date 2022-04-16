# Forensics | Secure Creds

## Work Tried

- I unzipped the given zip file using `unzip -e lsass.zip` and that gave a `lsass.DMP` file, which is provided in `work_files` folder.
- I used `strings lsass.DMP` which spit some text like `strstr`, `strcmp`, and many other C functions.
- I tried using `Ghidra` to decompile this, but it is a `.DMP` file and I have to research how to get data from this file.
