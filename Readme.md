# DummySMTPD

A simple and quite dummy smtp server which store every received email to a file.

Files are stored as-is in the current directory by default.

Type `python dummysmtpd.py --help` for more options.


## Example

Type `python dummysmtpd.py` to start the server.

In another terminal, connect to the server using nc and type the following `<`-prefixed lines:
```
$ nc localhost 1025
> 220 localhost Python SMTP proxy version 0.2
< HELO localhost^M
> 250 localhost
< MAIL FROM: nicolas@test.com^M
> 250 Ok
< RCPT TO: test@test.com^M
> 250 Ok
< DATA^M
> 354 End data with <CR><LF>.<CR><LF>
< Hello World!^M
< .^M
> 250 Ok
< QUIT^M

$
```
Note: Press Ctrl-V, then Enter to output a CRLF sequence, (^M in the example).
