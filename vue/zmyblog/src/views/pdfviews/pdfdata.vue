<template>
  <iframe :src="srcz" />
</template>

<script>
export default {
    data(){
        return{
            srcz:""
        }
    },
    mounted(){
        this.getpdf()
    },
    methods:{
      getpdf:function(){
            this.axios.get("http://127.0.0.1:5000/jlpdf",).then((response) =>{
                console.log(response.data);
                this.srcz = response.data.pdfdata;
            }).catch((error)=> {
            　　alert(error);
            });
        }
  }
}
</script>
<style scoped>
    iframe{
        height: 1000px;
        width: 100%;
    }
</style>

