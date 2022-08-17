# Web Servers and WSGI

## Learning Goals

- Describe the components of a web application framework.
- Build and run a Flask application on your computer.
- Manipulate and test the structure of a request object.

***

## Key Vocab

- **Web Framework**: software that is designed to support the development of
  web applications. Web frameworks provide built-in tools for generating web
  servers, turning Python objects into HTML, and more.
- **Extension**: a package or module that adds functionality to a Flask
  application that it does not have by default.
- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided
  by a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made
  over the internet.
- **Web Server Gateway Interface (WSGI)**: an interface between web servers
  and applications.
- **Template Engine**: software that takes in strings with tokenized
  values, replacing the tokens with their values as output in a web browser.

***

## Introduction

Web servers are the software and hardware that allow users to access resources
through the internet. While there are a whole range of jobs that are dedicated
to creating and maintaining servers, building a basic server for yourself is
actually very simple:

```console
$ python -m http.server
# => Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

Navigate to `localhost:8000` in your browser and you should see the following:

![http.server image](image.html "http.server web page")

`http.server` is a module in Python's standard library that creates a simple
webpage that can respond to clients through an open URL and port. Run from the
command line, it creates a navigable directory structure with URLs mimicking the
path for each resource. Clicking on a directory shows its contents, and clicking
on a file downloads it to your computer.

***

## Lesson Section

Lorem ipsum dolor sit amet. Ut velit fugit et porro voluptas quia sequi quo
libero autem qui similique placeat eum velit autem aut repellendus quia. Et
Quis magni ut fugit obcaecati in expedita fugiat est iste rerum qui ipsam
ducimus et quaerat maxime sit eaque minus. Est molestias voluptatem et nostrum
recusandae qui incidunt Quis 33 ipsum perferendis sed similique architecto.

```py
# python code block
print("statement")
# => statement
```

```js
// javascript code block
console.log("use these for comparisons between languages.")
// => use these for comparisons between languages.
```

```console
echo "bash/zshell statement"
# => bash/zshell statement
```

<details>
  <summary>
    <em>Check for understanding text goes here! <code>Code statements go here.</code></em>
  </summary>

  <h3>Answer.</h3>
  <p>Elaboration on answer.</p>
</details>
<br/>

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Instructions begin here:

- Make sure to specify any class, method, variable, module, package names
  that `pytest` will check for.
- Any other instructions go here.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Conclusion summary paragraph. Include common misconceptions and what students
will be able to do moving forward.

***

## Resources

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[reused resource]: https://docs.python.org/3/
