<template>
    <div class="content pure-u-1 pure-u-md-3-4">
        <div>
            <div class="posts">
                <h1 class="content-subhead">文章</h1>

                <section class="post" v-for="cdata in datas" >
                    <div>
                    <header class="post-header">
                       <h2 class="post-title" >{{ cdata.title}}</h2>
						<button @click="remove(cdata.id)">删除</button>
						<button @click="setcontent(cdata)">编辑</button>
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
            
            <!-- 底部-->
            <h1 class="content-subhead"></h1>
            <!-- 分页 通过:total="total"形式向子组件的props中传参-->
            <footer_list :total="total" :current-page='current' :display='display' @pagechange="pagechange"></footer_list>
        </div>
    </div>
</div>
</template>

<script>
import footer_list from "../home/footerlist.vue";
import { removecon,hostip } from '../../assets/js/setajax.js';
import { getCookie } from '../../assets/js/cookietools.js'

export default {
    components: {
      'footer_list': footer_list,
   
    },
    data(){
        return {
                total: 0,     // 记录总条数
                display: 5,   // 每页显示条数
                current: 1,   // 当前的页数
                contenttype:"all",
                datas:[],
                paramsdata:{}
        }
    },
    mounted(){
        this.pagechange()
    },
    methods: {
    	//pure响应式js特效
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
                console.log(this.total);
            }).catch((error)=> {
            　　alert(error);
            });
     },
//   showmenu(data){
//       this.contenttype=data;
//       this.pagechange(this.current);
//   },
     //修改
     setcontent(data){
     	console.log(data.id)
         this.$store.dispatch('setsummernotecommit',data);
         this.$router.push("/adminhome/home");
     },
     //删除
     remove(id){
     	var qs = require('qs');
        var pdatas = qs.stringify({
            'username': getCookie("username"),
            "token":getCookie("token"),
            "conid":id,
        });
     	removecon(pdatas);
     	this.pagechange(this.current);
     }
   }
}
</script>

<style scoped>
@import "../../assets/css/blog.css";
/*隐藏多余内容*/
.post-description p{
display: block;
    /*width: 70%;*/
    height: 109.2px;
    overflow: hidden;
    text-overflow: ellipsis;
}
a:hover{
    text-decoration:none;
}
.content{
	margin: 0 0 0 10%;
	/*padding: 2em 3em 0 8em;*/
}

</style>