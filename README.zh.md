# 基于项目的学习

[![Gitter](https://badges.gitter.im/practical-tutorials/community.svg)](https://gitter.im/practical-tutorials/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![ENDOC](https://img.shields.io/badge/english-document-white.svg)](README.md)

**译注：该中文翻译不保证最新**

这是一个编程教程列表，有志向成为软件开发者的人可以从零开始学习如何构建一个应用程序。这些教程根据不同的主要编程语言进行了分类。教程可能涉及多种技术和语言。

要开始，请复刻这个仓库。有关贡献准则，请参阅[贡献指南](CONTRIBUTING.zh.md)。

## 目录：

- [C#](#c)
- [C/C++](#cc)
- [Clojure](#clojure)
- [Dart](#dart)
- [Elixir](#elixir)
- [Erlang](#erlang)
- [F#](#f)
- [Go](#go)
- [Haskell](#haskell)
- [HTML/CSS](#html-and-css)
- [Java](#java)
- [JavaScript](#javascript)
- [Kotlin](#kotlin)
- [Lua](#lua)
- [OCaml](#ocaml)
- [PHP](#php)
- [Python](#python)
- [R](#r)
- [Ruby](#ruby)
- [Rust](#rust)
- [Scala](#scala)
- [Swift](#swift)
- [额外资源](#额外资源)

## C/C++:

- [构建一个解释器](http://www.craftinginterpreters.com/)（第14章开始使用C编写）
- [内存分配器101 - 编写一个简单的内存分配器](https://arjunsreedharan.org/post/148675821737/memory-allocators-101-write-a-simple-memory)
- [用C编写一个Shell](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- [编写一个FUSE文件系统](https://www.cs.nmsu.edu/~pfeiffer/fuse-tutorial/)
- [构建自己的文本编辑器](http://viewsourcecode.org/snaptoken/kilo/)
- [构建自己的Lisp](http://www.buildyourownlisp.com/)
- [如何在C中编写NES游戏](https://nesdoug.com/)
- [从零开始编写操作系统](https://github.com/tuhdo/os01)
- [如何从头开始创建操作系统](https://github.com/cfenollosa/os-tutorial)
- [构建一个CHIP-8模拟器](https://austinmorlan.com/posts/chip8_emulator/)
- [使用C++和SDL开始游戏编程](http://lazyfoo.net/tutorials/SDL/)
- [实现键值存储](http://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/)
- 微型3D图形项目
  - [微型渲染器或OpenGL的工作原理：500行代码中的软件渲染](https://github.com/ssloy/tinyrenderer/wiki)
  - [256行纯C++可理解的光线追踪](https://github.com/ssloy/tinyraytracer/wiki)
  - [180行纯C++ KABOOM！](https://github.com/ssloy/tinykaboom/wiki)
  - [486行C++：周末内编写的老派FPS](https://github.com/ssloy/tinyraycaster/wiki)
- 在C++中编写一个最小的x86-64 JIT编译器
  - [第1部分](https://solarianprogrammer.com/2018/01/10/writing-minimal-x86-64-jit-compiler-cpp/)
  - [第2部分](https://solarianprogrammer.com/2018/01/12/writing-minimal-x86-64-jit-compiler-cpp-part-2/)
- [为C++构建一个实时代码重新加载库](http://howistart.org/posts/cpp/1/index.html)
- [用C编写哈希表](https://github.com/jamesroutley/write-a-hash-table)
- [让我们构建一个简单的数据库](https://cstack.github.io/db_tutorial/)
- [编写一个引导加载程序](http://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)
- [用C编写引导加载程序](http://3zanders.co.uk/2017/10/13/writing-a-bootloader/)
- [500行代码中的Linux容器](https://blog.lizzie.io/linux-containers-in-500-loc.html)
- [编写自己的虚拟机](https://justinmeiners.github.io/lc3-vm/)
- [学习KVM - 实现自己的Linux内核](https://david942j.blogspot.com/2018/10/note-learning-kvm-implement-your-own.html)
- [使用C/C++构建自己的Redis](https://build-your-own.org/redis/)
- 编写一个C编译器
  - [第1部分：整数、词法分析和代码生成](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
  - [第2部分：一元运算符](https://norasandler.com/2017/12/05/Write-a-Compiler-2.html)
  - [第3部分：二元运算符](https://norasandler.com/2017/12/15/Write-a-Compiler-3.html)
  - [第4部分：更多二元运算符](https://norasandler.com/2017/12/28/Write-a-Compiler-4.html)
  - [第5部分：局部变量](https://norasandler.com/2018/01/08/Write-a-Compiler-5.html)
  - [第6部分：条件语句](https://norasandler.com/2018/02/25/Write-a-Compiler-6.html)
  - [第7部分：复合语句](https://norasandler.com/2018/03/14/Write-a-Compiler-7.html)
  - [第8部分：循环](https://norasandler.com/2018/04/10/Write-a-Compiler-8.html)
  - [第9部分：函数](https://norasandler.com/2018/06/27/Write-a-Compiler

-9.html)
  - [第10部分：全局变量](https://norasandler.com/2019/02/18/Write-a-Compiler-10.html)
- [使用LLVM实现一种语言](https://llvm.org/docs/tutorial/#kaleidoscope-implementing-a-language-with-llvm)
- [Meta Crush Saga：一个基于C++17的编译时游戏](https://jguegant.github.io//jguegant.github.io/blogs/tech/meta-crush-saga.html)
- [高性能矩阵乘法](https://gist.github.com/nadavrot/5b35d44e8ba3dd718e595e40184d03f0)
- 从零开始的太空入侵者
  - [第1部分](http://nicktasios.nl/posts/space-invaders-from-scratch-part-1.html)
  - [第2部分](http://nicktasios.nl/posts/space-invaders-from-scratch-part-2.html)
  - [第3部分](http://nicktasios.nl/posts/space-invaders-from-scratch-part-3.html)
  - [第4部分](http://nicktasios.nl/posts/space-invaders-from-scratch-part-4.html)
  - [第5部分](http://nicktasios.nl/posts/space-invaders-from-scratch-part-5.html)
- [C++平台无关的俄罗斯方块教程](http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/)
- 编写Linux调试器
  - [第1部分：设置](https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/)
  - [第2部分：断点](https://blog.tartanllama.xyz/writing-a-linux-debugger-breakpoints/)
  - [第3部分：寄存器和内存](https://blog.tartanllama.xyz/writing-a-linux-debugger-registers/)
  - [第4部分：精灵和矮人](https://blog.tartanllama.xyz/writing-a-linux-debugger-elf-dwarf/)
  - [第5部分：源码和信号](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-signal/)
  - [第6部分：源码级步进](https://blog.tartanllama.xyz/writing-a-linux-debugger-dwarf-step/)
  - [第7部分：源码级断点](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-break/)
  - [第8部分：堆栈展开](https://blog.tartanllama.xyz/writing-a-linux-debugger-unwinding/)
  - [第9部分：处理变量](https://blog.tartanllama.xyz/writing-a-linux-debugger-variables/)
  - [第10部分：高级主题](https://blog.tartanllama.xyz/writing-a-linux-debugger-advanced-topics/)
- 让我们写一个编译器
  - [第1部分：介绍、选择一种语言和做一些规划](https://briancallahan.net/blog/20210814.html)
  - [第2部分：词法分析器](https://briancallahan.net/blog/20210815.html)
  - [第3部分：解析器](https://briancallahan.net/blog/20210816.html)
  - [第4部分：测试](https://briancallahan.net/blog/20210817.html)
  - [第5部分：代码生成器](https://briancallahan.net/blog/20210818.html)
  - [第6部分：输入和输出](https://briancallahan.net/blog/20210819.html)
  - [第7部分：数组](https://briancallahan.net/blog/20210822.html)
  - [第8部分：字符串、前向引用和结论](https://briancallahan.net/blog/20210826.html)

### 网络编程

- 编写一个TCP/IP协议栈

  - [第1部分：以太网和ARP](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/)
  - [第2部分：IPv4和ICMPv4](http://www.saminiir.com/lets-code-tcp-ip-stack-2-ipv4-icmpv4/)
  - [第3部分：TCP基础和握手](http://www.saminiir.com/lets-code-tcp-ip-stack-3-tcp-handshake/)
  - [第4部分：TCP数据流和套接字API](http://www.saminiir.com/lets-code-tcp-ip-stack-4-tcp-data-flow-socket-api/)
  - [第5部分：TCP重传](http://www.saminiir.com/lets-code-tcp-ip-stack-5-tcp-retransmission/)

- 编写并发服务器

  - [第1部分 - 介绍](https://eli.thegreenplace.net/2017/concurrent-servers-part-1-introduction/)
  - [第2部分 - 线程](https://eli.thegreenplace.net/2017/concurrent-servers-part-2-threads/)
  - [第3部分 - 事件驱动](https://eli.thegreenplace.net/2017/concurrent-servers-part-3-event-driven/)
  - [第4部分 - libuv](https://eli.thegreenplace.net/2017/concurrent-servers-part-4-libuv/)
  - [第5部分 - Redis案例研究](https://eli.thegreenplace.net/2017/concurrent-servers-part-5-redis-case-study/)
  - [第6部分 - 回调、Promises和async/await](https://eli.thegreenplace.net/2018/concurrent-servers-part-6-callbacks-promises-and-asyncawait/)

- 从零开始构建MQTT代理
  - [第1部分 - 协议](https://codepr.github.io/posts/sol-mqtt-broker)
  - [第2部分 - 网络](https://codepr.github.io/posts/sol-mqtt-broker-p2)
  - [第3部分 - 服务器](https://codepr.github.io/posts/sol-mqtt-broker-p3)
  - [第4部分 - 数据结构](https://codepr.github.io/posts/sol-mqtt-broker-p4)
  - [第5部分 - 主题抽象](https://codepr.github.io/posts/sol-mqtt-broker-p5)
  - [第6部分 - 处理程序](https://codepr.github.io/posts/sol-mqtt-broker-p6)
  - [奖励 - 多线程](https://codepr.github.io/posts/sol-mqtt-broker-bonus)

### OpenGL：

- 使用C++和OpenGL创建2D打砖块游戏克隆
  - [打砖块](https://learnopengl.com/In-Practice/2D-Game/Breakout)
  - [设置](https://learnopengl.com/In-Practice/2D-Game/Setting-up)
  - [渲染精灵](https://learnopengl.com/In-Practice/2D-Game/Rendering-Sprites)
  - [关卡](https://learnopengl.com/In-Practice/2D-Game/Levels)
  - 碰撞
    - [球](https://learnopengl.com/In-Practice/2D-Game/Collisions/Ball)
    - [碰撞检测](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-detection)
    - [碰撞解决](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-resolution)
  - [粒子](https://learnopengl.com/In-Practice/2D-Game/Particles)
  - [后处理](https://learnopengl.com/In-Practice/2D-Game/Postprocessing)
  - [道具](https://learnopengl.com/In-Practice/2D-Game/Powerups)
  - [音频](https://learnopengl.com/In-Practice/2D-Game/Audio)
  - [渲染文本](https://learnopengl.com/In-Practice/2D-Game/Render-text)
  - [最终思考](https://learnopengl.com/In-Practice/2D-Game/Final-thoughts)
- [手工英雄](https://handmadehero.org)
- [如何使用C++/OpenGL制作Minecraft](https://www.youtube.com/playlist?list=PLMZ_9w2XRxiZq1vfw1lrpCMRDufe2MKV_)（视频）

## C#：

- [通过构建简单的RPG游戏学习C#](http://scottlilly.com/learn-c-by-building-a-simple-rpg-index/)
- [使用C#创建Rogue-like游戏](https://roguesharp.wordpress.com/)
- [使用C#和Xamarin创建空白应用程序（正在进行中）](https://www.intertech.com/Blog/xamarin-tutorial-part-1-create-a-blank-app/)
- [使用Xamarin和Visual Studio构建iOS照片库应用程序](https://www.raywenderlich.com/134049/building-ios-apps-with-xamarin-and-visual-studio)
- [构建CoreWiki](https://www.youtube.com/playlist?list=PLVMqA0_8O85yC78I4Xj7z48ES48IQBa7p) 这是一个完全使用C#、ASP.NET Core和Razor Pages编写的Wiki风格内容管理系统。您可以在[这里](https://github.com/csharpfritz/CoreWiki)找到源代码。

## Clojure：

- [使用Clojure构建Twitter机器人](http://howistart.org/posts/clojure/1/index.html)
- [构建拼写检查器](https://bernhardwenzel.com/articles/clojure-spellchecker/)
- [使用Clojure和Atlassian Connect构建JIRA集成](https://hackernoon.com/building-a-jira-integration-with-clojure-atlassian-connect-506ebd112807)
- [使用ClojureScript制作俄罗斯方块](https://shaunlebron.github.io/t3tr0s-slides)

## Dart：

### Flutter：

- [具有管理面板的亚马逊克隆](https://youtu.be/O3nmP-lZAdg)
-

 [食品交付应用程序](https://youtu.be/7dAt-JMSCVQ)
- [Google Docs克隆](https://youtu.be/0_GJ1w_iG44)
- [Instagram克隆](https://youtu.be/mEPm9w5QlJM)
- [多人TicTacToe游戏](https://youtu.be/Aut-wfXacXg)
- [TikTok克隆](https://youtu.be/4E4V9F3cbp4)
- [门票预订应用程序](https://youtu.be/71AsYo2q_0Y)
- [旅行应用程序](https://youtu.be/x4DydJKVvQk)
- [Twitch克隆](https://youtu.be/U9YKZrDX0CQ)
- [WhatsApp克隆](https://youtu.be/yqwfP2vXWJQ)
- [Wordle克隆](https://youtu.be/_W0RN_Cqhpg)
- [Zoom克隆](https://youtu.be/sMA1dKbv33Y)
- [Netflix克隆](https://youtu.be/J8IFNKzs3TI)

## Elixir

- [使用Elixir和Phoenix构建简单的聊天应用](https://sheharyar.me/blog/simple-chat-phoenix-elixir/)
- [如何使用Elixir、Phoenix和Mnesia编写超快的链接缩短器](https://medium.com/free-code-camp/how-to-write-a-super-fast-link-shortener-with-elixir-phoenix-and-mnesia-70ffa1564b3c)

## Erlang

- [ChatBus：使用Erlang/OTP构建您的第一个多用户聊天室应用](https://medium.com/@kansi/chatbus-build-your-first-multi-user-chat-room-app-with-erlang-otp-b55f72064901)
- [使用Erlang、Rebar、Cowboy和Bullet制作聊天应用程序](http://marianoguerra.org/posts/making-a-chat-app-with-erlang-rebar-cowboy-and-bullet.html)

## F#：

- [用100行F#编写自己的Excel](http://tomasp.net/blog/2018/write-your-own-excel)

## Java：

- [构建解释器](http://www.craftinginterpreters.com/)（第4-13章使用Java编写）
- [使用Java构建简单的HTTP服务器](http://javarevisited.blogspot.com/2015/06/how-to-create-http-server-in-java-serversocket-example.html)
- [使用Java构建Android手电筒应用](https://www.youtube.com/watch?v=dhWL4DC7Krs)（视频）
- [使用Spring Boot构建具有用户身份验证的Web应用程序](https://spring.io/guides/gs/securing-web/)

## JavaScript：

- [在30天内通过30个教程构建30个东西](https://javascript30.com)
- [纯JS构建应用程序](https://medium.com/codingthesmartway-com-blog/pure-javascript-building-a-real-world-application-from-scratch-5213591cfcd6)
- [构建Jupyter Notebook扩展](https://link.medium.com/wWUO7TN8SS)
- [使用JavaScript构建TicTacToe游戏](https://medium.com/javascript-in-plain-english/build-tic-tac-toe-game-using-javascript-3afba3c8fdcc)
- [使用Vanilla JavaScript构建简单的天气应用程序](https://webdesign.tutsplus.com/tutorials/build-a-simple-weather-app-with-vanilla-javascript--cms-33893)
- [使用JavaScript构建Todo List应用程序](https://github.com/dwyl/javascript-todo-list-tutorial)

## HTML和CSS：

- [构建加载屏幕](https://medium.freecodecamp.org/how-to-build-a-delightful-loading-screen-in-5-minutes-847991da509f)
- [使用JS构建HTML计算器](https://medium.freecodecamp.org/how-to-build-an-html-calculator-app-from-scratch-using-javascript-4454b8714b98)
- [仅使用JavaScript、HTML和CSS构建Snake](https://www.freecodecamp.org/news/think-like-a-programmer-how-to-build-snake-using-only-javascript-html-and-css-7b1479c3339e/)

### 移动应用：

- [构建React Native Todo应用程序](https://egghead.io/courses/build-a-react-native-todo-application)
- [使用Redux Thunk构建React Native应用程序](https://medium.com/@alialhaddad/how-to-use-redux-thunk-in-react-and-react-native-4743a1321bd0)

### Web应用：

#### React：

- [创建无服务器的React.js应用](http://serverless-stack.com/)
- [创建一个Trello克隆](http://codeloveandboards.com/blog/2016/01/04/trello-tribute-with-phoenix-and-react-pt-1/)
- [使用React、Node、MongoDB和SocketIO创建角色投票应用](http://sahatyalkabov.com/create-a-character-voting-app-using-react-nodejs-mongodb-and-socketio)
- [React教程：克隆Yelp](https://www.fullstackreact.com/articles/react-tutorial-cloning-yelp/)
- [使用Mocha、React、Redux和Immutable进行全栈电影投票应用的测试驱动开发](https://teropa.info/blog/2015/09/10/full-stack-redux-tutorial.html)
- [使用React和Node构建Twitter流](https://scotch.io/tutorials/build-a-real-time-twitter-stream-with-node-and-react-js)
- [使用React.js和Node.js创建简单的Medium克隆](https://medium.com/@kris101/clone-medium-on-node-js-and-react-js-731cdfbb6878)
- [在JS中集成MailChimp](https://medium.freecodecamp.org/how-to-integrate-mailchimp-in-a-javascript-web-app-2a889fb43f6f)
- [使用React + Parcel构建Chrome扩展](https://medium.freecodecamp.org/building-chrome-extensions-in-react-parcel-79d0240dd58f)
- [使用React Native构建ToDo应用](https://blog.hasura.io/tutorial-fullstack-react-native-with-graphql-and-authentication-18183d13373a)
- [制作聊天应用](https://medium.freecodecamp.org/how-to-build-a-chat-application-using-react-redux-redux-saga-and-web-sockets-47423e4bc21a)
- [使用React Native创建新闻应用](https://medium.freecodecamp.org/create-a-news-app-using-react-native-ced249263627)
- [学习React的Webpack](https://medium.freecodecamp.org/learn-webpack-for-react-a36d4cac5060)
- [使用Puppeteer和Jest测试React应用](https://blog.bitsrc.io/testing-your-react-app-with-puppeteer-and-jest-c72b3dfcde59)
- [构建自己的React脚手架](https://medium.freecodecamp.org/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f)
- [使用React创建生命游戏](https://medium.freecodecamp.org/create-gameoflife-with-react-in-one-hour-8e686a410174)
- [基本的React+Redux入门教程](https://hackernoon.com/a-basic-react-redux-introductory-tutorial-adcc681eeb5e)
- [构建预约调度器](https://hackernoon.com/build-an-appointment-scheduler-using-react-twilio-and-cosmic-js-95377f6d1040)
- [使用情感分析构建带有React的聊天应用](https://codeburst.io/build-a-chat-app-with-sentiment-analysis-using-next-js-c43ebf3ea643)
- [构建全栈Web应用程序设置](https://hackernoon.com/full-stack-web-application-using-react-node-js-express-and-webpack-97dbd5b9d708)
- [使用React和Firebase创建Todoist克隆](https://www.youtube.com/watch?v=hT3j87FMR6M)
- 构建一个随机引用机器
  - [第1部分](https://www.youtube.com/watch?v=3QngsWA9IEE)
  - [第2部分](https://www.youtube.com/watch?v=XnoTmO06OYo)
  - [第3部分](https://www.youtube.com/watch?v=us51Jne67_I)
  - [第4部分](https://www.youtube.com/watch?v=iZx7hqHb5MU)
  - [第5部分](https://www.youtube.com/watch?v=lpba9vBqXl0)
  - [第6部分](https://www.youtube.com/watch?v=Jvp8j6zrFHE)
  - [第7部分](https://www.youtube.com/watch?v=M_hFfrN8_PQ)
- [React手机电商项目(视频)](https://www.youtube.com/watch?v=-edmQKcOW8s)

#### Angular：

- [使用Angular 1.x构建Instagram克隆](https://hackhands.com/building-instagram-clone-angularjs-satellizer-nodejs-mongodb/)
- 使用Angular 2+构建支持离线的Hacker News客户端
  - [第1部分](https://houssein.me/angular2-hacker-news)
  - [第2部分](https://houssein.me/progressive-angular-applications)
- [使用Django和AngularJS（Angular 1.x）构建Google+克隆](https://thinkster.io/django-angularjs-tutorial)
- [使用Angular 8构建美丽的现实应用程序](https://medium.com/@hamedbaatour/build-a-real-world-beautiful-web-app-with-angular-6-a-to-z-ultimate-guide-2018-part-i-e121dd1d55e)
  - [第I部分](https://medium.com/@hamedbaatour/build-a-real-world-beautiful-web-app-with-angular-8-the-ultimate-guide-2019-part-ii-fe70852b2d6d)
- [使用BootStrap 4和Angular 6构建响应式布局](https://medium.com/@tomastrajan/how-to-build-responsive-layouts-with-bootstrap-4-and-angular-6-cfbb108d797b)
- 使用Angular 5构建ToDo应用
  - [Angular简介](http://www.discoversdk.com/blog/intro-to-angular-and-the-evolution-of-the-web)
  - [第1部分](http://www.discoversdk.com/blog/angular-5-to-do-list-app-part-1)

#### Node：

- [使用NodeJS构建实时Markdown编辑器](https://scotch.io/tutorials/building-a-real-time-markdown-viewer)
- [使用Node、Postgres和Knex进行测试驱动开发](http://mherman.org/blog/2016/04/28/test-driven-development-with-node/)
- 使用Node.js编写Twitter机器人
  - [第1部分](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-in-just-38-lines-of-code-ed92db9eb078)
  - [第2部分](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-part-2-do-more-2ef1e039715d)
- [在30分钟内构建

一个简单的搜索机器人](https://medium.freecodecamp.org/how-to-build-a-simple-search-bot-in-30-minutes-eb56fcedcdb1)
- [构建一个作业抓取Web应用](https://medium.freecodecamp.org/how-i-built-a-job-scraping-web-app-using-node-js-and-indreed-7fbba124bbdc)
- [构建GitHub应用](https://blog.scottlogic.com/2017/05/22/gifbot-github-integration.html)
- 如何使用JavaScript、Node.JS、MongoDB和Web Sockets构建自己的Uber-for-X应用
  - [第1部分](https://www.ashwinhariharan.tech/blog/how-to-build-your-own-uber-for-x-app/)
  - [第2部分](https://www.ashwinhariharan.tech/blog/how-to-build-your-own-uber-for-x-app-part-2/)

#### Vue：

- [Vue 2 + Firebase：在15分钟内构建具有Firebase身份验证系统的Vue应用](https://medium.com/@anas.mammeri/vue-2-firebase-how-to-build-a-vue-app-with-firebase-authentication-system-in-15-minutes-fdce6f289c3c)
- [Vue.js应用教程 - 使用Vue创建一个简单的预算应用程序](https://matthiashager.com/complete-vuejs-application-tutorial/)
- [使用Vue、GraphQL和Apollo构建博客](https://scotch.io/tutorials/build-a-blog-with-vue-graphql-and-apollo-client)
- 使用MEVN（MongoDB、Express、Vue、Node）堆栈构建全栈Web应用程序
  - [第1部分](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0)
  - [第2部分](https://medium.com/@anaida07/mevn-stack-application-part-2-2-9ebcf8a22753)
- [Vue.js待办事项列表教程(视频)](https://www.youtube.com/watch?v=78tNYZUS-ps)
- [Vue 2 + Pub/Sub：构建用于游戏的点对点多用户平台](https://www.ably.io/tutorials/peer-to-peer-vue)

#### 其他（Hapi、Express...）：

- 构建渐进式Web应用程序（PWA）
  - [第1部分](https://bitsofco.de/bitsofcode-pwa-part-1-offline-first-with-service-worker/)
  - [第2部分](https://bitsofco.de/bitsofcode-pwa-part-2-instant-loading-with-indexeddb/)
  - [第3部分](https://bitsofco.de/bitsofcode-pwa-part-3-push-notifications/)
- [使用JS构建本机桌面应用](https://medium.freecodecamp.org/build-native-desktop-apps-with-javascript-a49ede90d8e9)
- 使用NodeJs、GraphQL和Hapi构建强大的API
  - [第I部分](https://medium.freecodecamp.org/how-to-setup-a-powerful-api-with-nodejs-graphql-mongodb-hapi-and-swagger-e251ac189649)

#### D3.js

- [使用示例学习D3](https://www.sitepoint.com/d3-js-data-visualizations/)
- [学会制作线图](https://medium.freecodecamp.org/learn-to-create-a-line-chart-using-d3-js-4f43f1ee716b)

### 游戏开发：

- [使用Phaser制作2D Breakout游戏](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_breakout_game_Phaser)
- 使用Phaser在HTML5和JavaScript中制作Flappy Bird
  - [第1部分](http://www.lessmilk.com/tutorial/flappy-bird-phaser-1)
  - [第2部分](http://www.lessmilk.com/tutorial/flappy-bird-phaser-2)

### 桌面应用：

- [使用React和Electron构建桌面聊天应用](https://medium.freecodecamp.org/build-a-desktop-chat-app-with-react-electron-and-chatkit-744d168e6f2f)

### 杂项：

- [如何在不到20行代码内构建Web框架](https://www.pubnub.com/blog/build-yourself-a-web-framework-in-less-than-20-lines-of-code/)
- [构建自己的Redux](https://zapier.com/engineering/how-to-build-redux/)
- [如何编写自己的虚拟DOM](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)
- [使用AWS构建具有WebSockets的实时Serverless GraphQL API](https://andrewgriffithsonline.com/blog/serverless-websockets-on-aws/)

## Kotlin：

- [Keddit - 在开发Android应用的同时学习Kotlin](https://medium.com/@juanchosaravia/learn-kotlin-while-developing-an-android-app-introduction-567e21ff9664)

## Lua:

### LÖVE：

- BYTEPATH：使用Lua和LÖVE创建完整游戏
  - [第0部分：介绍](https://github.com/SSYGEN/blog/issues/30)
  - [第1部分：游戏循环](https://github.com/SSYGEN/blog/issues/15)
  - [第2部分：库](https://github.com/SSYGEN/blog/issues/16)
  - [第3部分：房间和区域](https://github.com/SSYGEN/blog/issues/17)
  - [第4部分：练习](https://github.com/SSYGEN/blog/issues/18)
  - [第5部分：游戏基础](https://github.com/SSYGEN/blog/issues/19)
  - [第6部分：玩家基础](https://github.com/SSYGEN/blog/issues/20)
  - [第7部分：玩家统计和攻击](https://github.com/SSYGEN/blog/issues/21)
  - [第8部分：敌人](https://github.com/SSYGEN/blog/issues/22)
  - [第9部分：导演和游戏循环](https://github.com/SSYGEN/blog/issues/23)
  - [第10部分：编码实践](https://github.com/SSYGEN/blog/issues/24)
  - [第11部分：被动技能](https://github.com/SSYGEN/blog/issues/25)
  - [第12部分：更多被动技能](https://github.com/SSYGEN/blog/issues/26)
  - [第13部分：技能树](https://github.com/SSYGEN/blog/issues/27)
  - [第14部分：控制台](https://github.com/SSYGEN/blog/issues/28)
  - [第15部分：最终](https://github.com/SSYGEN/blog/issues/29)

## Python:

### Web Scraping:

- [使用Python挖掘Twitter数据](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)
- [使用Scrapy和MongoDB爬取网站](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
- [如何使用Python和Selenium WebDriver进行网页抓取](http://www.byperth.com/2018/04/25/guide-web-scraping-101-what-you-need-to-know-and-how-to-scrape-with-python-selenium-webdriver/)
- [使用BeautifulSoup选择电影](https://medium.com/@nishantsahoo.in/which-movie-should-i-watch-5c83a3c0f5b1)

### Web Applications:

- [使用Flask构建微博](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [在Django中创建博客Web应用程序](https://tutorial.djangogirls.org/en/)
- [选择自己的冒险演示](https://www.twilio.com/blog/2015/03/choose-your-own-adventures-presentations-wizard-mode-part-1-of-3.html)
- [使用Flask和RethinkDB构建待办事项列表](https://realpython.com/blog/python/rethink-flask-a-simple-todo-list-powered-by-flask-and-rethinkdb/)
- [使用Django和测试驱动开发构建待办事项列表](http://www.obeythetestinggoat.com/)
- [在Python中构建RESTful微服务](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/)
- [Docker、Flask和React构建微服务](https://testdriven.io/)
- [使用Flask创建简单的Web应用程序](https://pythonspot.com/flask-web-app-with-python/)
- [在不到20分钟内创建Django API](https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3)
- 使用Django、Postgres和JavaScript构建社区驱动的交付应用程序
  - [第1部分](https://www.ashwinhariharan.tech/blog/thinking-of-building-a-contact-tracing-application-heres-what-you-can-do-instead/)
  - [第2部分](https://www.ashwinhariharan.tech/blog/thinking-of-building-a-contact-tracing-application-heres-what-you-can-do-instead-part-2/)
- 使用Vue、django-notifs、RabbitMQ和uWSGI构建实时聊天应用程序
  - [第1部分](https://danidee10.github.io/2018/01/01/realtime-django-1.html)
  - [第2部分](https://danidee10.github.io/2018/01/03/realtime-django-2.html)
  - [第3部分](https://danidee10.github.io/2018/01/07/realtime-django-3.html)
  - [第4部分](https://danidee10.github.io/2018/01/10/realtime-django-4.html)
  - [第5部分](https://danidee10.github.io/2018/01/13/realtime-django-5.html)
  - [第6部分](https://danidee10.github.io/2018/03/12/realtime-django-6.html)

### Bots:

- [构建Reddit机器人](http://pythonforengineers.com/build-a-reddit-bot-part-1/)
- [如何制作Reddit机器人 - YouTube](https://www.youtube.com/watch?v=krTUf7BpTc0) (视频)
- [构建Facebook Messenger机器人](https://blog.hartleybrody.com/fb-messenger-bot/)
- [制作Reddit + Facebook Messenger机器人](https://pythontips.com/2017/04/13/making-a-reddit-facebook-messenger-bot/)
- 使用Python创建Telegram机器人
  - [第1部分](https://khashtamov.com/en/how-to-create-a-telegram-bot-using-python/)
  - [第2部分](https://khashtamov.com/en/how-to-deploy-telegram-bot-django/)
- [在Python中创建Twitter机器人](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607)

### 数据科学:

- 通过执行多个项目学习Python数据科学 (视频):
  - [第1部分：介绍](https://www.youtube.com/watch?v=T5pRlIbr6gg)
  - [第2部分：Twitter情感分析](https://www.youtube.com/watch?v=o_OZdbCzHUA)
  - [第3部分：推荐系统](https://www.youtube.com/watch?v=9gBC9R-msAk&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=3)
  - [第4部分：预测股票价格](https://www.youtube.com/watch?v=SSu00IRRraY&index=4&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)
  - [第5部分：TensorFlow中的Deep Dream](https://www.youtube.com/watch?v=MrBzgvUNr4w&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=5)
  - [第6部分：遗传算法](https://www.youtube.com/watch?v=dSofAXnnFrY&index=6&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)

### 机器学习:

- [用Python从头开始编写线性回归](https://www.youtube.com/watch?v=uwwWVAgJBcM) (视频)
- [Python中的逐步机器学习](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
- [预测葡萄酒质量](https://medium.freecodecamp.org/using-machine-learning-to-predict-the-quality-of-wines-9e2e13d7480d)
- [解决水果分类问题](https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2)
- [使用Python学习无监督学习](https://scikit-learn.org/stable/unsupervised_learning.html)
- [用Python从头开始构建自己的神经网络](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
- [在Python中使用sklearn进行线性回归](https://medium.com/we-are-orb/linear-regression-in-python-without-scikit-learn-50aef4b8d122)
- [在Python中进行多元线性回归，不使用sklearn](https://medium.com/we-are-orb/multivariate-linear-regression-in-python-without-scikit-learn-7091b1d45905)
- [使用KNN创建音乐推荐系统](https://towardsdatascience.com/how-to-build-a-simple-song-recommender-296fcbc8c85)
- 查找相似的Quora问题 -
  - [使用BOW、TFIDF和Xgboost](https://towardsdatascience.com/finding-similar-quora-questions-with-bow-tfidf-and-random-forest-c54ad88d1370)
  - [使用Word2Vec和Xgboost](https://towardsdatascience.com/finding-similar-quora-questions-with-word2vec-and-xgboost-1a19ad272c0d)
- [使用Python和机器学习检测虚假新闻](https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/)

### OpenCV：

- [构建文档扫描仪](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [使用OpenCV和深度学习构建人脸检测器](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
- [使用YOLOv3构建最快的自定义目标检测系统（视频播放列表）](https://www.youtube.com/playlist?list=PLKHYJbyeQ1a0oGzgRXy-QwAN1tSV4XZxg)
- [使用OpenCV、Python和深度学习构建人脸识别系统](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
- [检测图像中的显著特征](https://www.pyimagesearch.com/2018/07/16/opencv-saliency-detection/)
- [构建条形码扫描仪](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)
- [学习使用Python进行人脸聚类](https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/)
- [使用Camshift进行目标跟踪](https://www.pyimagesearch.com/wp-content/uploads/2014/11/opencv_crash_course_camshift.pdf)
- [使用OpenCV和深度学习进行语义分割](https://www.pyimagesearch.com/2018/09/03/semantic-segmentation-with-opencv-and-deep-learning/)
- [图像和视频中的文本检测](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)
- [使用OpenCV的人流计数器](https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/)
- [使用OpenCV跟踪多个对象](https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/)
- [使用OpenCV进行神经风格转移](https://www.pyimagesearch.com/2018/08/27/neural-style-transfer-with-opencv/)
- [OpenCV OCR和文本识别](https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/)
- [文本斜率校正教程](https://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/)
- [面部标志检测教程](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)
- [使用Mask-R-CNN进行目标检测](https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/)
- [自动目标检测教程](https://www.pyimagesearch.com/2015/05/04/target-acquired-finding-targets-in-drone-and-quadcopter-video-streams-using-python-and-opencv/)
- [使用OpenCV的EigenFaces](https://www.learnopencv.com/eigenface-using-opencv-c-python/)
- [更快的（5点）面部标志检测教程](https://www.pyimagesearch.com/2018/04/02/faster-facial-landmark-detector-with-dlib/)
- [手部关键点检测](https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/)
- Dlib相关对象跟踪 -
  - [单个对象跟踪器](https://www.pyimagesearch.com/2018/10/22/object-tracking-with-dlib/)
  - [多对象跟踪器](https://www.pyimagesearch.com/2018/10/29/multi-object-tracking-with-dlib/)
- [使用OpenCV和Python进行图像拼接](https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/)
- [使用OpenCV进行实例分割](https://www.pyimagesearch.com/2018/11/26/instance-segmentation-with-opencv/)
- [面罩检测器](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

### 深度学习：

- [使用卷积神经网络检测面部关键点](http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/)
- [使用Python和OpenCV生成平均面](https://www.learnopencv.com/average-face-opencv-c-python-tutorial/)
- [使用CNN打破验证码系统](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710)
- [使用预训练的Inception模型进行图像预测](https://medium.com/google-cloud/keras-inception-v3-on-google-compute-engine-a54918b0058)
- [创建你的第一个CNN](https://hackernoon.com/deep-learning-cnns-in-tensorflow-with-gpus-cba6efe0acc2)
- [构建人脸识别流水线](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)
- [构建图像字幕生成器](https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f)
- [制作你自己的人脸识别系统](https://medium.freecodecamp.org/making-your-own-face-recognition-system-29a8e728107c)
- [在20分钟内训练语言检测AI](https://towardsdatascience.com/how-i-trained-a-language-detection-ai-in-20-minutes-with-a-97-accuracy-fdeca0fb7724)
- [基于神经网络的目标检测](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)
- 学习Twitter情感分析 -
  - [第I部分 - 数据清理

](https://towardsdatascience.com/another-twitter-sentiment-analysis-bb5b01ebad90)
  - [第II部分 - EDA，数据可视化](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-2-333514854913)
  - [第III部分 - Zipf定律，数据可视化](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-3-zipfs-law-data-visualisation-fc9eadda71e7)
  - [第IV部分 - 特征提取（计数矢量化器）](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-4-count-vectorizer-b3f4944e51b5)
  - [第V部分 - 特征提取（Tfidf矢量化器）](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-5-50b4e87d9bdd)
  - [第VI部分 - Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-6-doc2vec-603f11832504)
  - [第VII部分 - 短语建模 + Doc2Vec](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-7-phrase-modeling-doc2vec-592a8a996867)
  - [第VIII部分 - 降维](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-8-dimensionality-reduction-chi2-pca-c6d06fb3fcf3)
  - [第IX部分 - 使用Tfdif矢量的神经网络](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-9-neural-networks-with-tfidf-vectors-using-d0b4af6be6d7)
  - [第X部分 - 使用word2vec/doc2vec的神经网络](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-10-neural-network-with-a6441269aa3c)
  - [第XI部分 - 使用Word2Vec的CNN](https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-11-cnn-word2vec-41f5e28eda74)
- [使用迁移学习进行自定义图像分类](https://becominghuman.ai/transfer-learning-retraining-inception-v3-for-custom-image-classification-2820f653c557)
- [用11行Python代码编写简单的神经网络](https://iamtrask.github.io/2015/07/12/basic-python-network/)
- [使用梯度下降法构建神经网络](https://iamtrask.github.io/2015/07/27/python-network-part2/)
- [训练一个Keras模型生成颜色](https://heartbeat.fritz.ai/how-to-train-a-keras-model-to-generate-colors-3bc79e54971b)
- [使用自定义数据集在Keras上入门](https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/)
- [在Faces94数据集上使用EigenFaces和FisherFaces](https://nicholastsmith.wordpress.com/2016/02/18/eigenfaces-versus-fisherfaces-on-the-faces94-database-with-scikit-learn/)
- [Kaggle MNIST数字识别教程](https://medium.com/@lvarruda/how-to-get-top-2-position-on-kaggles-mnist-digit-recognizer-48185d80a2d4)
- [使用tf.keras进行Fashion MNIST教程](https://medium.freecodecamp.org/hello-deep-learning-fashion-mnist-with-keras-50fcff8cd74a)
- [使用Keras的CNN自动分类根健康](https://www.pyimagesearch.com/2018/10/15/deep-learning-hydroponics-and-medical-marijuana/)
- [Keras vs TensorFlow](https://www.pyimagesearch.com/2018/10/08/keras-vs-tensorflow-which-one-is-better-and-which-one-should-i-learn/)
- [用于疟疾检测的深度学习和医学图像分析](https://www.pyimagesearch.com/2018/12/03/deep-learning-and-medical-image-analysis-with-keras/)
- [使用Keras进行图像分类的迁移学习](https://towardsdatascience.com/transfer-learning-for-image-classification-using-keras-c47ccf09c8c8)
- [在Python中使用CNNS编写笑脸分类器](https://github.com/kylemcdonald/SmileCNN)
- [使用scikit-learn进行自然语言处理](https://towardsdatascience.com/natural-language-processing-count-vectorization-with-scikit-learn-e7804269bb5e)
- [编写Taylor Swift歌词生成器](https://towardsdatascience.com/ai-generates-taylor-swifts-song-lyrics-6fd92a03ef7e)
- [使用PyTorch Lightning进行口罩检测](https://towardsdatascience.com/how-i-built-a-face-mask-detector-for-covid-19-using-pytorch-lightning-67eb3752fd61)

### 杂项：

- [构建一个简单的解释器](https://ruslanspivak.com/lsbasi-part1/)
- [用Python构建一个简单的区块链](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
- [用Python编写一个NoSQL数据库](https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/)
- [使用OpenCV/Python/iOS构建一个加油站扫描仪](https://hackernoon.com/building-a-gas-pump-scanner-with-opencv-python-ios-116fe6c9ae8b)
- [使用Python和Kafka构建一个分布式流处理系统](https://codequs.com/p/S14jQ5UyG/build-a-distributed-streaming-system-with-apache-kafka-and-python)
- [从头开始用纯Python写一个x86-64 JIT编译器](https://csl.name/post/python-jit/)
- 制作一个低级别（Linux）调试器
  - [第1部分](https://blog.asrpo.com/making_a_low_level_debugger)
  - [第2部分：C](https://blog.asrpo.com/making_a_low_level_debugger_part_2)
- 实现一个搜索引擎
  - [第1部分](http://www.ardendertat.com/2011/05/30/how-to-implement-a-search-engine-part-1-create-index/)
  - [第2部分](http://www.ardendertat.com/2011/05/31/how-to-implement-a-search-engine-part-2-query-index/)
  - [第3部分](http://www.ardendertat.com/2011/07/17/how-to-implement-a-search-engine-part-3-ranking-tf-idf/)
- [构建生命游戏](https://robertheaton.com/2018/07/20/project-2-game-of-life/)
- [创建终端ASCII艺术](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/)
- [编写一个井字棋AI](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/)
- [创建光照艺术](https://robertheaton.com/2018/11/03/programming-project-4-photomosaics/)
- [在终端中构建游戏“Snake”](https://robertheaton.com/2018/12/02/programming-project-5-snake/)
- [写一个Git](https://wyag.thb.lt/)
- [Python字节码运行器的Python实现](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
- [使用Python创建语音助手](https://www.geeksforgeeks.org/voice-assistant-using-python/)

## Go：

- [使用Golang、Angular 2和WebSocket创建实时聊天应用](https://www.thepolyglotdeveloper.com/2016/12/create-real-time-chat-app-golang-angular-2-websockets/)
- [使用Gin构建Go Web应用程序和微服务](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin)
- [如何使用Godog进行Go中的行为驱动开发](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go)
- 在Go中构建区块链
  - [第1部分：基本原型](https://jeiwan.net/posts/building-blockchain-in-go-part-1/)
  - [第2部分：工作证明](https://jeiwan.net/posts/building-blockchain-in-go-part-2/)
  - [第3部分：持久性和CLI](https://jeiwan.net/posts/building-blockchain-in-go-part-3/)
  - [第4部分：交易1](https://jeiwan.net/posts/building-blockchain-in-go-part-4/)
  - [第5部分：地址](https://jeiwan.net/posts/building-blockchain-in-go-part-5/)
  - [第6部分：交易2](https://jeiwan.net/posts/building-blockchain-in-go-part-6/)
  - [第7部分：网络](https://jeiwan.net/posts/building-blockchain-in-go-part-7/)
- [在Go中从头开始构建容器 - Liz Rice（Microscaling Systems）（视频）](https://www.youtube.com/watch?v=8fi7uSYlOdc)
- [使用GoLang构建Web应用程序](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/)
- 在Go中使用ReactJS构建聊天应用程序
  - [第1部分：初始设置](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-1-initial-setup/)
  - [第2部分：简单通信](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-2-simple-communication/)
  - [第3部分：设计我们的前端](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-3-designing-our-frontend/)
  - [第4部分：处理多个客户端](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-4-handling-multiple-clients/)
  - [第5部分：改进前端](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-5-improved-frontend/)
  - [第6部分：将后端Docker化](https://tutorialedge.net/projects/chat-system-in-go-and-react/part-6-dockerizing-your-backend/)
- [Go WebAssembly教程 - 构建计算器教程](https://tutorialedge.net/golang/go-webassembly-tutorial/)
- 在Go中的REST服务器
  - [第1部分 - 标准库](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-1-standard-library/)
  - [第2部分 - 使用路由包](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-2-using-a-router-package/)
  - [第3部分 - 使用Web框架](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-3-using-a-web-framework/)
  - [第4部分 - 使用OpenAPI和Swagger](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-4-using-openapi-and-swagger/)
  - [第5部分 - 中间件](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-5-middleware/)
  - [第6部分 - 身份验证](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-6-authentication/)
  - [第7部分 - GraphQL](https://eli.thegreenplace.net/2021/rest-servers-in-go-part-7-graphql/)
- 在Go中构建URL缩短器 - 使用Gin和Redis
  - [第1部分 - 项目设置](https://www.eddywm.com/lets-build-a-url-shortener-in-go/)
  - [第2部分 - 存储层](https://www.eddywm.com/lets-build-a-url-shortener-in-go-with-redis-part-2-storage-layer/)
  - [第3部分 - 短链接生成器](https://www.eddywm.com/lets-build-a-url-shortener-in-go-part-3-short-link-generation/)
  - [第4部分 - 转发](https://www.eddywm.com/lets-build-a-url-shortener-in-go-part-iv-forwarding/)
- [在Go中构建TCP聊天（视频）](https://www.youtube.com/watch?v=Sphme0BqJiY)
- [从头开始在Go中构建BitTorrent客户端](https://blog.jse.li/posts/torrent/)
- [使用Go、PostgreSQL和Docker制作REST API大师班（视频播放列表）`进行中`](https://www.youtube.com/watch?v=rx6CPDK_5mU&list=PLy_6D98if3ULEtXtNSY_2qN21VCKgoQAE)

## PHP：

- [使用Laravel构建博客](https://www.youtube.com/playlist?list=PLwAKR305CRO-Q90J---jXVzbOd4CDRbVx)（视频）
- [用纯PHP制作你自己的博客](http://ilovephp.jondh.me.uk/en/tutorial/make-your-own-blog)
- [使用SilverStripe用实例构建房地产网站](https://www.silverstripe.org/learn/lessons/)
- [使用Laravel 5.4和VueJS构建实时聊天应用程序](https://www.youtube.com/playlist?list=PLXsbBbd36_uVjOFH_P25__XAyGsohXWlv)（视频）
- [构建社交网络：Laravel 5 - Youtube](https://www.youtube.com/playlist?list=PLfdtiltiRHWGGxaR6uFtwZnnbcXqyq8JD)（视频）
- 使用Laravel构建全功能的多租户应用
  - [第0部分：介绍](https://medium.com/@ashokgelal/writing-a-full-featured-multi-tenant-laravel-app-from-scratch-a0e1a7350d9d)
  - [第1部分：设置](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-1-4049a3cc229d)
  - [第2部分：角色和权限](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-2-roles-and-permissions-d9a5bfe5d525)
  - [第3部分：邀请](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-3-invitation-c982dca55eb9)
  - [第4部分：身份验证](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-4-tenancy-aware-authentication-e0ee37270bc8)
  - [第5部分：测试](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-2-unit-tests-96d6dfbf0617)
  - [第6部分：用户配置文件](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-5-user-profile-5c3d0c655f3a)
  - [第7部分：部署](https://medium.com/@ashokgelal/a-full-featured-multi-tenant-app-with-laravel-part-7-deployment-40bb3c895627)
- [从头开始使用Laravel构建CRUD应用程序](https://www.codewall.co.uk/laravel-crud-demo-with-resource-controller-tutorial/)

## OCaml：

- [在OCaml中使用LLVM实现语言](https://llvm.org/docs/tutorial/#kaleidoscope-implementing-a-language-with-llvm-in-objective-caml)
- [在OCaml中编写Game Boy模拟器](https://linoscope.github.io/writing-a-game-boy-emulator-in-ocaml/)

## Ruby：

- [使用Ruby构建网络堆栈](https://medium.com/geckoboard-under-the-hood/how-to-build-a-network-stack-in-ruby-f73aeb1b661b)
- 制作你自己的Redis
  - [第0部分：介绍](https://rohitpaulk.com/articles/redis-0)
  - [第1部分：裸TCP服务器](https://rohitpaulk.com/articles/redis-1)
  - [第2部分：PING <-> PONG](https://rohitpaulk.com/articles/redis-2)
  - [第3部分：并发客户端](https://rohitpaulk.com/articles/redis-3)
  - [第4部分：ECHO](https://rohitpaulk.com/articles/redis-4)
- [在Ruby中重建Git](https://thoughtbot.com/blog/rebuilding-git-in-ruby)

### Ruby on Rails：

- [Ruby on Rails教程](https://www.railstutorial.org/book)
- [使用Ruby on Rails从头开始构建Instagram](https://www.dropbox.com/s/9vq430e9s3q7pu8/Let%27s%20Build%20Instagram%20with%20Ruby%20on%20Rails%20-%20Free%20Edition.pdf?dl=0)
- [使用Rails构建社交网络](https://medium.com/rails-ember-beyond/how-to-build-a-social-network-using-rails-eb31da569233)
- [如何构建Ruby on Rails应用程序](https://www.digitalocean.com/community/tutorials/how-to-build-a-ruby-on-rails-application)

## Haskell:

- [写给你的 Haskell - 构建现代函数式编译器](http://dev.stephendiehl.com/fun/)
- [在48小时内写一个 Scheme](https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours)
- [写给你一个 Scheme，第二版](https://github.com/write-you-a-scheme-v2/scheme)
- [打造你自己的 IRC 机器人](https://wiki.haskell.org/Roll_your_own_IRC_bot)
- [制作 Movie Monad](https://lettier.github.io/posts/2016-08-15-making-movie-monad.html)
- [用 Haskell 制作网站 **（已过时）**](http://adit.io/posts/2013-04-15-making-a-website-with-haskell.html)

## R:

- [使用 Shiny 构建 Web 应用](http://shiny.rstudio.com/tutorial/)
- [构建加密货币机器人](https://towardsdatascience.com/build-a-cryptocurrency-trading-bot-with-r-1445c429e1b1)
- [学习 R 中的关联规则挖掘](https://towardsdatascience.com/association-rule-mining-in-r-ddf2d044ae50)

## Rust:

- Rust 中的简单 Web 应用
  - [第1部分](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-1/)
  - [第2部分a](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-2a/)
  - [第2部分b](http://joelmccracken.github.io/entries/a-simple-web-app-in-rust-pt-2b/)
- [用纯 Rust 编写操作系统](https://os.phil-opp.com/)
- [用 Rust 构建浏览器引擎](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
- [用 Rust 编写微服务](http://www.goldsborough.me/rust/web/tutorial/2018/01/20/17-01-11-writing_a_microservice_in_rust/)
- [通过学习 Rust 过多的链表](http://cglab.ca/~abeinges/blah/too-many-lists/book/README.html)
- Rust 详解：从头开始编写可扩展的聊天服务
  - [第1部分：实现 WebSocket。介绍。](https://nbaksalyar.github.io/2015/07/10/writing-chat-in-rust.html)
  - [第2部分：发送和接收消息](https://nbaksalyar.github.io/2015/11/09/rust-in-detail-2.html)
- [在桌面和Web上用 Rust 编写 Roguelike 游戏](https://aimlesslygoingforward.com/blog/2019/02/09/writing-a-rust-roguelike-for-the-desktop-and-the-web/)
- [使用 Rust 构建单页应用程序](http://www.sheshbabu.com/posts/rust-wasm-yew-single-page-application/)
- [用 Rust 编写 NES 模拟器](https://bugzmanov.github.io/nes_ebook/)
- 创建演变的模拟，使用神经网络和遗传算法，并将应用程序编译为 WebAssembly
  - [第1部分](https://pwy.io/en/posts/learning-to-fly-pt1/)
  - [第2部分](https://pwy.io/en/posts/learning-to-fly-pt2/)
  - [第3部分](https://pwy.io/en/posts/learning-to-fly-pt3/)
  - [第4部分](https://pwy.io/en/posts/learning-to-fly-pt4/)

## Scala:

- [简单基于 Actor 模型的区块链](https://www.freecodecamp.org/news/how-to-build-a-simple-actor-based-blockchain-aac1e996c177/)
- [没有魔法：正则表达式](https://rcoh.svbtle.com/no-magic-regular-expressions)

## Swift:

- [Hacking with Swift - 通过 39 个项目学 Swift](https://www.hackingwithswift.com/read)
- [从头开始制作复古第一人称射击游戏](https://github.com/nicklockwood/RetroRampage)

## 额外资源

- [React Redux 链接](https://github.com/markerikson/react-redux-links)
- [Udemy.com](https://www.udemy.com/)
- [Full Stack Python](https://www.fullstackpython.com/)
- [Node School](https://nodeschool.io/)
- [ScotchIO](https://scotch.io/)
- [Exercism](http://www.exercism.io/)
- [Egghead.io](http://www.egghead.io/)
- [Michael Herman's Blog](http://mherman.org/)
- [Thinkster.io](http://thinkster.io)
- [Enlight](https://enlight.nyc/)
- [Hack Club Workshops](https://hackclub.com/workshops/)
- [CodeCrafters](https://codecrafters.io/)
