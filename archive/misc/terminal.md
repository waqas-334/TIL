# Listing things I learned about terminal

`16th May 2024`
I learned about `find` command. So here is how it works:

`find` is followed by <path> where to search, then you can add type by `-type` flag and argument can be `d` for directory, `f` for any file, and you can add `-name` flag to pass the name of file/directory that you are searching. If you want it to be case insensitive then you can use `-iname` flag instead.

You can also pass some regex if you don't know the file name. Like find me all the text file that start with s and end with b. Command would be:

> find ~ -type f -iname "s*b.txt"

