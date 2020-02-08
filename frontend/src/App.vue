<template>
  <div id="app">
    <div id="title">
      <h1>Club Grove<br>Finding clubs within the area</h1>
    </div>
    <BaseNavBar></BaseNavBar>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
import BaseNavBar from './components/BaseNavBar'
export default {
  components : {BaseNavBar}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px 0px;
}

#nav a {
  font-weight: bold;
  color: #42b983;
}

#nav a.router-link-exact-active {
  color: #2c3e50;
}

#title {
  background-color: antiquewhite;
  color: darkred;
  padding: 10px;
}


</style>
