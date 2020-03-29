<template>
  <div v-if="isValid">
     <b-container fluid>
     <b-row class= "club-page text-left">
        <b-col>
          <h2>User Page</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left">
        <b-col>
          <h3>Info</h3>
           Email: {{user2[0]}}
        </b-col>
        <b-col>
          <h3>Pending requests</h3>
          <div v-for="item in requests">
          <b-container fluid>
            <b-row>
              <b-col> {{ item.name }} </b-col>
           </b-row>
          </b-container>
          </div>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left">
      <b-col>
      </b-col>
      <b-col>
        <h3>Interested</h3>
          <div v-for="item in requests">
          <b-container fluid>
            <b-row>
              <b-col> {{ item.name }} </b-col>
              <b-col><b-button variant="primary" @click="addRequest(item.name)"> Join? </b-button> </b-col>
           </b-row>
          </b-container>
          </div>
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
      isValid: false,
      requests: null,
      interested: null

    }
  },
  mounted() {
    this.loginStatus();
  },
  methods:{
    loginStatus (){
      var self = this;
      axios.all([this.getInfo()])
      .then(function (first){
        console.log(self.user2[0]);
        self.isValid = true;
        self.getRequests(self.user2[0]);
        self.getinterested(self.user2[0]);
      })
    },
    getInfo(){
      return axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        //console.log(response.data);
        this.user2 = response.data;
      })
      .catch(error => {console.log(error)});
    },
    getRequests(name){
      var self = this;
      var a = encodeURIComponent(name);
      console.log(name);
      return axios
      .get('http://localhost:5000/db/view/requests/'.concat(name).concat('?user=True'))
      .then(response => {
        console.log(response.data);
        self.requests = response.data;
      })
      .catch(error => {console.log(error)});
    },
    getinterested(name){
      var self = this;
      var a = encodeURIComponent(name);
      console.log(name);
      return axios
      .get('http://localhost:5000/db/view/interested/'.concat(name))
      .then(response => {
        console.log(response.data);
        self.requests = response.data;
      })
      .catch(error => {console.log(error)});
    },
    addRequest(name)
    {
        console.log(name)
    }
  }
}

</script>

<style>

</style>
