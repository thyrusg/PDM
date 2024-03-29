:Author:
	Thyrus Gorges

:Version: 0.1dev as of 2012/07/01

=============
Inner Working
=============

Part 1 - Find PDFs
-------------------

Finding PDFs will be done by findPDF.py. Finding PDFs will only occur when pdm 
is used with the *import* argument. 

Import argument
+++++++++++++++++

The import argument only requires one argument, the location of your PDF files.
PDM will check if the directory exists first, then it will check if it's
already in the provided directory. Once it passes both checks PDM will ask the
user whether they wish to reorganize the books in their current directory or
would they like a new directory created for the PDFs. If they select a new
directory the folder will be placed in their /home/user/ directory and will be
called PDM. If they chose to reorganize the current folder, the only thing
effected will be names of the PDFs. 

Part 2 - Obtain PDF Info
-------------------------

Basically, PDM will parse the PDF for the PDFs title, the author, and ISBN.
PDF parsing will be done by an external library. After it obtains the ISBN, 
if avaliable, PDM will send a request to some api where it can request info
using the ISBN. Then PDM will parse the result & store the data in a database.

Possible Resources:
- Amazon (Do they provide a search api ?)
- Google Books
- Library Thing
- Good Reads
- Open Library Books
- isbnDB


Part 3 - Folder Structure
--------------------------

This part is pretty simple. Folder structure only applies if the user chose to
reorganize their collection into the newly created PDM folder from earlier.


Part 4 - PDF Naming Structure
------------------------------