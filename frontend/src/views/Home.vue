<template>
  <div class="home">
    <HomeDescription/><br>
    <h2>Links to get started</h2>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeDescription from '@/components/HomeDescription.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'home',
  components: {
    HomeDescription,NavBar
  }
}
</script>

<style scoped>

.home a{
  display: inline-block;
  padding: 10px;
  background-color:grey;
}
</style>
