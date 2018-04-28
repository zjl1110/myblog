<template>
	<div class="typexx">
		所有类型：
		<div id="types" v-for="(muenx,index) in muens">
			<div class="typea">
				<input class="typex" type="text" v-model="muenx.type" required/>
				<button @click="removetype(muenx.id,index)">删除</button>
				<button @click="settype(muenx.id,muenx.type)">修改提交</button>
			</div>
		</div>
		添加类型:
		<div v-for="new_muenx in new_muens">
			<input  type="text" v-model="new_muenx.typedata" required/>
			<button @click="addtypedata(new_muenx.typedata)">确认添加</button>
		</div>
		<button @click="addtype">添加类型</button>
	</div>
</template>

<script>
import {getmenulise,hostip} from "../../assets/js/setajax.js";
import {getCookie} from "../../assets/js/cookietools.js";

export default{
	data(){
		return {
			typelist:"",
			muens:this.$store.getters.gettypelist,
			muenx:"",
			new_muens:[{typedata:""}],
		}
	},
	methods:{
		//删除类型
		removetype(id,index){
			let qs = require('qs');
            	let params = qs.stringify({
                'typeid': id,
                'username': getCookie("username"),
                "token":getCookie("token"),
            });
            this.axios.post(hostip+"/deltype",params
				).then((response) =>{
					if(response.data.login!="1"){
						this.$router.push("/admin")
					}
					if(response.data.code=="0"){
						alert("类型删除成功");
						//删除input
						this.muens.splice(index, 1);
						getmenulise();
					}else{
						alert(response.data.code);
					}
				   }).catch((error)=> {
	            　　alert(error);
	           });
		},
		//修改类型
		settype(id,data){
			if(!data){
				alert("不能为空");
			}else{
				let qs = require('qs');
	            	let params = qs.stringify({
	                'contenttype': data,
	                "typeid":id,
	                'username': getCookie("username"),
	                "token":getCookie("token"),
	            });
	            this.axios.post(hostip+"/settype",params
				).then((response) =>{
					if(response.data.login!="1"){
						this.$router.push("/admin")
					}
					if(response.data.code=="0"){
						alert("类型修改成功");
						getmenulise();
					}else{
						alert(response.data.code);
					}
				   }).catch((error)=> {
	            　　alert(error);
	           });
			}
		},
		addtype(){
			//添加输入框
			this.new_muens.push({typedata:""});	
		},
		//添加类型
		addtypedata(data){
			if(!data){
				alert("不能为空");
			}else{
				let qs = require('qs');
	            	let params = qs.stringify({
	                'contenttype': data,
	                'username': getCookie("username"),
	                "token":getCookie("token"),
	            });
	             this.axios.post(hostip+"/addtype",params
				).then((response) =>{
					if(response.data.login!="1"){
						this.$router.push("/admin")
					}
					if(response.data.code=="0"){
						alert("类型添加成功");
						getmenulise();
					}else{
						alert(response.data.code);
					}
				   }).catch((error)=> {
	            　　alert(error);
	           });
	       }
		}
	}
}
</script>

<style scoped>
.typex{
	display: block;
}
.typea{
	margin: 20px;
}
.typexx{
	margin: 20px 0 0 10%;
}
</style>