# LaTeX Project Repository

## Purpose

The purpose of this project is to create a version
controlled repository for our project files.

## Contents

This repository contains an /img/ folder for 
embedding images into our reports; a /tex/ folder
for allowing us to compose seperate chapters 
independently and then combine them later; and
then a whole bunch of random files dumped into the root.

## How to Use

LaTeX is a markup language which uses a different syntax
than HTML/CSS but fundamentally works in much the same way.

TEX files are analogous to HTML files, and STY files are
analogous to CSS files. I've predefined most of the 
interesting bits of the document construction in the
mystyle.sty file and the "parent" file, in this case
report1part1.tex. So you shouldn't need to worry about
having to define document classes, formatting of chapter heads,
or whatnot. And if you need a library, you should probably just
include it into the mystyle.sty file to keep things clean.

We're going to use on master and multiple children files for the report.
LaTeX allows you to include other TEX files into a master file,
incorporating whatever basic formatting is within. So we're going to
use the master file "reportXpartY.tex" as the master file for each
report when we submit, and we'll just include the relevant children.

Each person should take a stab at editing one child file and
editing it etc. and we'll take a look at the finished whole later.
