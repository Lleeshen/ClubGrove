<template>
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
</template>

<script>
export default {
  name: 'BaseNavBar',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.navbar {
  background-color: aliceblue;
}

</style>
