class MiniOS(object):
    def __init__(self, name):
        self.name = name
        self.apps = []

    def __str__(self):
        return "%s 安装的软件列表为 %s" % (self.name, str(self.apps))

    def install_app(self, app):
        if app.name in self.apps:
            print('已经安装了%s，无需再次安装' % app.name)
        else:
            app.install()
            self.apps.append(app.name)


class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return '%s的当前版本是%s - %s' % (self.name, self.version, self.desc)

    def install(self):
        print('将%s[%s]的执行程序复制到程序目录' % (self.name, self.version))


class PyCharm(App):
    pass


class Chrome(App):
    def install(self):
        print('正在解压缩安装程序...')
        super().install()


linux = MiniOS('Linux')
print(linux)

pychrm = PyCharm('PyChrm', '1.0', 'python的IDE环境')
chrome = Chrome('Chrome', '2.0', '浏览器')

linux.install_app(pychrm)
linux.install_app(chrome)
linux.install_app(chrome)

print(linux)