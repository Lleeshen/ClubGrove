<template>
  <div v-if="isValid">
    <b-container fluid="sm">
      <b-row class= "club-page text-left">
        <b-col>
          <h2>User Page</h2>
        </b-col>
      </b-row>
    </b-container>
     <b-container fluid>
      <b-row class= "club-page text-center">
        <b-col>
          Here is your information<br>
           Name: {{user[0].name}}
        </b-col>
        <b-col>
        </b-col>
      </b-row>
    </b-container>
  <b-container>
  </b-container>
  </div>
  <div v-else>
    <p>Please login to see page</p>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'User',
  data() {
    return {
      //Replace this with actual club results
      item: null,
      user: null,
      user2: null,
      isValid: false

    }
  },
  mounted() {
    this.loginStatus();
  },
  methods:{
    loginStatus (){
      var self = this;
      axios.all([this.getLogin(),this.getInfo()])
      .then(function (first,second){
        console.log(self.user[0].email);
        console.log(self.user2[0]);
        self.isValid = true;
        if(self.user[0].email == self.user2[0])
        {
          self.isValid = true;
        }
      })
    },
    getLogin() {
      var a = this.$route.params.name;
      var strin2 = 'http://localhost:5000/api/getUserInfo?name='.concat(a)
      console.log(strin2)
      return axios
        .get(strin2)
        .then(response => {
        this.user = response.data;
        //console.log(this.user);
        //console.log(response) 
        })
        .catch(error => {console.log(error)});
    },
    getInfo(){
      return axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        //console.log(response.data);
        this.user2 = response.data;
      })
      .catch(error => {console.log(error)});
    }
  }
}

</script>

<style>

</style>
