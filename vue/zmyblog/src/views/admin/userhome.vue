<template>
	<div id="con">
            <img width="108" height="108" alt="img" class="post-avatar" :src="userimg">
            <div>
            	修改头像:
                <input  name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="onUploadimg($event)"/>
                <button @click="submitImg($event)">提交</button>
            	</div>
	        <div class="content">
	        		用户名:
	            <h1 class="brand-title">{{ username }}</h1>
	            <div>简介:</div>
                <textarea rows="5" cols="40" class="brand-tagline" v-model="userintroduction"></textarea>
                <button @click="setintroduction">修改简介</button>
                <div class="new pasw">新密码:<input type="password" v-model="new_pasw" placeholder="密码" pattern="^[A-Za-z0-9.]*$" required/></div>
                <div class="new pasw">确认密码:<input type="password" v-model="new_pasw_2" placeholder="确认密码" pattern="^[A-Za-z0-9.]*$" required/></div>
                <p v-show="show_data" class="showdata">{{show_data}}</p>
                <input class="pure-button pasw" type="button" value="修改密码" @click="setpassword"/>
                <div>上传简历:
                		<input  name="file" type="file" accept="application/pdf" @change="uppdf($event)"/>
                		<button @click="submitpdf($event)">提交</button>
                </div>
				<div><a class="pure-button" @click="$router.push('/pdfdata')" >简历浏览</a></div>
	        </div>
	   </div>
</template>

<script>
import {getCookie,delCookie} from "../../assets/js/cookietools.js";
import {hostip} from "../../assets/js/setajax.js";
import md5 from 'js-md5';

export default{
    data(){
        return {
            userimg:"",
            username:"",
            userintroduction:"",
            new_pasw:"",
            new_pasw_2:"",
            imgfile:"",
            userid:"",
            show_data:false,
            pdffile:"",
        }
    },
    mounted(){
        this.getintroduction();
    },
    methods:{
    	//获取个人信息
        getintroduction:function(){
            this.axios.get(hostip+"/introduction").then((response) =>{
                console.log(response.data);
                this.userimg = response.data.userimg;
                this.username = response.data.username;
                this.userintroduction = response.data.userintroduction;
                this.userid = response.data.id;
            })
        },
        //获取图片信息
        onUploadimg(event){
        		this.imgfile = event.target.files[0];
        		console.log(this.imgfile);
            
        },
        //上传图片
        submitImg(event) {   // 上传照片
	      let param = new FormData(); //创建form对象  
        		param.append('file',this.imgfile);//通过append向form对象添加数据
        		param.append("token",getCookie("token"));
        		param.append("username",getCookie("username"));
        		param.append("userid",this.userid);
        		param.append("headimg","1");
        		console.log(this.imgfile); //FormData私有类对象，访问不到，可以通过get判断值是否传进去  
	      let config = {
	        headers: {'Content-Type': 'multipart/form-data'}
	      }
	     // 添加请求头
	    this.axios.post(hostip+'/imgupdata', param,config)
	        .then(response => {
	          	if(response.data.login!="1"){
            			this.$router.push("/admin")
            		}
	          	if(response.data.code=="0"){
					alert("头像修改成功");
				}
//	          	this.userimg = response.data.imgurl;
	          console.log(response.data.imgurl)
	          this.userimg = response.data.imgurl;
	        }).catch((error)=> {
            　　alert(error);
            });
	    },
	    //修改简介
	    setintroduction(){
	    		let qs = require('qs');
            	let params = qs.stringify({
                'userid': this.userid,
                'username': getCookie("username"),
                "token":getCookie("token"),
                "content":this.userintroduction,
            });
            	this.axios.post(hostip+"/setintroduction",params
			).then((response) =>{
				if(response.data.login!="1"){
					this.$router.push("/admin")
				}
				if(response.data.code=="0"){
					alert("简介修改成功");
				}
			   }).catch((error)=> {
            　　alert(error);
            });
	    },
	    //修改密码
	    setpassword(){
	    		if(this.new_pasw!=this.new_pasw_2){
	    			this.show_data="两次密码不一致!"
	    		}
	    		else if(!this.new_pasw && !this.new_pasw_2){
	    				this.show_data="密码不能为空且只能是数字与字母组合!"
	    			}else{
	    			let qs = require('qs');
            		let params = qs.stringify({
	                'userid': this.userid,
	                'username': getCookie("username"),
	                "token":getCookie("token"),
	                "password":md5(this.new_pasw),
	            });
	            this.axios.post(hostip+"/setpassword",params
				).then((response) =>{
					if(response.data.login!="1"){
						this.$router.push("/admin")
					}
					if(response.data.code=="0"){
						delCookie("username");
						delCookie("token");
						this.$router.push("/admin");
					}
				   }).catch((error)=> {
	            　　alert(error);
	            });
	    		}
	    },
	    //获取pdf信息
	    uppdf(event){
        		this.pdffile = event.target.files[0];
        		console.log(this.pdffile); 
        },
        //上传pdf
        submitpdf(event) {   // 上传pdf
	      let param = new FormData(); //创建form对象  
        		param.append('file',this.pdffile);//通过append向form对象添加数据
        		param.append("token",getCookie("token"));
        		param.append("username",getCookie("username"));
        		param.append("userid",this.userid);
        		param.append("headimg","1");
        		console.log(this.imgfile); //FormData私有类对象，访问不到，可以通过get判断值是否传进去  
	      let config = {
	        headers: {'Content-Type': 'multipart/form-data'}
	      }
	     // 添加请求头
	    this.axios.post(hostip+'/pdfupdata', param,config)
	        .then(response => {
	          	if(response.data.login!="1"){
            			this.$router.push("/admin")
            		}
	          	if(response.data.code=="0"){
	          		alert("pdf上传成功!");
	          	}
//	          	this.userimg = response.data.imgurl;
	          console.log(response.data.imgurl)
	          this.userimg = response.data.imgurl;
	        }).catch((error)=> {
            　　alert(error);
            });
	    },
     }
}
</script>

<style scoped>
#con{
	margin: 10px 0 0 10%;
}
.pasw{
	margin: 10px;
}
.showdata{
	color: red;
}
</style>