# myblog

##个人博客系统
* 前端使用vue
* css框架使用prue
* 后端使用flask

##博客地址
[url](http://193.112.41.53:8099)

##博客后台展示地址
[adminurl](https://blog.csdn.net/u013055678/article/details/80114555)

##vue涉及到的知识点
* vuex,vuex与sessionstorage组合(解决传值以后刷新没有数据的问题)
* vue-router,router路由过滤(检测状态)，router子路由
* 导入jquery,使用富文本编辑器summernote
* 子父组件props传值
* 分页组件

##flask涉及到的知识点
* 跨域问题
* redis状态验证
* 数据库操作

##问题
vue的summernote组件初始化以后出现一个.popover元素,开发时display:none直接隐藏掉,但是打包以后放入nginx中又显示了,于是我室直接修改打包以后的css文件,这个情况在直接使用jquery代码实现的summernote没有出现,使用npm安装会出现
