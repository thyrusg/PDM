PDM - A CLI tool for managing your extensive PDF collection.

This is a list of the possible commands::

    pdm import </your/directory/here>

Import all PDFs located inside the home folder into a new folder or reorganize
in PDFs current folder:: 

   pdm stat
   Total PDFs: 56	Size: 2.4GB	Authors: 42

Returns stats about your PDF collection. Stats include number of PDFs, total PDFs size, and etc::

   pdm search <title> <author> <isbn>

Search for a specific title, author, or ISBN::

   pdm remove <pdf>
   
Delete the PDF. 