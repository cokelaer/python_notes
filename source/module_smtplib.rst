smtplib module
#################

:Status: in progress


The smtplib module takes its name from SMTP, the Simple Mail Transport Protocol. 
That’s the protocol for sending Internet mail. 

Quick start
=============

If you are running a mail server, this code allows you to send a mail::

     >>> import smtplib
     >>> from = 'sender@example.com'
     >>> to = 'target@example.com'
     >>> message = 'Subject:testing smtplib\n\nBody of the message'
     >>> server = smtplib.SMTP(“localhost”, 25)
     >>> server.sendmail(from, to, message)
     {}


RFC2822 compliant message
==============================

.. todo:: check and chcnage content of this example

::

    >>> from email import Message
    >>> from email.Message import Message
    >>> message = Message()
    >>> message['Subject'] = 'Test'
    >>> message.set_payload(‘This is the body of the message’)
    >>> print str(message)
    From nobody Fri Mar 25 20:08:22 2005
    Subject: Test

    This is the body of the message


todo
=====
::

    smtplib.CRLF                    
    smtplib.LMTP                 
    smtplib.LMTP_PORT               
    smtplib.OLDSTYLE_AUTH         
    smtplib.SMTPAuthenticationError  
    smtplib.SMTPConnectError      
    smtplib.SMTPDataError     
    smtplib.SMTPException      
    smtplib.SMTPHeloError        
    smtplib.SMTPRecipientsRefused    
    smtplib.SMTPResponseException    
    smtplib.SMTPSenderRefused        
    smtplib.SMTPServerDisconnected   
    smtplib.SMTP_PORT                
    smtplib.SMTP_SSL                 smtplib.base64
    smtplib.SMTP_SSL_PORT            smtplib.email
    smtplib.SSLFakeFile              smtplib.encode_base64
    smtplib.hmac
    smtplib.quoteaddr
    smtplib.quotedata
    smtplib.re
    smtplib.socket
    smtplib.ssl
    smtplib.stderr

.. seealso:: :mod:`base64` and :mod:`quopri` for encoding/decoding. 
.. seealso:: :mod:`email` and :mod:`mailbox` to receive emails
.. seealso:: :mod:`poplib` and :mod:`imaplib` for fetching mails.



