<template>
  <div v-if="isValid">
     <b-container fluid class="ml-1">
     <b-row class= "club-page text-left">
        <b-col>
          <h2>User Page</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left">
        <b-col sm="3">
        <b-row>
        <b-col class = "border">
          <h3>Info</h3>
           Email: {{user2[0]}} <br><br>
           <b-button class = "float-left" size="sm" style="margin-bottom: 5px;" v-b-modal.modal-2>Pending Requests</b-button> <br><br>
           <b-button class = "float-left" size="sm" style="margin-bottom: 5px;" v-b-modal.modal-1>Interested Clubs</b-button>
        </b-col>
        </b-row>
        </b-col>
        <b-col>
        <BasicClubSearch v-bind:user="user2[0]"></BasicClubSearch>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left">
      <b-col>
      </b-col>
      </b-row>
    </b-container>
  <b-container>
  </b-container>
  <b-modal id="modal-2" title="Pending Request" ok-only>
    <p>
        Here are a list of request:
    </p>
    <div v-if= "requests">
      <div v-for="item in requests">
          <b-container fluid>
            <b-row>
              <b-col> {{ item.name }} </b-col>
           </b-row>
          </b-container>
      </div>
    </div>
    <div v-else>
      no
    </div>
    </b-modal>
  <b-modal id="modal-1" title="Interested Clubs" ok-only>
    <p>
        Here what you are intereseted in:
    </p>
    <div v-if= "interested">
      <div v-for="item in interested">
          <b-container fluid>
            <b-row>
              <b-col> {{ item.name }} </b-col>
              <b-col><b-button variant="primary" @click="addRequest(item.name)"> Join? </b-button> </b-col>
           </b-row>
          </b-container>
          </div>
    </div>
    <div v-else>
      no
    </div>
    </b-modal>
  </div>
  <div v-else>
    <p>Please login to see page</p>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import BasicClubSearch from '../components/BasicClubSearch'

export default {
  name: 'User',
  components : {BasicClubSearch},
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
        if(self.user2)
        {
          self.isValid = true;
          //console.log(self.user2[0]);
          self.getRequests(self.user2[0]);
          self.getinterested(self.user2[0]);
        }
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
      //console.log(name);
      return axios
      .get('http://localhost:5000/db/view/requests/'.concat(name).concat('?user=True'))
      .then(response => {
        //console.log(response.data);
        self.requests = response.data;
      })
      .catch(error => {console.log(error)});
    },
    getinterested(name){
      var self = this;
      var a = encodeURIComponent(name);
      //console.log(name);
      return axios
      .get('http://localhost:5000/db/view/interested/'.concat(name))
      .then(response => {
        //console.log(response.data);
        self.interested = response.data;
      })
      .catch(error => {console.log(error)});
    },
    addRequest(clubName)
    {
      console.log(clubName);
      var self = this;
      console.log(this.user2[0]);
      console.log(this.interested);
      this.$axios
        .post('http://localhost:5000/api/toRequest',{'name': clubName, 'email': this.user2[0]})
        .then(response =>{
          //console.log(response.data);
          if(response.data === "success") {
            console.log(self.interested);
            self.interested = self.interested.filter((club) => club.name !== clubName);
          }
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}

</script>

<style>

</style>
