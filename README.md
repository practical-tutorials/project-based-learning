# Project Based Learning

A list of programming tutorials in which learners build an application from scratch. These tutorials are divided into different primary programming languages. Some have intermix technologies and languages.

To get started, simply fork this repo. Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Table of Contents:

* [C#](#c)
* [C/C++](#cc)
* [Clojure](#clojure)
* [Elixir](#elixir)
* [Go](#go)
* [Haskell](#haskell)
* [HTML/CSS](#html-and-css)
* [Java](#java)
* [JavaScript](#javascript)
* [Kotlin](#kotlin)
* [Lua](#lua)
* [OCaml](#ocaml)
* [PHP](#php)
* [Python](#python)
* [R](#r)
* [Ruby](#ruby)
* [Rust](#rust)
* [Swift](#swift)
* [Additional resources](#additional-resources)

## C/C++:

* [Build an Interpreter](http://www.craftinginterpreters.com/) (Chapter 14 on is written in C)
* [Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)
* [Write a FUSE Filesystem](https://www.cs.nmsu.edu/~pfeiffer/fuse-tutorial/)
* [Build Your Own Text Editor](http://viewsourcecode.org/snaptoken/kilo/)
* [Build Your Own Lisp](http://www.buildyourownlisp.com/)
* [How to Program an NES Game in C](https://nesdoug.com/)
* [Write an OS from scratch](https://github.com/tuhdo/os01)
* [How to Write an Emulator (CHIP-8 interpreter)](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/)
* [Beginning Game Programming with C++ and SDL](http://lazyfoo.net/tutorials/SDL/)
* [Implementing a Key-Value Store](http://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/)
* Writing a minimal x86-64 JIT compiler in C++
  * [Part 1](https://solarianprogrammer.com/2018/01/10/writing-minimal-x86-64-jit-compiler-cpp/)
  * [Part 2](https://solarianprogrammer.com/2018/01/12/writing-minimal-x86-64-jit-compiler-cpp-part-2/)
  * [Part 3](https://solarianprogrammer.com/2018/01/12/writing-minimal-x86-64-jit-compiler-cpp-part-3/)
* [Build a Live Code-reloader Library for C++](http://howistart.org/posts/cpp/1/index.html)
* [Write a hash table in C](https://github.com/jamesroutley/write-a-hash-table)
* [Let's Build a Simple Database](https://cstack.github.io/db_tutorial/)
* [Let's Write a Kernel](http://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)
* [Write a Bootloader in C](http://3zanders.co.uk/2017/10/13/writing-a-bootloader/)
* [Linux Container in 500 Lines of Code](https://blog.lizzie.io/linux-containers-in-500-loc.html)
* Write a C compiler
  * [Part 1: Integers, Lexing and Code Generation](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
  * [Part 2: Unary Operators](https://norasandler.com/2017/12/05/Write-a-Compiler-2.html)
  * [Part 3: Binary Operators](https://norasandler.com/2017/12/15/Write-a-Compiler-3.html)
  * [Part 4: Even More Binary Operators](https://norasandler.com/2017/12/28/Write-a-Compiler-4.html)
  * [Part 5: Local Variables](https://norasandler.com/2018/01/08/Write-a-Compiler-5.html)
  * [Part 6: Conditionals](https://norasandler.com/2018/02/25/Write-a-Compiler-6.html)
  * [Part 7: Compound Statements](https://norasandler.com/2018/03/14/Write-a-Compiler-7.html)
  * [Part 8: Loops](https://norasandler.com/2018/04/10/Write-a-Compiler-8.html)
* [Implementing a Language with LLVM](https://llvm.org/docs/tutorial/#kaleidoscope-implementing-a-language-with-llvm)
* [High-Performance Matrix Multiplication](https://gist.github.com/nadavrot/5b35d44e8ba3dd718e595e40184d03f0)
* Space Invaders from Scratch
  * [Part 1](http://nicktasios.nl/posts/space-invaders-from-scratch-part-1.html)
  * [Part 2](http://nicktasios.nl/posts/space-invaders-from-scratch-part-2.html)
  * [Part 3](http://nicktasios.nl/posts/space-invaders-from-scratch-part-3.html)
  * [Part 4](http://nicktasios.nl/posts/space-invaders-from-scratch-part-4.html)
* [Tetris Tutorial in C++ Platform Independent](http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/)
* Writing a Linux Debugger
  * [Part 1: Setup](https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/)
  * [Part 2: Breakpoints](https://blog.tartanllama.xyz/writing-a-linux-debugger-breakpoints/)
  * [Part 3: Registers and memory](https://blog.tartanllama.xyz/writing-a-linux-debugger-registers/)
  * [Part 4: Elves and dwarves](https://blog.tartanllama.xyz/writing-a-linux-debugger-elf-dwarf/)
  * [Part 5: Source and signals](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-signal/)
  * [Part 6: Source-level stepping](https://blog.tartanllama.xyz/writing-a-linux-debugger-dwarf-step/)
  * [Part 7: Source-level breakpoints](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-break/)
  * [Part 8: Stack unwinding](https://blog.tartanllama.xyz/writing-a-linux-debugger-unwinding/)
  * [Part 9: Handling variables](https://blog.tartanllama.xyz/writing-a-linux-debugger-variables/)
  * [Part 10: Advanced topics](https://blog.tartanllama.xyz/writing-a-linux-debugger-advanced-topics/)

### Network programming

* Let's Code a TCP/IP Stack
  * [Part 1: Ethernet & ARP](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/)
  * [Part 2: IPv4 & ICMPv4](http://www.saminiir.com/lets-code-tcp-ip-stack-2-ipv4-icmpv4/)
  * [Part 3: TCP Basics & Handshake](http://www.saminiir.com/lets-code-tcp-ip-stack-3-tcp-handshake/)
  * [Part 4: TCP Data Flow & Socket API](http://www.saminiir.com/lets-code-tcp-ip-stack-4-tcp-data-flow-socket-api/)
  * [Part 5: TCP Retransmission](http://www.saminiir.com/lets-code-tcp-ip-stack-5-tcp-retransmission/)
  
* Programming concurrent servers
  * [Part 1 - Introduction](https://eli.thegreenplace.net/2017/concurrent-servers-part-1-introduction/)
  * [Part 2 - Threads](https://eli.thegreenplace.net/2017/concurrent-servers-part-2-threads/)
  * [Part 3 - Event-driven](https://eli.thegreenplace.net/2017/concurrent-servers-part-3-event-driven/)
  * [Part 4 - libuv](https://eli.thegreenplace.net/2017/concurrent-servers-part-4-libuv/)
  * [Part 5 - Redis case study](https://eli.thegreenplace.net/2017/concurrent-servers-part-5-redis-case-study/)
  * [Part 6 - Callbacks, Promises and async/await](https://eli.thegreenplace.net/2018/concurrent-servers-part-6-callbacks-promises-and-asyncawait/)

### OpenGL:

* Creating 2D Breakout game clone in C++ with OpenGL
  * [Breakout](https://learnopengl.com/In-Practice/2D-Game/Breakout)
  * [Setting up](https://learnopengl.com/In-Practice/2D-Game/Setting-up)
  * [Rendering Sprites](https://learnopengl.com/In-Practice/2D-Game/Rendering-Sprites)
  * [Levels](https://learnopengl.com/In-Practice/2D-Game/Levels)
  * Collisions
    * [Ball](https://learnopengl.com/In-Practice/2D-Game/Collisions/Ball)
    * [Collision detection](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-detection)
    * [Collision resolution](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-resolution)
  * [Particles](https://learnopengl.com/In-Practice/2D-Game/Particles)
  * [Postprocessing](https://learnopengl.com/In-Practice/2D-Game/Postprocessing)
  * [Powerups](https://learnopengl.com/In-Practice/2D-Game/Powerups)
  * [Audio](https://learnopengl.com/In-Practice/2D-Game/Audio)
  * [Render text](https://learnopengl.com/In-Practice/2D-Game/Render-text)
  * [Final thoughts](https://learnopengl.com/In-Practice/2D-Game/Final-thoughts)
* [Handmade Hero](https://handmadehero.org)
* [How to Make Minecraft in C++/OpenGL](https://www.youtube.com/playlist?list=PLMZ_9w2XRxiZq1vfw1lrpCMRDufe2MKV_)

## C#:

* [Learn C# By Building a Simple RPG Game](http://scottlilly.com/learn-c-by-building-a-simple-rpg-index/)
* [Create a Rogue-like game in C#](https://roguesharp.wordpress.com/)
* [Create a Blank App with C# and Xamarin (work in progress)](https://www.intertech.com/Blog/xamarin-tutorial-part-1-create-a-blank-app/)
* [Build iOS Photo Library App with Xamarin and Visual Studio](https://www.raywenderlich.com/134049/building-ios-apps-with-xamarin-and-visual-studio)

## Clojure:

* [Build a Twitter Bot with Clojure](http://howistart.org/posts/clojure/1/index.html)
* [Bulding a Spell-Checker](https://bernhardwenzel.com/articles/clojure-spellchecker/)
* [Building a JIRA integration with Clojure & Atlassian Connect](https://hackernoon.com/building-a-jira-integration-with-clojure-atlassian-connect-506ebd112807)

## Elixir

* [Building a Simple Chat App With Elixir and Phoenix](https://sheharyar.me/blog/simple-chat-phoenix-elixir/)

## Java:

* [Build an Interpreter](http://www.craftinginterpreters.com/) (Chapter 4-13 is written in Java)
* [Build a Simple HTTP Server with Java](http://javarevisited.blogspot.com/2015/06/how-to-create-http-server-in-java-serversocket-example.html)
* [Build an Android Flashlight App](https://www.youtube.com/watch?v=dhWL4DC7Krs)
* [Build a Spring Boot App with User Authentication](https://scotch.io/tutorials/build-a-spring-boot-app-with-user-authentication)

## JavaScript:

* [Build 30 things in 30 days with 30 tutorials](https://javascript30.com)
* [Build an App in Pure JS](https://medium.com/codingthesmartway-com-blog/pure-javascript-building-a-real-world-application-from-scratch-5213591cfcd6)

## HTML and CSS:

* [Build A Loading Screen](https://medium.freecodecamp.org/how-to-build-a-delightful-loading-screen-in-5-minutes-847991da509f)
* [Build an HTML Calculator with JS](https://medium.freecodecamp.org/how-to-build-an-html-calculator-app-from-scratch-using-javascript-4454b8714b98)

### Mobile Application:

* [Build a React Native Todo Application](https://egghead.io/courses/build-a-react-native-todo-application)

### Web Applications:

#### React:

* [Create Serverless React.js Apps](http://serverless-stack.com/)
* [Create a Trello Clone](http://codeloveandboards.com/blog/2016/01/04/trello-tribute-with-phoenix-and-react-pt-1/)
* [Create a Character Voting App with React, Node, MongoDB and SocketIO](http://sahatyalkabov.com/create-a-character-voting-app-using-react-nodejs-mongodb-and-socketio/)
* [React Tutorial: Cloning Yelp](https://www.fullstackreact.com/articles/react-tutorial-cloning-yelp/)
* [Build a Full Stack Movie Voting App with Test-First Development using Mocha, React, Redux and Immutable](https://teropa.info/blog/2015/09/10/full-stack-redux-tutorial.html)
* [Build a Twitter Stream with React and Node](https://scotch.io/tutorials/build-a-real-time-twitter-stream-with-node-and-react-js)
* Build a Serverless MERN Story App with Webtask.io
  * [Part 1](https://scotch.io/tutorials/build-a-serverless-mern-story-app-with-webtask-io-zero-to-deploy-1)
  * [Part 2](https://scotch.io/tutorials/build-a-serverless-mern-story-app-with-webtask-io-zero-to-deploy-2)
* [Build A Simple Medium Clone using React.js and Node.js](https://codeburst.io/build-simple-medium-com-on-node-js-and-react-js-a278c5192f47)
* [Integrate MailChimp in JS](https://medium.freecodecamp.org/how-to-integrate-mailchimp-in-a-javascript-web-app-2a889fb43f6f)
* [Build A Chrome Extension with React + Parcel](https://medium.freecodecamp.org/building-chrome-extensions-in-react-parcel-79d0240dd58f)
* [Build A ToDo App With React Native](https://blog.hasura.io/tutorial-fullstack-react-native-with-graphql-and-authentication-18183d13373a)
* [Make a Chat Application](https://medium.freecodecamp.org/how-to-build-a-chat-application-using-react-redux-redux-saga-and-web-sockets-47423e4bc21a)
* [Create a News App with React Native](https://medium.freecodecamp.org/create-a-news-app-using-react-native-ced249263627)
* [Learn Webpack For React](https://medium.freecodecamp.org/learn-webpack-for-react-a36d4cac5060)
* [Testing React App With Pupepeteer and Jest](https://blog.bitsrc.io/testing-your-react-app-with-puppeteer-and-jest-c72b3dfcde59)
* [Build Your Own React Boilerplate](https://medium.freecodecamp.org/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f)
* [Code The Game Of Life With React](https://medium.freecodecamp.org/create-gameoflife-with-react-in-one-hour-8e686a410174)
* [A Basic React+Redux Introductory Tutorial](https://hackernoon.com/a-basic-react-redux-introductory-tutorial-adcc681eeb5e)

#### Angular:

* [Build an Instagram Clone](https://hackhands.com/building-instagram-clone-angularjs-satellizer-nodejs-mongodb/)
* Build an offline-capable Hacker News client with Angular 2+
  * [Part 1](https://houssein.me/angular2-hacker-news)
  * [Part 2](https://houssein.me/progressive-angular-applications)
* [Build a web application with Django and AngularJS](https://thinkster.io/django-angularjs-tutorial)
* Build A Beautiful Real World App with Angular 6 :
  * [Part I](https://medium.com/@hamedbaatour/build-a-real-world-beautiful-web-app-with-angular-6-a-to-z-ultimate-guide-2018-part-i-e121dd1d55e)
* [Build Responsive layout with BootStrap 4 and Angular 6](https://medium.com/@tomastrajan/how-to-build-responsive-layouts-with-bootstrap-4-and-angular-6-cfbb108d797b)

#### Node:

* [Build A Simple Website With Node,Express and MongoDB](https://closebrace.com/tutorials/2017-03-02/the-dead-simple-step-by-step-guide-for-front-end-developers-to-getting-up-and-running-with-nodejs-express-and-mongodb)
* [Build a URL Shortener with Node, MongoDB and Hapi.js](https://www.codetuts.tech/build-a-url-shortener-node-hapi-js/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)
* [Build a real-time Markdown Editor with NodeJS](https://scotch.io/tutorials/building-a-real-time-markdown-viewer)
* [Test-Driven Development with Node, Postgres and Knex](http://mherman.org/blog/2016/04/28/test-driven-development-with-node/)
* Write a Twitter Bot in Node.js
  * [Part 1](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-in-just-38-lines-of-code-ed92db9eb078)
  * [Part 2](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-part-2-do-more-2ef1e039715d)
* [Create A Simple RESTFUL Web App](https://closebrace.com/tutorials/2017-03-02/creating-a-simple-restful-web-app-with-nodejs-express-and-mongodb)

#### Vue

* [Vue 2 + Firebase: How to build a Vue app with Firebase authentication system in 15 minutes](https://medium.com/@anas.mammeri/vue-2-firebase-how-to-build-a-vue-app-with-firebase-authentication-system-in-15-minutes-fdce6f289c3c)
* [Vue.js Application Tutorial – Creating a Simple Budgeting App with Vue](https://matthiashager.com/complete-vuejs-application-tutorial/)

#### Others (Hapi, Express...):

* Build a Progressive Web Application (PWA)
  * [Part 1](https://bitsofco.de/bitsofcode-pwa-part-1-offline-first-with-service-worker/)
  * [Part 2](https://bitsofco.de/bitsofcode-pwa-part-2-instant-loading-with-indexeddb/)
  * [Part 3](https://bitsofco.de/bitsofcode-pwa-part-3-push-notifications/)
* Build A Support Ticket Application With AdonisJs
  * [Part 1](https://scotch.io/tutorials/build-a-support-ticket-application-with-adonisjs)
  * [Part 2](https://scotch.io/tutorials/build-a-support-ticket-application-with-adonisjs-part-2)
* [Build A Native Desktop App with JS](https://medium.freecodecamp.org/build-native-desktop-apps-with-javascript-a49ede90d8e9)
* Build a Powerful API with NodeJs,GraphQL and Hapi
  * [Part I](https://medium.com/@wesharehoodies/how-to-setup-a-powerful-api-with-nodejs-graphql-mongodb-hapi-and-swagger-e251ac189649)

#### D3.js

* [Learn D3 using examples](https://www.sitepoint.com/d3-js-data-visualizations/)
* [Learn To Make A Line Chart](https://medium.freecodecamp.org/learn-to-create-a-line-chart-using-d3-js-4f43f1ee716b)

### Game Development:

* [Make 2D Breakout Game using Phaser](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_breakout_game_Phaser)
* Make Flappy Bird in HTML5 and JavaScript with Phaser
  * [Part 1](http://www.lessmilk.com/tutorial/flappy-bird-phaser-1)
  * [Part 2](http://www.lessmilk.com/tutorial/flappy-bird-phaser-2)

### Desktop Application:

* Build a Music Player with React & Electron
  * [Part 1](https://scotch.io/tutorials/build-a-music-player-with-react-electron-i-setup-basic-concepts)
  * [Part 2](https://scotch.io/tutorials/build-a-music-player-with-react-electron-ii-making-the-ui)
  * [Part 3](https://scotch.io/tutorials/build-a-music-player-with-react-electron-iii-bringing-it-all-together)

### Miscellaneous:

* [How to Build a Web Framework in Less Than 20 Lines of Code](https://www.pubnub.com/blog/build-yourself-a-web-framework-in-less-than-20-lines-of-code/)
* [Build Yourself a Redux](https://zapier.com/engineering/how-to-build-redux/)
* [How to write your own Virtual DOM](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)

## Kotlin:

* [Keddit - Learn Kotlin While Developing an Android Application](https://medium.com/@juanchosaravia/learn-kotlin-while-developing-an-android-app-introduction-567e21ff9664)

## Lua:

### LÖVE:

* BYTEPATH: Creation of a Complete Game with Lua and LÖVE
  * [Part 0: Introduction](https://github.com/SSYGEN/blog/issues/30)
  * [Part 1: Game Loop](https://github.com/SSYGEN/blog/issues/15)
  * [Part 2: Libraries](https://github.com/SSYGEN/blog/issues/16)
  * [Part 3: Rooms and Areas](https://github.com/SSYGEN/blog/issues/17)
  * [Part 4: Exercises](https://github.com/SSYGEN/blog/issues/18)
  * [Part 5: Game Basics](https://github.com/SSYGEN/blog/issues/19)
  * [Part 6: Player Basics](https://github.com/SSYGEN/blog/issues/20)
  * [Part 7: Player Stats and Attacks](https://github.com/SSYGEN/blog/issues/21)
  * [Part 8: Enemies](https://github.com/SSYGEN/blog/issues/22)
  * [Part 9: Director and Gameplay Loop](https://github.com/SSYGEN/blog/issues/23)
  * [Part 10: Coding Practices](https://github.com/SSYGEN/blog/issues/24)
  * [Part 11: Passives](https://github.com/SSYGEN/blog/issues/25)
  * [Part 12: More Passives](https://github.com/SSYGEN/blog/issues/26)
  * [Part 13: Skill Tree](https://github.com/SSYGEN/blog/issues/27)
  * [Part 14: Console](https://github.com/SSYGEN/blog/issues/28)
  * [Part 15: Final](https://github.com/SSYGEN/blog/issues/29)

## Python:

### Web Scraping:

* [Mining Twitter Data with Python](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)
* [Scrape a Website with Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
* [How To Scrape With Python and Selenium WebDriver](http://www.byperth.com/2018/04/25/guide-web-scraping-101-what-you-need-to-know-and-how-to-scrape-with-python-selenium-webdriver/)
* [Which Movie Should I Watch using BeautifulSoup](https://medium.com/@nishantsahoo.in/which-movie-should-i-watch-5c83a3c0f5b1)

### Web Applications:

* [Build a Microblog with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* Create a Blog Web App In Django
  * [Part I : Introduction](https://tutorial.djangogirls.org/en/)
  * [Part II : Extension To Add More Features](https://legacy.gitbook.com/book/djangogirls/django-girls-tutorial-extensions/details)
* [Choose Your Own Adventure Presentations](https://www.twilio.com/blog/2015/03/choose-your-own-adventures-presentations-wizard-mode-part-1-of-3.html)
* [Build a Todo List with Flask and RethinkDB](https://realpython.com/blog/python/rethink-flask-a-simple-todo-list-powered-by-flask-and-rethinkdb/)
* [Build a Todo List with Django and Test-Driven Development](http://www.obeythetestinggoat.com/)
* [Build a RESTful Microservice in Python](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/)
* [Microservices with Docker, Flask, and React](https://testdriven.io/)
* [Build A Simple Web App With Flask](https://pythonspot.com/flask-web-app-with-python/)
* [Build a RESTful API with Flask – The TDD Way](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)

### Bots:

* [Build a Reddit Bot](http://pythonforengineers.com/build-a-reddit-bot-part-1/)
* [How to Make a Reddit Bot - YouTube](https://www.youtube.com/watch?v=krTUf7BpTc0)
* [Build a Facebook Messenger Bot](https://blog.hartleybrody.com/fb-messenger-bot/)
* [Making a Reddit + Facebook Messenger Bot](https://pythontips.com/2017/04/13/making-a-reddit-facebook-messenger-bot/)
* How To Create a Telegram Bot Using Python
  * [Part 1](https://khashtamov.com/en/how-to-create-a-telegram-bot-using-python/)
  * [Part 2](https://khashtamov.com/en/how-to-deploy-telegram-bot-django/)
* [Create a Twitter Bot In Python](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607)

### Data Science:

* Learn Python For Data Science by Doing Several Projects:
  * [Part 1: Introduction](https://www.youtube.com/watch?v=T5pRlIbr6gg)
  * [Part 2: Twitter Sentiment Analysis](https://www.youtube.com/watch?v=o_OZdbCzHUA)
  * [Part 3: Recommendation Systems](https://www.youtube.com/watch?v=9gBC9R-msAk&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=3)
  * [Part 4: Predicting Stock Prices](https://www.youtube.com/watch?v=SSu00IRRraY&index=4&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)
  * [Part 5: Deep Dream in TensorFlow](https://www.youtube.com/watch?v=MrBzgvUNr4w&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=5)
  * [Part 6: Genetic Algorithms](https://www.youtube.com/watch?v=dSofAXnnFrY&index=6&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)

### Machine Learning:

* [Write Linear Regression From Scratch in Python](https://www.youtube.com/watch?v=uwwWVAgJBcM)
* [Step-By-Step Machine Learning In Python](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
* [Predict Quality Of Wine](https://medium.freecodecamp.org/using-machine-learning-to-predict-the-quality-of-wines-9e2e13d7480d)
* [Solving A Fruits Classification Problem](https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2)
* [Learn Unsupervised Learning with Python](https://towardsdatascience.com/unsupervised-learning-with-python-173c51dc7f03)
* [Build Your Own Neural Net from Scratch in Python](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)

### Deep Learning:

* [Using Convolutional Neural Nets to Detect Facial Keypoints](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)
* [Generate an Average Face using Python and OpenCV](https://www.learnopencv.com/average-face-opencv-c-python-tutorial/)
* [Break A Captcha System using CNNs](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710)
* [Use pre-trained Inception model to provide image predictions](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)
* [Create your first CNN](https://hackernoon.com/deep-learning-cnns-in-tensorflow-with-gpus-cba6efe0acc2)
* [Build A Facial Recognition Pipeline](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)
* [Build An Image Caption Generator](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f)
* [Make your Own Face Recognition System](https://medium.freecodecamp.org/making-your-own-face-recognition-system-29a8e728107c)
* [Train a Language Detection AI in 20 minutes](https://towardsdatascience.com/how-i-trained-a-language-detection-ai-in-20-minutes-with-a-97-accuracy-fdeca0fb7724)
* [Object Detection With Neural Networks](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)
* Learn Twitter Sentiment Analysis -
  * [Part I - Data Cleaning](https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)
  * [Part II - EDA, Data Visualisation](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-2-333514854913)
  * [Part III - Zipf's Law, Data Visualisation](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-3-zipfs-law-data-visualisation-fc9eadda71e7)
  * [Part IV - Feature Extraction(count vectoriser)](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-4-count-vectorizer-b3f4944e51b5)
  * [Part V - Feature Extraction(Tfidf vectoriser)](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-5-50b4e87d9bdd)
  * [Part VI - Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-6-doc2vec-603f11832504)
  * [Part VII - Phrase Modeling + Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-7-phrase-modeling-doc2vec-592a8a996867)
  * [Part VIII - Dimensionality Reduction](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-8-dimensionality-reduction-chi2-pca-c6d06fb3fcf3)
  * [Part IX - Neural Nets with Tfdif vectors](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-9-neural-networks-with-tfidf-vectors-using-d0b4af6be6d7)
  * [Part X - Neural Nets with word2vec/doc2vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-10-neural-network-with-a6441269aa3c)
  * [Part XI - CNN with Word2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-11-cnn-word2vec-41f5e28eda74)
* [Use Transfer Learning for custom image classification](https://becominghuman.ai/transfer-learning-retraining-inception-v3-for-custom-image-classification-2820f653c557)

### Miscellaneous:

* [Build a Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/)
* [Build a Simple Blockchain in Python](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
* [Write a NoSQL Database in Python](https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/)
* [Building a Gas Pump Scanner with OpenCV/Python/iOS](https://hackernoon.com/building-a-gas-pump-scanner-with-opencv-python-ios-116fe6c9ae8b)
* [Build a Distributed Streaming System with Python and Kafka](https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python)
* [Writing a basic x86-64 JIT compiler from scratch in stock Python](https://csl.name/post/python-jit/)

## Go:

* [Create a Real Time Chat App with Golang, Angular 2, and WebSocket](https://www.thepolyglotdeveloper.com/2016/12/create-real-time-chat-app-golang-angular-2-websockets/)
* [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin)
* [How to Use Godog for Behavior-driven Development in Go et started with Godog](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go)
* Building Blockchain in Go
  * [Part 1: Basic Prototype](https://jeiwan.cc/posts/building-blockchain-in-go-part-1/)
  * [Part 2: Proof of Work](https://jeiwan.cc/posts/building-blockchain-in-go-part-2/)
  * [Part 3: Persistence and CLI](https://jeiwan.cc/posts/building-blockchain-in-go-part-3/)
  * [Part 4: Transactions 1](https://jeiwan.cc/posts/building-blockchain-in-go-part-4/)
  * [Part 5: Address](https://jeiwan.cc/posts/building-blockchain-in-go-part-5/)
  * [Part 6: Transactions 2](https://jeiwan.cc/posts/building-blockchain-in-go-part-6/)
  * [Part 7: Network](https://jeiwan.cc/posts/building-blockchain-in-go-part-7/)
* [Build Web Application with GoLang](https://legacy.gitbook.com/book/astaxie/build-web-application-with-golang/details)

## PHP:

* [How To Build A Blog With Laravel](https://www.youtube.com/playlist?list=PLwAKR305CRO-Q90J---jXVzbOd4CDRbVx)
* [Make Your Own Blog (in Pure PHP)](http://ilovephp.jondh.me.uk/en/tutorial/make-your-own-blog)
* [Build A Real Estate Website Example with SilverStripe](https://www.silverstripe.org/learn/lessons/)
* [Building Realtime Chat App with Laravel 5.4 and VueJS](https://www.youtube.com/playlist?list=PLXsbBbd36_uVjOFH_P25__XAyGsohXWlv)
* [Build A Social Network: Laravel 5 - Youtube](https://www.youtube.com/playlist?list=PLfdtiltiRHWGGxaR6uFtwZnnbcXqyq8JD)
* Build a full-featured multi-tenant app with Laravel
  * [Part 0: Introduction](https://medium.com/@ashokgelal/writing-a-full-featured-multi-tenant-laravel-app-from-scratch-a0e1a7350d9d)
  * [Part 1: Setup](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-1-4049a3cc229d)
  * [Part 2: Roles and Permissinos](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-2-roles-and-permissions-d9a5bfe5d525)
  * [Part 3: Invitation](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-3-invitation-c982dca55eb9)
  * [Part 4: Authentication](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-4-tenancy-aware-authentication-e0ee37270bc8)
  * [Part 5: Testing](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-2-unit-tests-96d6dfbf0617)
  * [Part 6: User Profile](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-5-user-profile-5c3d0c655f3a)
  * [Part 7: Deployment](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-7-deployment-40bb3c895627
)
  

## OCaml:

* [Implement a Language with LLVM in OCaml](https://llvm.org/docs/tutorial/#kaleidoscope-implementing-a-language-with-llvm-in-objective-caml)

## Ruby:

* [Build a Network Stack with Ruby](https://medium.com/geckoboard-under-the-hood/how-to-build-a-network-stack-in-ruby-f73aeb1b661b)

### Ruby on Rails:

* [Build Instagram From Scratch with Ruby on Rails](https://www.dropbox.com/s/9vq430e9s3q7pu8/Let%27s%20Build%20Instagram%20with%20Ruby%20on%20Rails%20-%20Free%20Edition.pdf?dl=0)
* [Build a CMS with Ruby on Rails](https://pchm.co/posts/tutorial-how-to-build-a-cms-in-ruby-on-rails)
* [Build a Social Network using Rails](https://medium.com/rails-ember-beyond/how-to-build-a-social-network-using-rails-eb31da569233)

## Haskell:

* [Write You a Haskell - Build a modern functional compiler](http://dev.stephendiehl.com/fun/)
* [Write Yourself a Scheme in 48 hours](https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours)
* [Write You A Scheme, Version 2](https://github.com/write-you-a-scheme-v2/scheme)
* [Roll Your Own IRC Bot](https://wiki.haskell.org/Roll_your_own_IRC_bot)
* [Let's Build A Basic Compiler in Haskell](http://alephnullplex.github.io/cradle/)
* [Making Movie Monad](https://lettier.github.io/posts/2016-08-15-making-movie-monad.html)
* [Making a Website with Haskell **(outdated)**](http://adit.io/posts/2013-04-15-making-a-website-with-haskell.html)

## R:

* [Build Web Apps with Shiny](http://shiny.rstudio.com/tutorial/)
* [Build A Cryptocurrency Bot](https://towardsdatascience.com/build-a-cryptocurrency-trading-bot-with-r-1445c429e1b1)
* [Learn Associate Rule Mining in R](https://towardsdatascience.com/association-rule-mining-in-r-ddf2d044ae50)

## Rust:

* A Simple Web App in Rust
  * [Part 1](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-1/)
  * [Part 2a](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-2a/)
  * [Part 2b](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-2b/)
* [Write an OS in pure Rust](https://os.phil-opp.com/news/2018-03-09-pure-rust/)
* [Build a browser engine in Rust](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
* [Write a Microservice in Rust](http://www.goldsborough.me/rust/web/tutorial/2018/01/20/17-01-11-writing_a_microservice_in_rust/)
* [Learning Rust with Too Many Linked Lists](http://cglab.ca/~abeinges/blah/too-many-lists/book/README.html)
* Rust in Detail: Writing Scalable Chat Service from Scratch
  * [Part 1: Implementing WebSocket. Introduction.](https://nbaksalyar.github.io/2015/07/10/writing-chat-in-rust.html)
  * [Part 2: Sending and Receiving Messages](https://nbaksalyar.github.io/2015/11/09/rust-in-detail-2.html)

## Swift:

* [Hacking with Swift - Learn Swift by doing 39 projects](https://www.hackingwithswift.com/read)

## Additional Resources

* [React Redux Links](https://github.com/markerikson/react-redux-links)
* [Full Stack Python](https://www.fullstackpython.com/)
* [Node School](https://nodeschool.io/)
* [ScotchIO](https://scotch.io/)
* [Exercism](http://www.exercism.io/)
* [Egghead.io](http://www.egghead.io/)
* [Michael Herman's Blog](http://mherman.org/)
* [Thinkster.io](http://thinkster.io)
* [C Project Based Tutorials](https://www.reddit.com/r/C_Programming/comments/872rlt/c_project_based_tutorials/)
