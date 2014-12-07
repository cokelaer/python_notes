CGI module
#############

:Status: in progress

The :mod:`cgi` module contains suprinsingly functions to build up CGI script. 
GI script can be written to handle many tasks such as user input form, databases requests and other programs available on the server side. 

Quick start
=============

A simple CGI script looks like::

    #!/usr/bin/python
    print "Content-Type: text/plain\n\n"
    print "Whatever HTML code would now work"

The second line is compulsary!! When you write a new script, consider adding these lines::

    import cgitb
    cgitb.enable()

This activates a handler that will display detailed reports in the Web browser if any errors occur. 

Forms
=========

The :func:`cgi.FieldStorage` class can be used to manipulate forms (and input from the user). The following code checks that the fields name and addr are both set to a non-empty string::

    form = cgi.FieldStorage()
    if "name" not in form or "addr" not in form:
        print "<H1>Error</H1>"
        print  "Please fill in the name and email fields."
        return
    print "<p>name:", form["login"].value
    print "<p>pwd:", form["email"].value
    ...further form processing here...


The HTML code would be something like::

    <form method="post" action="validate.py">
    <p>login:<input type="text" name="login", value=""></p>
    <p>login:<input type="text" name="email", value=""></p>
    <p>password:<input type="password" name="password", value=""></p>
    <input type="submit" value="SUBMIT">
    </form>

The forms in CGI script constitute a language by itself and is not covered here.

todo
=====
::

    cgi.FormContent            cgi.parse
    cgi.ForContentDict        cgi.parse_header
    cgi.InterpFormContentDict  cgi.parse_multipart
    cgi.MiniFieldStorage       cgi.parse_qs
    cgi.StringIO               cgi.parse_qsl
    cgi.SvFormContentDict      cgi.print_arguments
    cgi.UserDict               cgi.print_directory
    cgi.attrgetter             cgi.print_environ
    cgi.catch_warnings         cgi.print_environ_usage
    cgi.dolog                  cgi.print_exception
    cgi.escape                 cgi.print_form
    cgi.filterwarnings         cgi.rfc822
    cgi.initlog                cgi.sys
    cgi.log                    cgi.test
    cgi.logfile                cgi.urllib
    cgi.logfp                  cgi.urlparse
    cgi.maxlen                 cgi.valid_boundary
    cgi.mimetools              cgi.warn
    cgi.nolog                  


:References: http://docs.python.org/2/library/cgi.html
