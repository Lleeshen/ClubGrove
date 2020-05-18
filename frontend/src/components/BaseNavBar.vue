<template>
  <div id="nav">
      <b-navbar type ="light">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/club">Club Search</b-nav-item>
          <b-nav-item to="/events">Event Search</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-if=this.loggedIn 
        class="ml-auto">
        <b-nav-item-dropdown text="User" right >
          <b-dropdown-item to="/user" variant="dark">My Page</b-dropdown-item>
          <b-dropdown-item @click=logOut variant="dark"> Log out</b-dropdown-item>
        </b-nav-item-dropdown>
        </b-navbar-nav>
        <b-navbar-nav v-else class="ml-auto">
          <b-nav-item @click="startLogIn"> Sign in </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
      </b-navbar>
      <b-modal v-model="logInModal" hide-footer>
      <b-form action="/club" @submit.prevent="logIn">
        <b-form-group>
          <label for="username">Username:</label>
          <b-form-input v-model="username" id="username" placeholder="example@gmail.com"></b-form-input>
        </b-form-group>
        <b-form-group>
          <label for="password">Password:</label>
          <b-form-input type="password" v-model="password" id="password"></b-form-input>
        </b-form-group>
        <b-button variant="secondary" type="submit">Log In</b-button>
        <br />
        <br />
        <div v-if=failedLogin id="formText"> {{failedLogin}} </div>
      </b-form>
    </b-modal>
    </div>
</template>

<script>
export default {
  name: 'BaseNavBar',
  props: {
    msg: String
  },
  data() {
    return {
      loggedIn: false,
      logInModal: false,
      username: '',
      password: '',
      failedLogin: false,
    }
  },
  mounted() {
    this.$axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        //console.log(response.data);
        if (response.data != '') {
          this.loggedIn = true;
        }
      })
      .catch(error => {console.log(error)});
  },
  methods: {
    startLogIn() {
      this.logInModal = true;
    },
    logIn() {
      this.$axios
        .post('http://localhost:5000/api/login',{
          'username': this.username,
          'password': this.password
        })
        .then(response => {
          //console.log(response.data);
          if(response.data.length != 0) {
            location.reload();
          } else {
            this.failedLogin = "Invalid credentials";
          }
        })
        .catch(error => {console.log(error)});
    },
    logOut() {
      this.$axios
        .get('http://localhost:5000/api/logout')
        .then(response => {
           this.loggedIn = false;
           this.failedLogin = false;
           location.reload();
         })
        .catch(error => {console.log(error)});
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.navbar {
  background-color: #B50043;
}

.navbar-light{
  font-family: Helvetica, Arial, sans-serif;
}
.navbar-light .navbar-nav .nav-item .dropdown-menu{
      color:black!important
}

</style>
