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

.description-content {
  background-color: #CECECE;
  padding: 10px;
  text-align: left;
  color: black;
  border: solid 1px;
}

.btn-custom {
  background-color: #B50043 !important;
  color: #F3F3F3 !important;
}

.btn-custom:hover{
  background-color: #D51154 !important;
  color: #FBFBFB !important;
}

.btn-customBlack {
  background-color: #111111 !important;
  color: #F3F3F3 !important;
}

.btn-customBlack:hover{
  background-color: #888888 !important;
  color: #FBFBFB !important;
}

.btn-customBlack:disabled {
  background-color: #AAAAAA !important;
  color: #F3F3F3 !important;
  pointer-events: none;
}

.pagination > li > a
{
  background-color: white;
  color: #000000;
}
.pagination > li > a:hover,
.pagination > li > a:active
{
  color: #000000 !important;
}

.pagination > .active > a
{
  background-color: #777777 !important;
  color: #F3F3F3 !important;
}
</style>
