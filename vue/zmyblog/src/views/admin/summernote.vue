<template>
	<div>
	<div class="typeselect">
		分类:<select v-model="selected">
			<option v-for="typedata in typedatas">{{typedata.type}}</option>
		</select>
		<div>标题:<input type="text" v-model="title"/></div>
	</div>
    <div class="m">		
		<div id="summernote" v-html="summernotecon"></div>
		<button id="edit" class="btn btn-primary" @click="edit()" type="button">编辑</button>
		<button id="save" class="btn btn-primary" @click="save()" type="button">预览</button>
		<button id="submit" class="btn btn-primary" @click="submit()" type="button">提交</button>
    </div>
    </div>
</template>

<script>
import $ from 'jquery';
import {getmenulise,setsummernotecon,hostip} from '../../assets/js/setajax.js'
import {setCookie,getCookie} from "../../assets/js/cookietools.js";

export default {
    data(){
        return {
        		conid:this.$store.getters.getsummernotecon.id,
        		title:this.$store.getters.getsummernotecon.title,
            datax:"",
            selected:this.$store.getters.getsummernotecon.type,
            paramsdata:"",
			typedatas:this.$store.getters.gettypelist,
			summernotecon:this.$store.getters.getsummernotecon.content,
//			title:this.$refs.input.value,
			username:getCookie("username"),
			token:getCookie("token"),
			successdata:"",
        }
    },
    mounted(){
    		//获取menu类型
    		getmenulise(),
    		//初始化summernote
        $('#summernote').summernote({
        height: 200,
        tabsize: 2,
        lang: 'zh-CN',
        placeholder:"输入内容.....",
        toolbar:[
        		['style',['bold','italic','clear']],
        		['fontsize',['fontsize']],
        		['para',['ul','ol','paragraph']],
        		['insert',['picture','link']]
        ],
        callbacks: {
            onImageUpload: function(files) { //回调上传图片函数 
            this.datax = new FormData();  
            this.datax.append("file", files[0]);
            this.datax.append("token",getCookie("token"))
        		this.datax.append("username",getCookie("username"))
                console.log(files[0]);
                // sendFile(files[0]); 
            $.ajax({  
            data: this.datax,  
            type: "POST",  
            url: hostip+"/imgupdata", 
            dataType:"json",
            cache: false,  
            contentType: false,  
            processData: false,  
            success: function(datas) { 
            		if(datas.login!="1"){
            			this.$router.push("/admin")
            		}
                console.log(datas.imgurl);
                $('#summernote').summernote('insertImage', datas.imgurl); // url必须是有效的http  
            },
            error:function(){
                alert("图片上传失败...");
            }  
        }); 
        	}  
		}
    });
    },
    methods:{
    //编辑
    edit(){
    $('#summernote').summernote({height: 200,tabsize: 2,lang: 'zh-CN',focus: true});
    },

    //预览
    save() {
    var markup = $('#summernote').summernote('code');
    $('#summernote').summernote('destroy');
    },
    //提交文章
    submit(){
    		var qs = require('qs');
            this.paramsdata = qs.stringify({
                'title': this.title,
                'content': $('#summernote').summernote('code'),
                'type': this.selected,
                'username': this.username,
                "token":this.token,
                "conid":this.conid
            });
            if(this.title && this.selected){
            		setsummernotecon(this.paramsdata);
            }else{
            		alert("标题，类型不能为空")
            }
            
    },

//  //上传图片
//  sendFile(file){
//      data = new FormData();  
//      data.append("file", file);   
//      $.ajax({  
//          data: data,  
//          type: "POST",  
//          url: hostip+"/imgupdata",  
//          cache: false,  
//          contentType: false,  
//          processData: false,  
//          success: function(url) {  
//              console.log(url);
//              $('#summernote').summernote('insertImage', url); // url必须是有效的http  
//          },
//          error:function(){
//              alert("图片上传失败...");
//          }  
//      });  
//  }
    }
}
</script>

<style scoped>
.m{ 
    width: 800px; 
    margin :10px 0 0 10%; 
}
button{
    margin: 20px 0 0 0;
}
.typeselect{
	margin: 20px 0 0 10%;
}
</style>
