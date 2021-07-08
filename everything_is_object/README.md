#[Everything is an object](https://web.archive.org/web/20151210024637/https://mail.python.org/pipermail/python-list/2015-June/691689.html)

1. In Python, "everything is an object" (that is, all values are objects)
is because Python does not include any primitive unboxed values. Anything
which can be used as a value (int, str, float, functions, modules, etc) are
implemented as objects.
   
2. Python **also** has metaclasses. This does not follow from the above --
they are independent statements about the language. We could, if we want,
invent new languages:

    - one where everything is an object, just like Python, but lacking
metaclasses;

    - one which has metaclasses, just like Python, but not everything is an
object;

    - and one which *neither* has metaclasses, *nor* everything is an object. 
    
   (Java is an example of the third one)

## More details

Various kinds of things in a programming language:

1. **Simple** machine types, like *bytes*, *integers*, *floats*. These have no
internal structure, apart from individual bits. These are sometimes
called "machine primitives", and are the sorts of things you work with in
assembly language.

2. **Compound** or structured machine types. These are made up of one or more
simple machine type, and include things like C structs and arrays.

3. **Objects**, which are a more complex kind of compound type. More
importantly, objects involve a way of thinking about programming: some form
of inheritance, for example. Physically, an object is just a struct. But
it's a struct with a specific kind of meaning to the programming language,
which allows the language to provide inheritance, runtime types, and
various other goodies involved in Object Oriented Programming.
   

A language can choose to allow any or these, or all of these:

- **assembly** languages typically only support the most primitive, **simple**
machine types;

- languages like **C and Pascal** supports only **simple** and **compound** machine
types;

- some languages include **both simple** machine primitives **and objects**, such as
**Java and Javascript**;

- other languages don't offer any direct access to machine primitives, so
**all values are objects**, for example **Python and Ruby**.
  

To give a concrete example, consider a language with an "integer" type.
**In C, an integer will be a machine primitive**, a single, unstructured chunk of
memory with typically 32 bits, and that's all there is to it.
**In Python, an integer will be an object**, a large block of *structured* memory, typically
over 100 bits long, and different parts of that structure are used
internally to the interpreter.


###Whether or not classes are values?

In some languages, classes are *not* values: you cannot pass a class as argument to a
function, or assign it to a variable.
In languages like these, classes are not things (values), so "everything is an object" remains true even though
classes are not objects. Java is an example of that.

In Python, **classes *are* variables**. So we could have:

"In Python, everything is an object, or a class";

or

"In Python, everything is an object, including classes".


The second is true: **classes themselves are objects**.

### Does the language provide metaclasses?

Python does. Ruby, which is otherwise very similar to Python, does not:

In Python, everything is an object, and we have metaclasses.

In Ruby, everything is an object, but we don't have metaclasses.
