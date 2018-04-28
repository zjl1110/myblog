import Vue from 'vue';
import Vuex from 'vuex';
//vuex数据持久化，防止vuex刷新数据消失问题
import VuexPersistence from 'vuex-persist';

Vue.use(Vuex)

//初始化插件
const vuexLocal = new VuexPersistence({
    storage: window.sessionStorage
});

//初始化
const store = new Vuex.Store({
    state: {
        content:[],
        typelist:[],
        contentlist:[],
        summernotecon:{},
    },
    actions: {
		//actions调用
        setcontencommit:({ commit },datas)=>{
            commit("setcontents",datas)
        },
        settypelistcommit:({ commit },datas)=>{
        		commit("settypelist",datas)
        },
        setsummernotecommit:({ commit },datas)=>{
        		commit("setsummernotecon",datas)
        },
      },
    mutations: {
        //设置数据
        setcontents:(state,datas)=>{
            state.content = datas
        },
        settypelist:(state,datas)=>{
        		state.typelist = datas
        },
        setsummernotecon:(state,datas)=>{
        		state.summernotecon = datas
        },
      },
    getters:{
        //获取数据
        getcontents:state=>{
            return state.content
        },
        gettypelist:state=>{
        		return state.typelist
        },
        getsummernotecon:state=>{
        		return state.summernotecon
        },
    },
    //添加插件
    plugins: [vuexLocal.plugin]
  })
export default store