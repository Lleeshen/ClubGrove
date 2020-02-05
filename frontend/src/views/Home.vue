<template>
  <div class="home">
    <HomeDescription/><br>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeDescription from '@/components/HomeDescription.vue'

export default {
  name: 'home',
  components: {
    HomeDescription
  }
}
</script>

<style scoped>


</style>
