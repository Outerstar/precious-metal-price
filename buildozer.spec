[app]

# (str) 版本号
version = 1.0

# (str) 应用标题
title = 贵金属实时价格

# (str) 包名
package.name = preciousmetal

# (str) 域名格式的包标识符
package.domain = com.preciousmetal.price

# (str) 源代码目录
source.dir = .

# (list) 要包含的源文件
source.include_exts = py,png,jpg,kv,atlas

# (str) 应用入口点
source.main = main.py

# (list) 模式
android.permissions = INTERNET,SYSTEM_ALERT_WINDOW

# (int) 目标Android API
android.api = 33

# (int) 最低API
android.minapi = 21

# (str) Android SDK版本 (deprecated, use ANDROID_SDK_ROOT env)

# (str) NDK版本
android.ndk = 25b

# (bool) 是否使用--private方式创建发布版
android.release = False

# (str) Android归档输出路径
android.archs = arm64-v8a,armeabi-v7a

# (bool) 是否进行签名
android.sign = True

# (str) 签名密钥（可选）
# android.keystore = my-release-key.keystore

# (str) 签名密钥密码
# android.keypass = password

# (str) 签名别名
# android.keyalias = myalias

# (str) 别名密码
# android.keyaliaspass = password

# (list) 需要包含的Java/JAR包
# android.add_jars = foo.jar,bar.jar

# (list) 需要包含的AAR包
# android.add_aars = foo.aar,bar.aar

# (list) 需要的gradle依赖
# android.gradle_dependencies =

# (list) Java/Android额外活动
# android.activities = MainActivity,OtherActivity

# (list) 添加到AndroidManifest.xml的额外标签
# android.add_manifest =

# (list) Android库项目
# android.library_references =

# (str) Android日志级别
android.logcat_level = warning

# (int) 日志进程数
android.logcat_process = Main

# (bool) 复制库而不是符号链接
android.copy_libs = 1

#
# Python for Android相关设置
#

# (str) python-for-android分支
p4a.branch = master

# (str) Python版本
python3.python = python3.11

# (str) 使用的Python实现
python3.implementation = cpython

# (list) 需要包含的Python模块
requirements = python3,kivy,requests,urllib3,certifi

# (str) 自定义引导菜单
# strp4a.bootstraps =

# (bool) 是否使用PyJNIus
android.use_pyjnius = True

# (bool) 是否使用Android的ctypes
android.use_ctypes = True

# (bool) 使用SDL2
android.use_sdl2 = True

# (list) 需要复制的源文件
# source.copy_files =

#
# Buildozer自定义命令
#

# (list) 构建前执行的命令
# buildozer.pre_cmd =

# (list) 构建后执行的命令
# buildozer.post_cmd =
