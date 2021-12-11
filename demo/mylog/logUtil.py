import logging.config

# 读取日志配置文件内容
logging.config.fileConfig("loggingconf.conf")

# 创建一个日志器logger
logger = logging.getLogger("simpleExample")

# 日志输出
logger.debug("debug message.")
logger.info("info message.")
logger.warning("warning message.")
logger.error("error message.")
logger.critical("critical message.")


'''
1.关于fileConfig()函数的说明：
该函数实际上是对configparser模块的封装，函数定义：该函数定义在logging.config模块下

logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True)
参数说明：

fname：表示配置文件的文件名或文件对象；
defaults：指定传给ConfigParser的默认值；
disable_existing_loggers：这是一个布尔值，默认值为True(为了向后兼容)表示禁用已经存在的logger，除非它们或它们的祖先明确的出现在日志配置中；如果该值为False，则对已存在的loggers保持启动状态；
2.配置文件格式说明：
上面提到过，fileConfig()函数是对ConfigParser/configparser模块的封装，也就是说fileConfig()函数是基于ConfigParser/configparser模块来理解日志配置文件的。换句话说，fileConfig()函数所能理解的配置文件基础格式是与ConfigParser/configparser模块一致的，因此在此基础上对文件中包含的section和option做了以下规定和限制，比如：

(1)配置文件中一定要包含loggers、handlers、formatters这些section，它们通过keys这个option来指定该配置文件中已经定义好的loggers、handlers和formatters，多个值之间用逗号分隔；另外loggers这个section中的keys一定要包含root这个值；
(2)loggers、handlers、formatters中所所指定的日志器、处理器和格式器都需要在下面单独的section中进行定义。section的命名规则为[logger_loggerName]、[handler_handlerName]、[formatter_formatterName]；
(3)定义logger的section必须指定level和handlers这两个option，level的可取值为DEBUG、INFO、WARNING、ERROR、CRITICAL、NOTSET，其中NOTSET表示所有级别的日志消息都要记录，包括用户定义级别；handlers的值是以逗号分隔的handler名字列表，这里出现的handler必须出现在[handlers]这个section中，并且相应的handler必须在配置文件中有对应的section定义；
(4)对于非root logger来说，除了level和handlers这两个option之外，还需要一些额外的option，其中qualname是必须提供的option，它表示在logger层级中的名字，在应用代码中通过这个名字得到logger；propagate是可选的，其默认值为1，表示消息将会传递给高层次logger的handler，通常我们需要指定其值为0，这个可以看下面的例子；另外，对于非root logger的level如果设置为NOTSET，系统将会查找高层次的logger来决定此logger的有效level；
(5)定义handler的section中必须指定class和args这两个option，level和formatter为可选option；class表示用于创建handler的类名，args表示传递给class所指定的handler类初始化方法参数，它必须是一个元组(tuple)的形式，即便只有一个参数值也需要是一个元组的形式；level与logger中的level一样，而formatter指定的是该处理器所使用的格式器，这里指定的格式器名称必须出现在formatters这个section总，且在配置文件中必须要有这个formatter的section定义；如果不指定formatter则该handler将会以消息本身作为日志消息进行记录，而不添加额外的时间、日志器名称等信息；
(6)定义formatter的section中的option都是可选的，其中包括format用于指定格式字符串，默认为消息字符串本身；datefmt用于指定asctime的时间格式，默认为"%Y-%m-%d %H:%M:%S"；class用于指定格式器类名，默认为logging.Formatter；
说明：配置文件中的class指定类名时，该类名可以是相对于logging模块的相对值，如：FileHandler、handlers.TimeRotatingFileHnadler；也可以是一个绝对路径值，通过普通的import机制来解析，如：自定义的handler类，mypackage.mymodule.MyHandler，但是mypackage需要在Python可用的导入路径中---sys.path

'''
