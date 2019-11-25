### FLASK 项目结构规划
 ##### 创建一个APP包，主要来存放应用
 ###### 在App包中的入口文件中__init__.py中创建Flask程序，并进行初始化
     初始化Flask自己，在Flask上进行设置
     -使用配置文件，在Flask上设置
     -初始化蓝图，也就是初始化Views
     -初始化第三方，初始化ext 
 
####项目结构
    manage.py             用来全局控制我们的项目
    App                    代表项目
       - App/__init__        初始化,使用进行项目初始化
       - App/views        视图面数,用来处理我们的请求
                     -views中使用蓝图进行的突现
       - App/models       模型,用未定义和数据映射的对象的
                  - 使用orm进行实现
       -App/sttings       设置、配置、App应用的配置文件
                   -全局配置
                  -设置多套环境的配置
       -App/ext           扩展库,第三方扩展库统一管理
                  -轻量级框架
                  -第三方插件多,可以统一处理
 
 
#### 配置
 ###### 开发中，可能拥有多套运行环境
        写一个文件，实现多个环境配置
        环境中有很通用的部分，我们可以进行一个代码提取
        
        
#### flask-migrate 
 ###### 数据库迁移
        使用流程
           安装pip install flask- migrate
           进行初始化
               在ext中进行初始化
               迁移库需要同时绑定app和db
        使用方法(原生方法,针对默认结构有效·修改的结构需要额外配置)
             flask db init
             flask db migrate
             flask db upgrade
             flask db downgrade
             flask db.help
        集成fask- script使用
             按照使用流程进行配置
             添加和f1a5 k-scripti对接的代码
             就是在 manager中添加命令 manager. add command("db', Migratecommand)
        使用方法
           python manage.py db init
             初始化·每个项目只调用一次,生成迁移结构
           python manage.py db migrate
             生成迁移文件,会在根目录生成迁移文件调用时机,每次修改mdel之后
           python manage.py db upgrade
             执行迁移文件将修改映射到数据库中,增量的
           python manage.py db downgrade
             执行迁移文件降级操作吃后懈药
           python manage.py db.help
             查看帮助