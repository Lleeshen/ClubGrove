<template>
  <div id="app">
    <div id="title">
      <h1>Club Grove<br>Finding clubs within the area</h1>
    </div>
    <div id="nav">
      <b-navbar type ="light">
      <b-navbar-brand class="navbar-brand">Club Grove</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
      </b-navbar>
      
    </div>
    <router-view/>
  </div>
</template>

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

.navbar {
  background-color: aliceblue;
}

</style>
