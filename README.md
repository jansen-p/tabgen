# chord_gen

Converts the chords specified in a file called 'notes' to pdf files.

The 'notes' file might look as follows:

```
A,x02220
A7,002020
Csus4,x3301x
...
```

Run python chord_gen.py --help to check available options. Don't forget to set the output directory (end of the script).

---

# tabs_gen

Example: run ` python tabs_gen.py DustintheWind-Kansas`.

This creates an image containing the tabs specified in the file DustintheWind-Kansas.

### source-file structure

1st line: Title. This can be any string

Following lines: one of the following

* a,b,c,d,e,f 
	a...f can be either a string, or nothing. 
	Example: ,,3p,,2,1 (3p might represent a pull-off)
* a,b,c,d,e,f # comment
	Same as above, 'comment' is printed above this tab-column
* empty line: this will create a line break
* '|' or '||': creates a vertical line/separator
* ':x||': can be used to indicate how often a section is meant to be repeated (during playing), e.g. 'x3||' as in the sample file