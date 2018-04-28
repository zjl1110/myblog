<template>
  <!-- 简介列-->
	    <div class="sidebar pure-u-1 pure-u-md-1-4">
            <img width="108" height="108" alt="img" class="post-avatar" :src="userimg">
	        <div class="header">
	            <h1 class="brand-title">{{ username }}</h1>
                <h4 class="brand-tagline">{{ userintroduction }}</h4>
	
	            <nav class="nav">
	                <ul class="nav-list">
	                    <li class="nav-item">
	                        <a class="pure-button" @click="$router.push('/pdfdata')" >简历</a>
	                    </li>
	                    <!-- <li class="nav-item">
	                        <a class="pure-button" href="http://yuilibrary.com">YUI Library</a>
	                    </li> -->
	                </ul>
	            </nav>
	        </div>
	    </div>
</template>

<script>
import { hostip } from '../../assets/js/setajax.js';

export default{
    data(){
        return {
            userimg:"",
            username:"",
            userintroduction:"",
        }
    },
    mounted(){
        this.getintroduction();
    },
    methods:{
    	//个人简介
        getintroduction:function(){
            this.axios.get(hostip+"/introduction").then((response) =>{
                console.log(response.data);
                this.userimg = response.data.userimg;
                this.username = response.data.username;
                this.userintroduction = response.data.userintroduction;
            })
        },
    }
}
</script>

<style scoped>
@import "../../assets/css/blog.css";
.post-avatar{
    margin: 40% 30% 0 0%;
}
</style>



