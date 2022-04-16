# Web | Sql Tutor

The files in `work_files` directory is downloaded from the website. The website has an input field and a drop down menu.

The drop-down menu has multiple sql statements with dashes in them. And it will be filled by the text entered in that input.

When we try to give any SQL injection text in that input field, it validates in the server side for `select` or `union` or `=` or other texts, and throws an alert on client end.

## Code Analysis

### Requests

- `POST /verify_and_sign_text`: Sends our inputed text as base64 encoded and `alg` as `sha1`. This returns a signature from server end if the text is not having SQL injection.
- `POST /execute`: Takes in signature, text and then returns the results. It validates in server end if the text passed in this request has the same `sha1` signature as the one passed in this request to `/execute`.


