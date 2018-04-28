// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
//目录下文件名是index.js可以直接引用
import router from './router'
import store from'./store'
import Vuex from 'vuex'
import axios from 'axios'  
import VueAxios from 'vue-axios'
//全局引入样式
import "../src/assets/css/pure-min.css"
import "../src/assets/css/grids-responsive-min.css"
//summernote依赖库
import "bootstrap/dist/js/bootstrap.bundle.min.js"
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.min.js"
import "font-awesome/css/font-awesome.css"
import "summernote"
import "summernote/dist/lang/summernote-zh-CN.js"
import "summernote/dist/summernote.css"
   
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  contents:{},
  el: '#app',
  //路由
  router,
  store,
  components: { App },
  template: '<App/>',
})

