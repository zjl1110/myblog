import axios from 'axios'
import store from'../../store'
import router from '../../router'
import $ from 'jquery';

//因为异步不能返回值所以这里用了jquery的ajax同步，不然menu上第一次不会显示
function getmenulist(){
	let data = "";
	$.ajax({    
            type: "GET",  
            url: hostip+"/getmenulist", 
            dataType:"json",  
            cache:false, 
       		async:false,
            success: function(datas) { 
            	console.log("123456"+datas.typedatas);
            		store.dispatch('settypelistcommit',datas.typedatas);
                data =  datas.typedatas
            },
            error:function(){
                alert("图片上传失败...");
            }  
        }); 
        return data
}

//这里是异步获取menu
function getmenulise(){
	axios.get(hostip+"/getmenulist").then((response) =>{
	    console.log("cccc111"+response.data.typedatas);
	    store.dispatch('settypelistcommit',response.data.typedatas);
	}).catch((error)=> {
	　　alert(error);
	});
};

function getcontentlist(paramsdata){
	axios.get(hostip+"/getcontentlist",{
       params:paramsdata
   }).then((response) =>{
       return response.data.datas;
    }).catch((error)=> {
       alert(error);
    });
};

function setsummernotecon(paramsdata){
	var datad;
	axios.post(hostip+"/editcontent",paramsdata
).then((response) =>{
	datad = response.data.login;
	console.log("xxxx"+datad)
	if(datad && datad!="0"){
		router.push("/adminhome/conlist")
		store.dispatch('setsummernotecommit',{});
	}else{
		router.push("/admin")
	}
    }).catch((error)=> {
       alert(error);
    });
    console.log(datad);
    return datad;
};

function removecon(paramsdata){
	var datad;
	axios.post(hostip+"/delcontent",paramsdata
).then((response) =>{
	datad = response.data.login;
	if(datad && datad!="0"){
		alert("删除成功");
		router.push("/adminhome/conlist")
		store.dispatch('setsummernotecommit',{});
	}else{
		router.push("/admin")
	}
    }).catch((error)=> {
       alert(error);
    });
}

//上线改成服务器ip
const hostip ="http://127.0.0.1:5000";

export{
	getmenulist,
	hostip,
	getmenulise,
	getcontentlist,
	setsummernotecon,
	getintroduction,
	removecon,
};



