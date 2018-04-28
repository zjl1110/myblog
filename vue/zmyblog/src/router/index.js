import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Hhome from '@/views/home/home'
import Pdfdata from '@/views/pdfviews/pdfdata'
import Ccontent from '@/views/content/blogcontent'
import Login from '@/views/admin/login'
import Amain from '@/views/admin/adminmain'
import Ahome from '@/views/admin/home'
import Acontlist from '@/views/admin/contentlist'
import Auser from '@/views/admin/userhome'
import Atype from '@/views/admin/typehome'

Vue.use(Router)

const router = new Router({
  routes: [
  //路由
    {
      path: '/',
      name: 'Hhome',
      component: Hhome
    },
    {
      path:'/pdfdata',
      name:'Pdfdata',
      component:Pdfdata
    },
    {
      path:'/content',
      name:'Ccontent',
      component:Ccontent
    },
    {
      path: '/admin',
      name: 'Login',
      component: Login
    },
    {
      path: '/adminhome',
//    name: 'Amain',
      component: Amain,
      //子路由，meta中存原信息，requiresAuth说明需要验证
      children:[
      	{ path: '/adminhome/home', component: Ahome,meta: { requiresAuth: true } },
      	{ path: '/adminhome/conlist', component: Acontlist,meta: { requiresAuth: true } },
      	{ path: '/adminhome/user', component: Auser,meta: { requiresAuth: true } },
      	{ path: '/adminhome/type', component: Atype,meta: { requiresAuth: true } }
      ],
    },
  ]
});

import {getCookie} from "../assets/js/cookietools.js";
//路由拦截器，没有cookie就跳到登入界面(也可以使用vuex，登入成功后在vuex中添加一个字段用于判断)
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth) {  // 判断该路由是否需要登录权限
        if (getCookie("username")) {  // 通过vuex state获取当前的token是否存在
            next();
        }
        else {
            next({
                path: '/admin',
            })
        }
    }
    else {
        next();
    }
})

export default router;