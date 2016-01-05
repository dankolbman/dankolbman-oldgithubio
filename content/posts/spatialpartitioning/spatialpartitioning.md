title: Spatial Hashing for Broad Phase Collision Tests
author: Dan Kolbman
date: 2014-07-19
status: draft

### Core Data Structures

There are three arrays to keep track of the objects and cells. First is the
_Object Array_. This is an array of neatly defined objects or structs with 
parameters for id, position, and anything else that might be important in the 
simulation. These objects will be the general representations that should be
easy and quick to work with inside the physical enivironment, unlike the
following two arrays. The next array that will need to be kept is the _Object 
List_ array. This is a pure data array that will hold values of a fundamental 
type (probably Ints) for the Object Id, followed a pass number for each cell the
object occupies (Up to 2^d - 1 cells). The last array is the _Cell ID_ array,
also for low level types. It holds, for every object, the ID of the Home Cell
followed by the IDs of the Home Cell`s Phantom Cells.

All of this info could be compactly stored into one list by utilizing objects
and/or fundamental data structures, however, because all of this information
needs to be passed onto the GPU, it`s important to minimize memory transfer.
Stucts and objects can be a little more costly in terms of overhead, but more
importantly, some GPUs might have different/no support for more complex data
structures.

### Generating Cell Object List and Cell ID Arrays



The general process of building the cell list is as follows:

