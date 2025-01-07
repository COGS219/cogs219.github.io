#!/usr/bin/env python
# coding: utf-8

# Classes
# ===
# So far you've learned about Python's core data types: strings, numbers, lists, tuples, and dictionaries. In this section you will learn about the last major data structure, classes. Classes are unlike other data types, in that they are much more flexible. Classes allow you to define the information and behavior that characterize anything you want to model in your program. This notebook is a short introduction to classes. The first part gives soem generic examples. The second part give some examples of using classes in a context of a psych experiment.
# 
# There is a lot of new language that comes into play when you start learning about classes. If you are familiar with object-oriented programming (OOP) from  another language, this will be a quick read about how Python approaches OOP. If you are new to programming in general, there will be a lot of new ideas here. Just start reading, try out the examples on your own machine, and trust that it will start to make more sense as you work your way through.

# What are classes?
# ===
# Classes are a way of combining information and behavior. For example, think about what you'd need to do if you were creating a rocket ship in a game, or in a physics simulation. One of the first things you'd want to track are the x and y coordinates of the rocket. Here is what a simple rocket ship class looks like in code:

# In[1]:


class Rocket():   
     
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0


# One of the first things you do with a class is to define the **\__init\__()** method (`__` is a double underscore). The \_\_init\_\_() method sets the values for any parameters that need to be defined when an object is first created. The *self* part will be explained later; basically, it's a syntax that allows you to access a variable from anywhere else in the class.
# 
# The Rocket class stores two pieces of information so far, but it can't do anything. The first behavior to define is a core behavior of a rocket: moving up. Here is what that might look like in code:

# In[2]:


class Rocket():

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# The Rocket class can now store some information, and it can do something. But this code has not actually created a rocket yet. Here is how you actually make a rocket:

# In[3]:


class Rocket():
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# To actually *use* a class, you create a variable such as *`my_rocket`* like so:
# 
# ```python
# my_rocket = Rocket()
# ```
# 
# `my_rocket` is now an instance of the Rocket class. It has a copy of each of the class's variables and it can do any action that is defined for the class. In this case, you can see that the variable `my_rocket` is a Rocket object from the `__main__` program file, which is stored at a particular location in memory. Each instance is independent of another. Normally, changes you make to one will not affect other instances you've created. 
# 
# 

# In[1]:


class Rocket():
    # Rocket simulates a rocket ship for a game (or a physics simulation!).
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# To access an object's variables or methods, you give the name of the object and then use *dot notation* to access the variables and methods. So to get the y-value of `my_rocket` you use `my_rocket.y`. To use the move_up() method on my_rocket, you write `my_rocket.move_up()`.
# 
# 
# ```{note}
# You'll recognize this dot notation from things like random.shuffle() (shuffle is one of the methods possessed by objects instantiated by the Random class inside the random module contained in random.py). Whew..
# ```
# 
# Once you have a class defined, you can create as many objects from that class as you want. Each object is its own instance of that class, with its own separate variables. All of the objects are capable of the same behavior, but each object's particular actions do not affect any of the other objects. Here is how you might make a simple fleet of rockets:

# In[ ]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.

my_rockets = []
for _ in range(5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)



# In[ ]:


my_rockets[1]=my_rockets[2]


# In[ ]:


my_rockets[0].move_up()
my_rockets[2].move_up()


print(my_rockets[0].y)
print(my_rockets[1].y)
print(my_rockets[2].y)


print(my_rockets[0],my_rockets[1],my_rockets[2])


# You can see that each rocket is at a separate place in memory. 
# 
# :::{tip}
# You can use [list comprehension](https://psych750.github.io/notebooks/list_comprehension.html) to create your rocket fleet in one line:
# ```python
# my_rockets = [Rocket() for _ in range(5)]
# ```
# :::
# 

# You can prove that each rocket has its own x and y values by moving just one of the rockets:

# In[3]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [Rocket() for x in range(0,5)]

# Move the first rocket up.
my_rockets[0].move_up()

# Show that only the first rocket has moved.
for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)


# At this point it might seem like this is a lot of work for not much gain. But consider how you might create a rocket without using classes. You might store the x and y values in a dictionary. But what if you also want to score their current acceleration? Remaining fuel? More dictionaries? And let's say a person wants to call up all the information about a particular rocket? Do they need to remember what each of the dictionaries is called? What a mess! All of this messiness goes away once we use object oriented programming.

# Object-Oriented terminology
# ===
# Classes are part of a programming paradigm called **object-oriented programming**. Object-oriented programming, or OOP for short, focuses on building reusable blocks of code called classes. When you want to use a class in one of your programs, you make an **object** from that class, which is where the phrase "object-oriented" comes from. Python itself is not tied to object-oriented programming, but you will be using objects in most or all of your Python projects. In order to understand classes, you have to understand some of the language that is used in OOP.

# General terminology
# ---
# A **class** is a body of code that defines the **attributes** and **behaviors** required to accurately model something you need for your program. You can model something from the real world, such as a rocket ship or a guitar string, or you can model something from a virtual world such as a rocket in a game, or a set of physical laws for a game engine.
# 
# An **object** is a particular *instance* (a specific realization) of a class. An object has a certain set of values for all of the attributes (variables) in the class. You can have as many objects as you want for any one class. For example, Rect() is a class in PsychoPy. When you create a new rectangle by assigning Rect() to a variable, you are creating a new instance of the class -- the specific Rectangle object that is assigned to your variable.  
# 
# An **attribute** is a piece of information. In code, an attribute is just a variable that is part of a class.
# 
# A **behavior** is an action that is defined within a class. These are made up of **methods**. A method is just a function that is defined within a particular class.
# 
# 
# There is more to know, but this terminology is enough to get you started. It will make more sense as you see more examples, and start to use classes on your own.

# A closer look at the Rocket class
# ---
# Now that you have seen a simple example of a class, and have learned some basic OOP terminology, it will be helpful to take a closer look at the Rocket class.

# The `__init__()` method
# ---
# Here is the initial code block that defined the Rocket class:

# In[9]:


class Rocket():
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0


# The first line shows how a class is created in Python. The keyword **class** tells Python that you are about to define a class. The rules for naming a class are the same rules you learned about [naming variables](var_string_num.html#naming_rules), but there is a strong convention among Python programmers that classes should be named using CamelCase. If you are unfamiliar with CamelCase, it is a convention where each letter that starts a word is capitalized, with no underscores in the name. The name of the class is followed by a set of parentheses. These parentheses will be empty for now, but later they may contain a class upon which the new class is based.
# 
# It is good practice to write a comment at the beginning of your class, describing the class. There is a [more formal syntax](http://www.python.org/dev/peps/pep-0257/) for documenting your classes, but you can wait a little bit to get that formal. For now, just write a comment at the beginning of your class summarizing what you intend the class to do. Writing more formal documentation for your classes will be easy later if you start by writing simple comments now.
# 
# Function names that start and end with two underscores are special built-in functions that Python uses in certain ways. The \_\_init()\_\_ method is one of these special functions. It is called automatically when you create an object from your class. The \_\_init()\_\_ method lets you make sure that all relevant attributes are set to their proper values when an object is created from the class, before the object is used. In this case, The \_\_init\_\_() method initializes the x and y values of the Rocket to 0.
# 
# The **self** keyword often takes people a little while to understand. The word "self" refers to the current object that you are working with. When you are writing a class, it lets you refer to certain attributes from any other part of the class. Basically, all methods in a class need the *self* object as their first argument, so they can access any attribute that is part of the class.
# 
# Now let's take a closer look at a **method**.

# A simple method
# ---
# Here is the method that was defined for the Rocket class:

# In[10]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# Here we have 2 methods -- a default initialization method (what's called when you create a new instance of `Rocket()`) and a `move_up` method. A method is just a function that is part of a class. Since it is just a function, you can do anything with a method that you learned about with functions. You can accept [positional](more_functions.html#positional_arguments) arguments, [keyword](more_functions.html#keyword_arguments) arguments, an arbitrary [list of argument values](more_functions.html#arbitrary_sequence), an arbitrary [dictionary of arguments](more_functions.html#arbitrary_keyword_arguments), or any combination of these. Your arguments can return a value or a set of values if you want, or they can just do some work without returning any values.
# 
# Each method has to accept one argument by default, the value **self**. This is a reference to the particular object that is calling the method. This *self* argument gives you access to the calling object's attributes. In this example, the self argument is used to access a Rocket object's y-value. That value is increased by 1, every time the method move_up() is called by a particular Rocket object. This is probably still somewhat confusing, but it should start to make sense as you work through your own examples.
# 
# If you take a second look at what happens when a method is called, things might make a little more sense:

# In[11]:


class Rocket():
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# In this example, a Rocket object is created and stored in the variable my_rocket. After this object is created, its y value is printed. The value of the attribute *y* is accessed using dot notation. The phrase *my\_rocket.y* asks Python to return "the value of the variable y attached to the object my_rocket".
# 
# After the object my_rocket is created and its initial y-value is printed, the method move_up() is called. This tells Python to apply the method move_up() to the object my_rocket. Python finds the y-value associated with my_rocket and adds 1 to that value. This process is repeated several times, and you can see from the output that the y-value is in fact increasing.

# ```{tip}
# Want to remind yourself what methods are defined/available for use with an object? Use `help(your_object)`
# ```

# Making multiple objects from a class
# ---
# One of the goals of object-oriented programming is to create reusable code. Once you have written the code for a class, you can create as many objects from that class as you need. It is worth mentioning at this point that classes are usually saved in a separate file, and then imported into the program you are working on. So you can build a library of classes, and use those classes over and over again in different programs. Once you know a class works well, you can leave it alone and know that the objects you create in a new program are going to work as they always have.
# 
# You can see this "code reusability" already when the Rocket class is used to make more than one Rocket object. Here is the code that made a fleet of Rocket objects:

# In[12]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# If you are comfortable using list comprehensions, go ahead and use those as much as you can. I'd rather not assume at this point that everyone is comfortable with comprehensions, so I will use the slightly longer approach of declaring an empty list, and then using a for loop to fill that list. That can be done slightly more efficiently than the previous example, by eliminating the temporary variable *new\_rocket*:

# In[13]:


class Rocket():
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    my_rockets.append(Rocket())

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)


# What exactly happens in this for loop? The line *`my_rockets.append(Rocket())`* is executed 5 times. Each time, a new Rocket object is created and then added to the list `my_rockets`. The `__init__()` method is executed once for each of these objects, so each object gets its own x and y value. When a method is called on one of these objects, the *self* variable allows access to just that object's attributes, and ensures that modifying one object does not affect any of the other objecs that have been created from the class.
# 
# Each of these objects can be worked with individually. At this point we are ready to move on and see how to add more functionality to the Rocket class. We will work slowly, and give you the chance to start writing your own simple classes.

# A quick check-in
# ---
# If all of this makes sense, then the rest of your work with classes will involve learning a lot of details about how classes can be used in more flexible and powerful ways. If this does not make any sense, you could try a few different things:
# 
# - Reread the previous sections, and see if things start to make any more sense.
# - Type out these examples in your own editor, and run them. Try making some changes, and see what happens.
# - Try the next exercise, and see if it helps solidify some of the concepts you have been reading about.
# - Read on. The next sections are going to add more functionality to the Rocket class. These steps will involve rehashing some of what has already been covered, in a slightly different way.
# 
# Classes are a huge topic, and once you understand them you will probably use them for the rest of your life as a programmer. If you are brand new to this, be patient and trust that things will start to sink in.

# Refining the Rocket class
# ===
# The Rocket class so far is very simple. It can be made a little more interesting with some refinements to the \_\_init\_\_() method, and by the addition of some methods.

# Accepting parameters for the \_\_init\_\_() method
# ---
# The \_\_init\_\_() method is run automatically one time when you create a new object from a class. The \_\_init\_\_() method for the Rocket class so far is pretty simple:

# In[14]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# All the \_\_init\_\_() method does so far is set the x and y values for the rocket to 0. We can easily add a couple keyword arguments so that new rockets can be initialized at any position:

# In[15]:


class Rocket():
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# Now when you create a new Rocket object you have the choice of passing in arbitrary initial values for x and y:

# In[7]:


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1
        
# Make a series of rockets at different starting places.
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,10))
rockets.append(Rocket(100,0))

# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print(f"Rocket {index} is at {rocket.x}, {rocket.y}")


# Accepting parameters in a method
# ---
# The \_\_init\_\_ method is just a special method that serves a particular purpose, which is to help create new objects from a class. Any method in a class can accept parameters of any kind. With this in mind, the move_up() method can be made much more flexible. By accepting keyword arguments, the move_up() method can be rewritten as a more general move_rocket() method. This new method will allow the rocket to be moved any amount, in any direction:

# In[17]:


class Rocket():
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment


# The paremeters for the move() method are named x_increment and y_increment rather than x and y. It's good to emphasize that these are changes in the x and y position, not new values for the actual position of the rocket. By carefully choosing the right default values, we can define a meaningful default behavior. If someone calls the method move_rocket() with no parameters, the rocket will simply move up one unit in the y-direciton. Note that this method can be given negative values to move the rocket left or right:

# Adding a new method
# ---
# One of the strengths of object-oriented programming is the ability to closely model real-world phenomena by adding appropriate attributes and behaviors to classes. One of the jobs of a team piloting a rocket is to make sure the rocket does not get too close to any other rockets. Let's add a method that will report the distance from one rocket to any other rocket.
# 
# If you are not familiar with distance calculations, there is a fairly simple formula to tell the distance between two points if you know the x and y values of each point. This new method performs that calculation, and then returns the resulting distance.

# In[13]:


from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
# Make two rockets, at different places.
rocket_0 = Rocket()
rocket_1 = Rocket(10,5)

# Show the distance between them.
distance = rocket_0.get_distance(rocket_1)
print("The rockets are %f units apart." % distance)


# Hopefully these short refinements show that you can extend a class' attributes and behavior to model the phenomena you are interested in as closely as you want. The rocket could have a name, a crew capacity, a payload, a certain amount of fuel, and any number of other attributes. You could define any behavior you want for the rocket, including interactions with other rockets and launch facilities, gravitational fields, and whatever you need it to! There are techniques for managing these more complex interactions, but what you have just seen is the core of object-oriented programming.
# 
# At this point you should try your hand at writing some classes of your own. After trying some exercises, we will look at object inheritance, and then you will be ready to move on for now.

# Inheritance
# ===
# One of the most important goals of the object-oriented approach to programming is the creation of stable, reliable, reusable code. If you had to create a new class for every kind of object you wanted to model, you would hardly have any reusable code. In Python and any other language that supports OOP, one class can **inherit** from another class. This means you can base a new class on an existing class; the new class *inherits* all of the attributes and behavior of the class it is based on. A new class can override any undesirable attributes or behavior of the class it inherits from, and it can add any new attributes or behavior that are appropriate. The original class is called the **parent** class, and the new class is a **child** of the parent class. The parent class is also called a **superclass**, and the child class is also called a **subclass**.
# 
# The child class inherits all attributes and behavior from the parent class, but any attributes that are defined in the child class are not available to the parent class. This may be obvious to many people, but it is worth stating. This also means a child class can override behavior of the parent class. If a child class defines a method that also appears in the parent class, objects of the child class will use the new method rather than the parent class method.
# 
# To better understand inheritance, let's look at an example of a class that can be based on the Rocket class.

# The SpaceShuttle class
# ---
# If you wanted to model a space shuttle, you could write an entirely new class. But a space shuttle is just a special kind of rocket. Instead of writing an entirely new class, you can inherit all of the attributes and behavior of a Rocket, and then add a few appropriate attributes and behavior for a Shuttle.
# 
# One of the most significant characteristics of a space shuttle is that it can be reused. So the only difference we will add at this point is to record the number of flights the shutttle has completed. Everything else you need to know about a shuttle has already been coded into the Rocket class.
# 
# Here is what the Shuttle class looks like:

# In[14]:


from math import sqrt

class Rocket():
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
shuttle = Shuttle(10,0,3)
print(shuttle.flights_completed)


# When a new class is based on an existing class, you write the name of the parent class in parentheses when you define the new class:
# 
#     

# ```python
# class NewClass(ParentClass):
#     pass
# ```

# The \_\_init\_\_() function of the new class needs to call the \_\_init\_\_() function of the parent class. The \_\_init\_\_() function of the new class needs to accept all of the parameters required to build an object from the parent class, and these parameters need to be passed to the \_\_init\_\_() function of the parent class. The *super().\_\_init\_\_()* function takes care of this:

# In[ ]:


class NewClass(ParentClass):
    
    def __init__(self, arguments_new_class, arguments_parent_class):
        super().__init__(arguments_parent_class)
        # Code for initializing an object of the new class.


# The *super()* function passes the *self* argument to the parent class automatically. You could also do this by explicitly naming the parent class when you call the \_\_init\_\_() function, but you then have to include the *self* argument manually:

# In[ ]:


class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        Rocket.__init__(self, x, y)
        self.flights_completed = flights_completed


# This might seem a little easier to read, but it is preferable to use the *super()* syntax. When you use *super()*, you don't need to explicitly name the parent class, so your code is more resilient to later changes. As you learn more about classes, you will be able to write child classes that inherit from multiple parent classes, and the *super()* function will call the parent classes' \_\_init\_\_() functions for you, in one line. This explicit approach to calling the parent class' \_\_init\_\_() function is included so that you will be less confused if you see it in someone else's code.

# The output above shows that a new Shuttle object was created. This new Shuttle object can store the number of flights completed, but it also has all of the functionality of the Rocket class: it has a position that can be changed, and it can calculate the distance between itself and other rockets or shuttles. This can be demonstrated by creating several rockets and shuttles, and then finding the distance between one shuttle and all the other shuttles and rockets. This example uses a simple function called [randint](http://docs.python.org/2/library/random.html#random.randint), which generates a random integer between a lower and upper bound, to determine the position of each rocket and shuttle:

# In[5]:


from math import sqrt
from random import randint

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
        
# Create several shuttles and rockets, with random positions.
#  Shuttles have a random number of flights completed.
shuttles = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x, y))
    
# Show the number of flights completed for each shuttle.
for index, shuttle in enumerate(shuttles):
    print(f"Shuttle {index} has completed {shuttle.flights_completed} flights.")
    
print("\n")    
# Show the distance from the first shuttle to all other shuttles.
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print(f"The first shuttle is {distance} units away from shuttle {index}.")

print("\n")
# Show the distance from the first shuttle to all other rockets.
for index, rocket in enumerate(rockets):
    distance = first_shuttle.get_distance(rocket)
    print(f"The first shuttle is {distance} units away from rocket {index}.")


# Inheritance is a powerful feature of object-oriented programming. Using just what you have seen so far about classes, you can model an incredible variety of real-world and virtual phenomena with a high degree of accuracy. The code you write has the potential to be stable and reusable in a variety of applications.

# # Example of using a class in a Psychopy experiment
# 
# This section goes through a more practical example of using a class in an experiment. Let's say we want to make a moving circle that wiggles its way across a window. Here's some basic code to make this happen.

# ## A single moving circle

# In[1]:


import time
import random
import sys
import os
from math import *
from psychopy import visual, core, event

win = visual.Window([300,300],color="black", units='pix',allowGUI=True)
my_mouse = event.Mouse(win=win)

target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])
min_angle=-30
max_angle=30
prev_angle_to_deviate=0
new_cur_angle=0.0
inter_step_interval = 3.0

while True:
	core.wait(.02)
	target.draw()
	win.flip()

	cur_angle_to_deviate = prev_angle_to_deviate + random.randint(min_angle,max_angle); #calculate new angle
	cur_angle = cur_angle_to_deviate*pi/180.0; #convert to radians
	
	new_x_pos = inter_step_interval*cos(cur_angle)	
	new_y_pos = inter_step_interval*sin(cur_angle)
	
	target.setPos((new_x_pos,new_y_pos),'+')
	hit_boundary=False
	if (abs(target.pos[0]) > 150 or abs(target.pos[1]) > 150):
		hit_boundary=True
		new_x_pos =  inter_step_interval*cos(cur_angle-pi)
		new_y_pos =  inter_step_interval*sin(cur_angle-pi)

	prev_angle_to_deviate = cur_angle_to_deviate
	if hit_boundary:
		prev_angle_to_deviate -= 180
		prev_angle_to_deviate %= 360

	if event.getKeys(['space']):
		sys.exit()


# Let's extend this code so that when we click on the circle, it gets dimmer and moves slower.

# In[16]:


import time
import random
import sys
import os
from math import *
from psychopy import visual, core, event

win = visual.Window([350,350],color="black", units='pix',allowGUI=True)
my_mouse = event.Mouse(win=win)

target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])
min_angle=-30
max_angle=30
prev_angle_to_deviate=0
new_cur_angle=0.0
inter_step_interval = 2.0

while True:
	core.wait(.02)
	target.draw()
	win.flip()

	cur_angle_to_deviate = prev_angle_to_deviate + random.randint(min_angle,max_angle); #calculate new angle
	cur_angle = cur_angle_to_deviate*pi/180.0; #convert to radians
	
	new_x_pos = inter_step_interval*cos(cur_angle)	
	new_y_pos = inter_step_interval*sin(cur_angle)

	if my_mouse.isPressedIn(target):
		inter_step_interval *= .8
		target.opacity *= .9
	
	target.setPos((new_x_pos,new_y_pos),'+')
	hit_boundary=False
	if (abs(target.pos[0]) > 150 or abs(target.pos[1]) > 150):
		hit_boundary=True
		new_x_pos =  inter_step_interval*cos(cur_angle-pi)
		new_y_pos =  inter_step_interval*sin(cur_angle-pi)

	prev_angle_to_deviate = cur_angle_to_deviate
	if hit_boundary:
		prev_angle_to_deviate -= 180
		prev_angle_to_deviate %= 360

	if event.getKeys(['space']):
		sys.exit()


# ## More circles!
# But now suppose we want to have lots of moving circles that move independently of one another such that we can set some to move faster, have them be different colors, allow people to click on them independently, etc. This is the kind of situation where classes shine. 
# 
# The code below implements a `movingCircle` class. We then use it to make a bunch of individual circles and allow the user to click on them individually. Notice that it's not much longer than the code above. And if we want 10 circles, we just need to change `numCircles = 4` to `numCircles = 5`. Wizardry!

# In[1]:


import time
import random
import sys
import os
from math import sin, cos, pi
from psychopy import visual, core, event

win = visual.Window([300,300],color="black", units='pix',allowGUI=True)
my_mouse = event.Mouse(win=win)
num_cirlces = 4

class MovingCircle():
	
	def __init__(self,win):

		self.min_angle=-30
		self.max_angle=30
		self.prev_angle_to_deviate=0
		self.angle_moving_degrees=0.0
		self.inter_step_interval = 2.0
		self.target = visual.Circle(win,size=20,lineColor="black",fillColor=[1,1,1])

	def change_speed(self,delta_speed):
		self.inter_step_interval *= delta_speed

	def make_dimmer(self,percent):
		self.target.opacity *= percent

	def get_pos(self):
		return self.target.pos

	def target(self):
		return self.target

	def move_it(self):
		"gets new position and sets target to that position"
		cur_angle_to_deviate = self.prev_angle_to_deviate + random.randint(self.min_angle,self.max_angle); #calculate new angle
		cur_angle = cur_angle_to_deviate*pi/180.0; #convert to radians
		
		new_x_pos = self.inter_step_interval*cos(cur_angle)	
		new_y_pos = self.inter_step_interval*sin(cur_angle)
		
		self.target.setPos((new_x_pos,new_y_pos),'+')
		hit_boundary=False
		if (abs(self.target.pos[0]) > 150 or abs(self.target.pos[1]) > 150):
			hit_boundary=True
			new_x_pos =  self.inter_step_interval*cos(cur_angle-pi)
			new_y_pos =  self.inter_step_interval*sin(cur_angle-pi)

		self.prev_angle_to_deviate = cur_angle_to_deviate
		if hit_boundary:
			self.prev_angle_to_deviate -= 180
			self.prev_angle_to_deviate %= 360


circles = [MovingCircle(win) for _ in range(num_cirlces)]
while True:
	for cur_circle in circles:
		cur_circle.target.draw()
		if my_mouse.isPressedIn(cur_circle.target):
			print('clicked on a circle!' )
			cur_circle.change_speed(.8)
			cur_circle.make_dimmer(.9)

		cur_circle.move_it()
	core.wait(.05)
	win.flip()

	if event.getKeys(['space']):
		sys.exit()


# Make sure you understand what's happening here. Play around with the code. If you're confused, message on Slack.

# Modules and classes
# ===
# Now that you are starting to work with classes, your files are going to grow longer. This is good, because it means your programs are probably doing more interesting things. But it is bad, because longer files can be more difficult to work with. Python allows you to save your classes in another file and then import them into the program you are working on. This has the added advantage of isolating your classes into files that can be used in any number of different programs. As you use your classes repeatedly, the classes become more reliable and complete overall.

# Storing a single class in a module
# ---
# 
# When you save a class into a separate file, that file is called a **module**. You can have any number of classes in a single module. There are a number of ways you can then import the class you are interested in.
# 
# Start out by saving just the Rocket class into a file called *rocket.py*. Notice the naming convention being used here: the module is saved with a lowercase name, and the class starts with an uppercase letter. This convention is pretty important for a number of reasons, and it is a really good idea to follow the convention.

# In[ ]:


from math import sqrt

class Rocket():
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance


# Make a separate file called *rocket_game.py*. Or, if you want it to sound more scienc-ey, call it *rocket_simulation.py*. The exact name doesn't matter, but the convention does. Follow the convention by using a lowercase_underscore name for this file. This file will *use* the rocket class to do something.

# In[10]:


# Save as rocket_game.py
from rocket import Rocket

rocket = Rocket()
print(f"The rocket is at {rocket.x}, {rocket.y}")


# This is a really clean and uncluttered file. A rocket is now something you can define in your programs, without the details of the rocket's implementation cluttering up your file. You don't have to include all the class code for a rocket in each of your files that deals with rockets; the code defining rocket attributes and behavior lives in one file, and can be used anywhere.
# 
# The first line tells Python to look for a file called *rocket.py*. It looks for that file in the same directory as your current program. (You *can* put your classes in other directories, but it requires having it in the PYTHONPATH)
# 
# When Python finds the file *rocket.py*, it looks for a class called *Rocket*. When it finds that class, it imports that code into the current file, without you ever seeing that code. You are then free to use the class Rocket as you have seen it used in previous examples.

# Storing multiple classes in a module
# ---
# 
# A module is simply a file that contains one or more classes or functions, so the Shuttle class actually belongs in the rocket module as well:

# In[ ]:


# Save as rocket.py
from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    

class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


# Now you can import the Rocket and the Shuttle class, and use them both in a clean uncluttered program file:

# In[11]:


# Save as rocket_game.py
from rocket import Rocket, Shuttle

rocket = Rocket()
print(f"The rocket is at {rocket.x}, {rocket.y}")

shuttle = Shuttle()
print(f"\nThe shuttle is at {shuttle.x}, {shuttle.y}")

print(f"\nThe shuttle has completed {shuttle.flights_completed} flights.")


# The first line tells Python to import both the *Rocket* and the *Shuttle* classes from the *rocket* module. You don't have to import every class in a module; you can pick and choose the classes you care to use, and Python will only spend time processing those particular classes.

# A number of ways to import modules and classes
# ---
# There are several ways to import modules and classes, and each has its own merits.

# ### import *module_name*
# 
# The syntax for importing classes that was just shown:
# 
# ```python
# from module_name import ClassName
# ```
# 
# is straightforward, and is commonly used. It allows you to use the class names directly in your program, so you have very clean and readable code. This can be a problem, however, if the names of the classes you are importing conflict with names that have already been used in your program This is unlikely to happen in short programs like those in the examples, but becomes increasingly likely as your codebase grows. It's also an issue if you are sharing your code. Maybe you take pains to ensure that a class name doesn't conflict with names used in *your* code, but can you guarantee that it won't happen when others use your code? So, you can also import the module itself:

# In[ ]:


# Save as rocket_game.py
import rocket

rocket_0 = rocket.Rocket()
print(f"The rocket is at {rocket_0.x}, {rocket_0.y}")
print(f"Shuttle {index} has completed {shuttle.flights_completed} flights.")

shuttle_0 = rocket.Shuttle()
print(f"The shuttle is at {shuttle_0.x}, {shuttle_0.y}")
print(f"Shuttle has completed {shuttle_0.flights_completed} flights.")


# The general syntax for import is:
# 
# ```python
# import module_name
# ```
# 
# After this, classes are accessed using the dot notation:
# 
# ```python
# module_name.ClassName
# ```
#     
# This prevents some name conflicts. If you were reading carefully however, you might have noticed that the variable name *rocket* in the previous example had to be changed because it has the same name as the module itself. This is not good, because in a longer program that could mean a lot of renaming.

# ### import *module_name* as *local_module_name*
# 
# There is another syntax for imports that is quite useful:
# 
# ```python
# import module_name as local_module_name
# ```
# 
# When you are importing a module into one of your projects, you are free to choose any name you want for the module in your project. So the last example could be rewritten in a way that the variable name *rocket* would not need to be changed:

# In[12]:


# Save as rocket_game.py
import rocket as rocket_module

rocket_0 = rocket_module.Rocket()
print(f"The rocket is at {rocket_0.x}, {rocket_0.y}")
print(f"Shuttle {index} has completed {shuttle.flights_completed} flights.")

shuttle_0 = rocket_module.Shuttle()
print(f"The shuttle is at {shuttle_0.x}, {shuttle_0.y}")
print(f"Shuttle has completed {shuttle_0.flights_completed} flights.")


# This approach is often used to shorten the name of the module, so you don't have to type a long module name before each class name that you want to use. But it is easy to shorten a name so much that you force people reading your code to scroll to the top of your file and see what the shortened name stands for. In this example,
# 
# ```python
# import rocket as rocket_module
# ```
# 
# leads to much more readable code than something like:
# 
# ```python
# import rocket as r
# ```
# 

# ### from *module_name* import *
# There is one more import syntax that you should be aware of, but Python gurus advise against using. This syntax imports all of the available classes and functions in a module:
# 
# ```python
# from module_name import *
# ```
# 
# This isn't recommended for a couple reasons. First, you don't know what all the names of the classes and functions in a module are. If you accidentally give one of your variables the same name as a name from the module, you will have naming conflicts. Second, you may be importing way more code into your program than you need.
# 
# If you really need all the functions and classes from a module, just import the module and use the `module_name.ClassName` syntax in your program.
# 
# You will get a better sense of how to write imports as you read more Python code and as you write and share some of your own code.

# A module of functions
# ---
# You can use modules to store a set of functions you want available in different programs as well, even if those functions are not attached to any one class. To do this, you save the functions into a file, and then import that file just as you saw in the last section. Here is a really simple example; save this is *multiplying.py*:

# In[ ]:


# Save as multiplying.py
def double(x):
    return 2*x

def triple(x):
    return 3*x

def quadruple(x):
    return 4*x


# Now you can import the file *multiplying.py*, and use these functions. Using the `from module_name import function_name` syntax:

# In[ ]:


from multiplying import double, triple, quadruple

print(double(5))
print(triple(5))
print(quadruple(5))


# Using the `import module_name` syntax:

# In[ ]:


import multiplying

print(multiplying.double(5))
print(multiplying.triple(5))
print(multiplying.quadruple(5))


# Using the `import module_name as local_module_name` syntax:

# In[ ]:


import multiplying as m

print(m.double(5))
print(m.triple(5))
print(m.quadruple(5))


# Using the `from module_name import *` syntax:

# In[ ]:


from multiplying import *

print(double(5))
print(triple(5))
print(quadruple(5))

