Working with XML
####################


XML is a powerful, flexible, open-standards-based method of data storage.
Its format makes it human readable, while remaining easy to parse for programs. It is a simple hierarchical markup language. Tags are used to mark off sections of content and attributes are used to add metadata to the content.

Example::


    <?xml version="1.0"?>
    <books>
        <book id="1">
            <title>Les miserables</title>
            <author>Victor Hugo</author>
        </book>
    </books>

One problem with semantic markup is the possibility for confusion. What is the meaning of title (book title or author title?). This is why namespaces have been introduced. A namespace provides a frame of reference for tags and has a unique ID (a URL) and a prefix to
apply to tags from that namespace. In the following example, the URL is  http://server.domain.tld/NameSpaces/Books and with a prefix of book: . The document would look like this::

     <?xml version=”1.0”?>
     <books:books owner='John Q. Reader' xmlns:lib=”http://server.domain.tld/NameSpaces/Library”>
         <books:book id="1">
            <books:title>Les miserables</title>
            <books:author>Victor Hugo</author>
        </books:book>
     </books:books>


.. todo:: xslt, schema, xpath, ... dtd

Quick Start
=============

from htmllib import htmlparser 


see [Noton]_ chapter 15 
