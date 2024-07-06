# AlgorithmicTrading
New project for algorithmic trading practice and concept research


# Research 
_04/07/2024_

From the research I did on the job market, I learned that C#, C++, and Python are the most commonly used languages for algorithmic trading. While Java, Rust, and Go were mentioned, they were barely used.

**Mentions in the Job postings**
* GO 3%
* C# 16%
* C++ 38%
* Python 33%
* R 5%
* Java 5%

Note that when C++ is mentioned, Python is also likely to be mentioned, or all three top languages C#, C++, and Python 
are mentioned together. So it would make most sense to choose one of the top 3 languages. I have experience with all of 
them, and I believe C# and Python might be best for this project. Therefore, it would make the most sense to choose one 
of these top three languages. 

_05/07/2024_

Upon further investigation, I decided to use Python because C# is very similar to Java in how both languages are used. 
This means Python would allow me to be more flexible later on when I need to move from Java to other language. Moreover,
the different trading platforms I check all of them offer Python integration while not all of them offer C#.

# Release/Deploy

Like any program, it needs to be installed or deployed somewhere to be used. The next section will focus on how to 
release and deploy a Python application. I will explore how to build and deploy it using a Docker container.

I learned more about dependency management in Python and found two ways to manage dependencies: using pip with a
requirements file, and using Pipenv with a Pipfile. Both files act like build.gradle in Java. The main difference is 
that Pipenv allows you to set up a specific environment each time, ensuring consistency. In contrast, with the
requirements.txt method, some dependencies can be updated, potentially leading to compatibility issues.
https://python.land/deployment/containerize-your-project

I had some issues debugging, as the error messages are not as informative as Java's, but I managed to dockerize and run 
a simple Flask application following this resource. Currently, I am looking for a good way to run it with open ports 
available to everyone. I could create a CMD script to run the required commands sequentially, but I will do some
research before committing.

_06/07/2024_

Seems like docker compose will do even-though it is not made for this purpose, but that is okay as later on I will be adding 
a DB and would like run everything with single command. Seems like I will need to create a new directory or repository for 
separation of concerns.

Managed to run CI for automated tests, I could be doing CD by building docker image and uploading it, but I rather do some 
coding instead of the project setup. Might need to do some planning on what exactly I want to do, need to find a strategy 
and implement it even if it is bad.