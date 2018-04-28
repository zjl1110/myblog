<template>
<div>
    <form class="pure-form pure-form-stacked" @submit.prevent="postuserdata">
        <fieldset>
            <legend>后台登入</legend>
            <p v-show="show_data" class="showdata">{{show_data}}</p>
            <label for="username">用户名</label>
            <input id="username" name="username" type="text" v-model="inputtext.name" placeholder="用户名" pattern="^[A-Za-z0-9.]*$" required>
    
            <label for="password">密码</label>
            <input id="password" name="password" type="password" v-model="inputtext.password" placeholder="密码" pattern="^[A-Za-z0-9.]*$" required>
    
            <button type="submit" class="pure-button pure-button-primary" >提交</button>
        </fieldset>
	</form>
</div> 
</template>
<script>
import md5 from 'js-md5';
import {setCookie,getCookie} from "../../assets/js/cookietools.js";
import {hostip} from "../../assets/js/setajax.js";

export default {
    data(){
        return {
            inputtext:{},
            paramsdata:{},
            show_data:false,
        }
    },
    mounted(){
    },
    methods:{
    	//登入
        postuserdata:function(){
            var qs = require('qs');
            this.paramsdata = qs.stringify({
                'username': this.inputtext.name,
                'password': md5(this.inputtext.password)
            })
        		console.log(this.paramsdata);
            this.axios.post(hostip+"/login",this.paramsdata).then((response) =>{
                    console.log(response.data);
                    if(response.data.code=="0"){
                        setCookie("token",response.data.token,1000*60);
                        setCookie("username",response.data.username,1000*60);
                        this.show_data = "登入成功";
                        setTimeout(function(){  
                            this.$router.push("/adminhome/home")
                        }.bind(this),1000);
                    }else{
                        this.show_data = "登入失败";
                    }
                }).catch((error)=> {
                　　alert(error);
                });
        }
    },

}
</script>
<style scoped>
form{
    margin: 10% 0 0 30%;
}
.showdata{
    color: red;
}
</style>
