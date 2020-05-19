<template>
  <div id="app">
    <div id="title">
      <h1>Club Grove<br>Finding clubs within SCU</h1>
    </div>
    <BaseNavBar></BaseNavBar>
    <router-view/>
  </div>
</template>

<script>
import BaseNavBar from './components/BaseNavBar'
export default {
  components : {BaseNavBar}
}
</script>

<style>
#app {
  font-family: Garamond, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin: 0px 0px;
  font-size: 18px !important;
}

#nav a {
  font-weight: bold;
  color: #E0E0E0;
}

#nav a:hover {
  color: #FBFBFB;
}

#nav a.router-link-exact-active {
  //color: #2c3e50;
  color: #FFFFFF;
}

#title {
  background-color: antiquewhite;
  color: darkred;
  padding: 10px;
}

#status {
  font-size: 24px;
  float: right;
  margin-top: 30px;
  margin-right: 70px;
}

#formText {
  font-size: 16px !important;
}

h1, h2, h3 {
  color: darkred;
}

.loginM{
  font-family: Helvetica, Arial, sans-serif;
}

.description {
  display: inline-block;
  margin: 10px 0px 0px 0px;
  padding: 10px;
}

 .decription-content {
  background-color: #CECECE;
  padding: 10px;
  text-align: left;
  color: black;
  border: solid 1px;
}

.description-content {
  background-color: #CECECE;
  padding: 10px;
  text-align: left;
  color: black;
  border: solid 1px;
}
</style>
