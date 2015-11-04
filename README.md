s3arch
======

A search engines hacking tool

[http://maurosoria.blogspot.com/2014/09/s3arch-v01.html](http://maurosoria.blogspot.com/2014/09/s3arch-v01.html)

#### s3arch v0.1

This time I want to tell you about a small tool I've coded last year, but never talked about here.

It's name is s3arch, and it's a Google&Bing hacking tool. I coded to automate the process of searching with Google and Bing but without repeating GET values. For example, suppose the following dork:

```
site:www.example.com ext:php
```

Now, suppose Google returns the following results:

```
www.example.com/index.php?id=1
www.example.com/index.php?id=2
www.example.com/index.php?id=3
.....
www.example.com/index.php?id=31337
www.example.com/index.php?category=1
www.example.com/index.php?category=2
www.example.com/index.php?section=contact
```

Launch the application with the following arguments:

```
python3 s3arch --query "site:www.example.com ext:php" --only-parameters --google
```

The ouput of s3arch would be:
```
www.example.com/index.php?id=1
www.example.com/index.php?category=1
www.example.com/index.php?section=contact
```

Easy, right? It's very helpful when looking for parameterized parts of Web Applications and search engines returns lots of results with the same parameters.

Now imagine you are facing a PHP WebApp that has magic_quotes enabled. There are more chances to find vulnerable parameters that are meant to receive only numbers. We can use **"-n|--numeric-values"** for this. Let's back again to the previous example but now with -n argument:
```
python3 s3arch --query "site:www.example.com ext:php" --only-parameters --google --numeric
```
The ouput would be:
```
www.example.com/index.php?id=1
www.example.com/index.php?category=1
```

Notice that "www.example.com/index.php?section=contact" wouldn't be printed.

You have two modes, --query and --site. The first one, just searches with the passed argument. The sencond one, **--site**, makes use of **"site:"** operator. So, the next line is equivalent to the previous example:
```
python3 s3arch --site "www.example.com" --custom "ext:php" --only-parameters --google --numeric
```
It's important to know that we shouldn't write **--site "www.example.com ext:php"**, you to should use **--custom** argument to accomplish the desired behaviour. Why? Actually, you could do that way too now, but I'm planning to add more features in the future that would make more use of --site argument.

You can get s3arch from github:
[https://github.com/maurosoria/s3arch](https://github.com/maurosoria/s3arch)

If you have any suggestion, please let me know :)


