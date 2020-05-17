<template>
  <div v-if= "item">
    <b-container fluid>
      <b-row class= "club-page text-left">
        <b-col>
          <h2>{{item[0].name}}</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left">
        <b-col>
          <h3 >Description</h3>
          {{item[0].description}}
          <br><br>
          <b-row>
          <b-col class="club-page text-left">
          <h3>Requests</h3>
              <b-button class = "float-left" size="sm" style="margin-bottom: 5px;" v-b-modal.modal-1>Accept Requests</b-button>
          </b-col>
          </b-row>
        </b-col>
        <b-col class = "text-center float-center">
          <img src="@/assets/noImage.png" style = "max-width: 100%">
        </b-col>
      </b-row>
    </b-container>
    <b-modal id="modal-1" title="Request List">
    <p>
        Here are a list of request:
    </p>
    <div v-if= "item2">
    <b-list-group>
      <b-list-group-item>
       <b-row>
         <b-col> Email </b-col>
         <b-col> Accept </b-col>
         <b-col> Decline </b-col>
        </b-row>
      </b-list-group-item>
      <div v-for="item in item2">
        <b-list-group-item  key=item.name>
          <b-row>
            <b-col> {{ item.email }} </b-col>
            <b-col> <b-button @click="acceptRequest(item.email, item.name)">Accept Request </b-button> </b-col>
            <b-col> <b-button @click="declineRequest(item.email, item.name)">Decline Request </b-button> </b-col>
         </b-row>
        </b-list-group-item>
      </div>
    </b-list-group>
    </div>
    <div v-else>
      no
    </div>
    </b-modal>
  <b-container>
    
  </b-container>
  </div>
  <div v-else>
   Nothing is here.
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'clubPageManage',
  data() {
    return {
      //Replace this with actual club results
      item: null,
      item2: null

    }
  },
  mounted() {
    var a = this.$route.params.name;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a);
    var strin3 = 'http://localhost:5000/db/view/requests/'.concat(a);
    console.log(strin2);
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
       console.log(response) })
      .catch(error => {console.log(error)});
    axios
      .get(strin3)
      .then(response => {this.item2 = response.data;
       console.log(response) })
      .catch(error => {console.log(error)});
      
  },
  methods: {
    acceptRequest(email,name) {
      this.$axios
        .post('http://localhost:5000/api/acceptClubRequest',{
          'name': name,
          'email':email})
        .then(response =>{
          //console.log(response.data);
          if(response.data === "success") {
            this.item2 = this.item2.filter((student) => student.email !== email);
          }
        })
        .catch(error => {
          console.log(error);
        })
    },
    declineRequest(email, name){
      this.$axios
        .post('http://localhost:5000/api/declineClubRequest',{
          'name': name,
          'email':email})
        .then(response =>{
          //console.log(response.data);
          if(response.data === "success") {
            this.item2 = this.item2.filter((student) => student.email !== email);
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