<template>
<div>
	<!--分类menu-->
 <meun :contenttype="contenttype" @contenttype="showmenu"></meun>
    <div class="content pure-u-1 pure-u-md-3-4">
        <div>
            <div class="posts">
                <h1 class="content-subhead">最新发布</h1>

                <section class="post" v-for="cdata in datas" >
                    <div @click="setcontent(cdata)">
                    <header class="post-header">
                        <!-- <img width="48" height="48" alt="Eric" class="post-avatar" src="img/common/ericf-avatar.png"> -->

                        <h2 class="post-title">{{ cdata.title}}</h2>

                        <p class="post-meta">
                            By <a class="post-author" href="#">{{cdata.author}}</a> under <a class="post-category post-category-js" href="#">{{ cdata.type }}</a>
                        </p>
                    </header>

                    <div class="post-description">
                    <!-- v-html 显示富文本内容 -->
                        <p v-html="cdata.content">
                        </p>
                    </div>
                    </div>
                </section>
            </div>
            
            <div v-show="show_data">
	            <!-- 底部-->
	            <h1 class="content-subhead"></h1>
	            <!-- 分页 通过:total="total"形式向子组件的props中传参-->
	            <footer_list :total="total" :current-page='current' :display='display' @pagechange="pagechange"></footer_list>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { hostip } from '../../assets/js/setajax.js';
import footer_list from "./footerlist.vue";
import Meun from "./tuckedmenuvertilcal.vue";

export default {
    components: {
      'footer_list': footer_list,
      "meun":Meun
    },
    data(){
        return {
        			show_data:true,
                total: 0,     // 记录总条数
                display: 5,   // 每页显示条数
                current: 1,   // 当前的页数
                contenttype:"all",//类型
                datas:[],
                paramsdata:{}
        }
    },
    mounted(){
        this.pagechange()
    },
    methods: {
    	//分页组件加获取文章内容
     pagechange:function(currentPage){
       console.log("ccc:"+currentPage);
       if(currentPage){
           currentPage = currentPage;
       }else{
           currentPage = 1;
       }
       this.paramsdata={
           "display":this.display,
           "current":currentPage,
           "contenttype":this.contenttype
       }
       // ajax请求, 向后台发送 currentPage, 来获取对应的数据
       this.axios.get(hostip+"/getcontentlist",{
           params:this.paramsdata
           }).then((response) =>{
                // console.log(response.data);
                this.datas = response.data.datas;
                this.total = parseInt(response.data.total);
                this.current = currentPage;
                this.display = parseInt(response.data.display);
                console.log(this.datas.length+"nnnnnn");
                if(!this.datas.length){
                		alert("此类型没有文章");
                		this.show_data = false;
                }
            }).catch((error)=> {
            　　alert(error);
            });
     },
     //获取子组件值
     showmenu(data){
         this.contenttype=data;
         this.pagechange(this.current);
     },
     //将文章内容存入vuex，内容页直接vuex获取内容
     setcontent(data){
         this.$store.dispatch('setcontencommit',data);
         this.$router.push("/content");
     }
   }
}
</script>

<style scoped>
@import "../../assets/css/blog.css";
.post-title{
	width: 80%;
}
/*隐藏多余内容*/
.post-description p{
display: block;
    width: 80%;
    height: 109.2px;
    overflow: hidden;
    text-overflow: ellipsis;
}
a:hover{
    text-decoration:none;
}
.content{
    padding: 2em 3em 0 8em;
    /*margin:0 0 0 5%;*/
}
</style>


