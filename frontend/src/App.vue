<template>
  <div id="app">
    <div id="status">
      <b-button v-if=this.loggedIn square variant="info" @click=logOut> Log out </b-button>
      <b-button v-else square variant="info" @click="startLogIn"> Sign in </b-button>
    </div>
    <b-modal v-model="logInModal">
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
    <div id="title">
      <h1>Club Grove<br>Finding clubs within the area</h1>
    </div>
    <BaseNavBar></BaseNavBar>
    <router-view/>
  </div>
</template>

<script>
import BaseNavBar from './components/BaseNavBar'
export default {
  components : {BaseNavBar},
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
        console.log(response.data);
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
          console.log(response.data);
          if(response.data.length != 0) {
            this.logInModal = false;
            this.loggedIn = true;
            this.failedLogin = false;
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
         })
        .catch(error => {console.log(error)});
    }
  }
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

#status {
  font-size: 24px;
  float: right;
  margin-top: 30px;
  margin-right: 70px;
}

#formText {
  font-size: 16px !important;
}

</style>
