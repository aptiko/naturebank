NatureBank
==========

Version 1.0 (2015-10-01)

NatureBank is a database for managing data on biotopes and landscapes
as well as species of the flora and fauna. It can be accessed through
a web application powered by Django. This is a Greek version of NatureBank
i.e. all textual information (web pages, names, descriptions etc.) are in
Greek language.


Requirements
------------
 * Python v.2.7
 * PostreSQL v.9.0
 * PostGIS v.2.1

Additional requirements related with Django and its applications are
documented in file requirements.txt.
NatureBank has been successfully tested with PostreSQL v.9.0,
spatially enabled with PostGIS v.2.1. Other versions of the above
software or other spatially enabled databases may work as well.


Installation
------------
 * Install Python, PostreSQL and PostGIS
 * Install Django and dependencies
 * Create a database user and a database supporting UTF8
 * Populate the database (dump data file will be prepared)
 * Create and configure a file /filotis/settings/local.py same as
   /filotis/settings/development.py
 * Configure your web server

(to be completed)


License
-------
    NatureBank is a database for managing data on  biotopes and
    landscapes as well as species of the flora and fauna.
    Copyright (C) 2005-2015 National Technical University of Athens

    NatureBank is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public
    License along with this program. If not, see
    <http://www.gnu.org/licenses/>.

NatureBank is a reengineered, generalized version of Filotis, which is
Copyright (C) 2005-2015 National Technical University of Athens.
Filotis is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

All additional 3rd party software provided with this release and/or used
by NatureBank are AGPLv3 compatible as their licenses ensure the freedoms
to run, study, share (copy), and modify the software. Additionally, some
of them are copylefted.


Acknowledgements
----------------
NatureBank is based on Filotis developed between 2005-2015 by the
National Technical University of Athens.
Main authors of Filotis are Anthony Christophides and Stefanos Kozanis.
Theodore Kargas was the main author of the initial version of Filotis.
Authors of NatureBank are Antonis Christophides, George Karavokiros and
Antonis Koukouvinos.
