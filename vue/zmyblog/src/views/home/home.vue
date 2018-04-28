<template>
  <div id="home">
    <div id="layout" class="pure-g">
      <Introduction></Introduction>
      <Contentlist></Contentlist>
    </div>
  </div>
</template>

<script>
import Meun from "./tuckedmenuvertilcal.vue"
import Introduction from "./introduction.vue"
import Contentlist from "./contentlist.vue"

export default {
  components:{
    Introduction,
    Contentlist,
  }
}
</script>

<style>
</style>
