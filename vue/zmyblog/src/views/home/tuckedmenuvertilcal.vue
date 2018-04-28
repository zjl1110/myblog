<template>
    <div class="custom-wrapper pure-g" id="menu">
        <div class="pure-u-1 pure-u-md-1-3">
            <div class="pure-menu">
                <a href="/" class="pure-menu-heading custom-brand">博客</a>
                <a href="#" class="custom-toggle" id="toggle"><s class="bar"></s><s class="bar"></s></a>
            </div>
        </div>
        <div class="pure-u-1 pure-u-md-1-3">
            <div class="pure-menu pure-menu-horizontal custom-can-transform">
                <ul class="pure-menu-list" >
                    <li class="pure-menu-item" v-for="typedata in typedatas">
                        <a @click="gettype(typedata.type)" class="pure-menu-link">{{typedata.type}}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import {getmenulise,getmenulist} from '../../assets/js/setajax.js'
export default {
    //要向父组件传递的值
    props:["contenttype"],
    data(){
        return{
            typedatas:this.$store.getters.gettypelist,
        }
    },
    mounted() {
    		this.settypes();
        this.changeIcon(window,window.document);
    },
    methods:{
    	//pure响应样式的js效果代码
        changeIcon (window, document) {
            var menu = document.getElementById('menu'),
                WINDOW_CHANGE_EVENT = ('onorientationchange' in window) ? 'orientationchange':'resize';

            function toggleHorizontal() {
                [].forEach.call(
                    document.getElementById('menu').querySelectorAll('.custom-can-transform'),
                    function(el){
                        el.classList.toggle('pure-menu-horizontal');
                    }
                );
            };

            function toggleMenu() {
                // set timeout so that the panel has a chance to roll up
                // before the menu switches states
                if (menu.classList.contains('open')) {
                    setTimeout(toggleHorizontal, 500);
                }
                else {
                    toggleHorizontal();
                }
                menu.classList.toggle('open');
                document.getElementById('toggle').classList.toggle('x');
            };

            function closeMenu() {
                if (menu.classList.contains('open')) {
                    toggleMenu();
                }
            }
            document.getElementById('toggle').addEventListener('click', function (e) {
                toggleMenu();
                e.preventDefault();
            });
            window.addEventListener(WINDOW_CHANGE_EVENT, closeMenu);
            },
//      getmenulise:function(){
//          this.axios.get("http://127.0.0.1:5000/getmenulist").then((response) =>{
//              console.log(response.data);
//              this.typedatas = response.data.typedatas;
//          }).catch((error)=> {
//          　　alert(error);
//          });
//      },
        //向父组件传值的触发
        gettype(contenttype){
            this.$emit("contenttype",contenttype);
        },
        //menu类型获取
        settypes(){
        		this.typedatas = getmenulist();
        }
        
    }
}
</script>


<style scoped>
/*顶部导航*/
.custom-wrapper {
    background-color: rgb(136, 181, 192);
    margin-bottom: 1em;
    -webkit-font-smoothing: antialiased;
    height: 2.1em;
    overflow: hidden;
    -webkit-transition: height 0.5s;
    -moz-transition: height 0.5s;
    -ms-transition: height 0.5s;
    transition: height 0.5s;
    z-index: 99999;
    position: fixed;
    width: 100%;
}

.custom-wrapper.open {
    height: 19em;
}

.custom-menu-3 {
    text-align: right;
}

.custom-toggle {
    width: 34px;
    height: 34px;
    position: absolute;
    top: 0;
    right: 0;
    display: none;
}

.custom-toggle .bar {
    background-color: #777;
    display: block;
    width: 20px;
    height: 2px;
    border-radius: 100px;
    position: absolute;
    top: 18px;
    right: 7px;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    -ms-transition: all 0.5s;
    transition: all 0.5s;
}

.custom-toggle .bar:first-child {
    -webkit-transform: translateY(-6px);
    -moz-transform: translateY(-6px);
    -ms-transform: translateY(-6px);
    transform: translateY(-6px);
}

.custom-toggle.x .bar {
    -webkit-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
}

.custom-toggle.x .bar:first-child {
    -webkit-transform: rotate(-45deg);
    -moz-transform: rotate(-45deg);
    -ms-transform: rotate(-45deg);
    transform: rotate(-45deg);
}

@media (max-width: 47.999em) {

    .custom-menu-3 {
        text-align: left;
    }

    .custom-toggle {
        display: block;
    }

}
.pure-menu-list{
    text-align:left;
}
a:hover{
    text-decoration:none;
}

</style>
