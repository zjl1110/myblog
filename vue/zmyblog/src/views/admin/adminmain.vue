<template>
	<div id="admin">
		<Menu></Menu>
		<router-view/>
	</div>
</template>

<script>
import Menu from './homemenu.vue'


export default {
    components:{
        Menu
    }
}
</script>

<style>
</style>