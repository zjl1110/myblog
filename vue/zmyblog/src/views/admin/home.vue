<template>
<div>
   <summernote></summernote>
</div>
</template>

<script>
import summernote from './summernote.vue';

export default {
	data(){
		return{
		}
	},
    components:{
        summernote,
    },    
}
</script>

<style scoped>
.note-popover{
	position:inherit;
	display: none;
	z-index: -999;
}
.popover{
	position:inherit;
	display: none;
	z-index: -999;
}
</style>
