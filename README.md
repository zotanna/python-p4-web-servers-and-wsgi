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

![http.server image](
https://curriculum-content.s3.amazonaws.com/python/python_httpserver_screenshot.png
"http.server web page")

`http.server` is a module in Python's standard library that creates a simple
webpage that can respond to clients through an open URL and port. Run from the
command line, it creates a navigable directory structure with URLs mimicking the
path for each resource. Clicking on a directory shows its contents, and clicking
on a file downloads it to your computer.

### Ports

Notice the "8000" after your hostname when you run `http.server`? This is the
**port** that allows you to access the resources that your server is serving.
Ports are a networking concept that you won't use a whole lot in full-stack web
development, but you'll see them whenever you run a server.

You can think of ports like _extensions_ on phone numbers. If you call your
doctor's office, you're accessing the practice with the phone number itself
(this is like the URL), but you're reaching the specific doctor through the
extension.

Some ports are explicit and specific- you can't access your `http.server`
resource without including `:8000` at the end of your URL. Others are implied
by the protocol used to connect to the resource. HTTP is always `:80`, HTTPS is
always `:443`, FTP (**F**ile **T**ransfer **P**rotocol) uses `:20` and `:21`,
etc.

> NOTE: If you see a lock next to the URL (or `https://`), it means that you're
> accessing a resource protected by Transport Layer Security, or TLS. Though it
> doesn't show `:443`, this is the port that you're using. You should always
> check that a website is protected before entering any personal information!

Running your own server, you can choose any port between 1024 and 65,535 to
make your application accessible in the browser. `http.server` defaults to 8000
as seen above, and Flask applications default to port 5000. There isn't
typically a need to specify a port, but if you're running two servers on your
computer at once, you will need to set the second port to another value.

***

## 

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
