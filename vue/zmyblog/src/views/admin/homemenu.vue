<template>
<div>
  <div class="pure-menu pure-menu-horizontal">
    <a @click="submit()"><router-link to="/adminhome/home" class="pure-menu-heading pure-menu-link" >首页</router-link></a>
    <ul class="pure-menu-list">
        <li class="pure-menu-item"><router-link to="/adminhome/user" class="pure-menu-link">个人信息</router-link></li>
        <li class="pure-menu-item"><router-link to="/adminhome/type" class="pure-menu-link">分类管理</router-link></li>
        <li class="pure-menu-item"><router-link to="/adminhome/conlist" class="pure-menu-link">文章管理</router-link></li>
    </ul>
</div>
</div>
</template>

<script>
export default {
  	methods:{
  		submit(){
  			this.$store.dispatch('setsummernotecommit',{});
  		}
  	}
}
</script>

<style scoped>
.pure-menu {
    width: 100%;
    height: 38px;
    background-color: burlywood;
}
a{
	text-decoration:none;
}
</style>

