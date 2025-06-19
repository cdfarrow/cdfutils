# cdfutils

_A library of miscellaneous utility functions and classes that I've created for my projects._

## Config

+ ConfigStore: A generic configuration class that persists values in a text file.

## DotNet
_Some general helper classes for use with .NET Windows.Forms_

+ CustomMainMenu: Builds a full MenuStrip from a supplied configuration.
+ CustomToolBar: Builds a ToolStrip from a supplied configuration.
+ SimpleContextMenu: Builds a ContextMenuStrip from a supplied configuration.

Note: these are all breaking changes from 1.0.8; These now use the newer .NET classes instead of MainMenu, ToolBar and ContextMenu, and they need different handling in the calling application. This [article](https://www.codeproject.com/Articles/12953/Upgrading-from-MainMenu-and-ToolBar-to-MenuStrip-a) gives some (although not all) of the details.

## Textfile
_Utility functions for reading from text files_

+ randomLine(): Returns a random line from a file.
+ randomSection(): Returns a random section (delimited by lines starting with #) from a file.
