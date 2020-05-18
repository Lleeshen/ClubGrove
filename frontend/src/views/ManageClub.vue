<template>
  <div v-if= "isleader">
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
          <img v-bind:src="image()" 
          style = "max-width: 100%">
          <div v-if="noImg">
            Club does not have a picture
          </div>
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
   You don't have access to this Page
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
      item2: null,
      isleader: false,
      noImg: false
      //imgLoc: require("@/assets/club/Chinese Student Association.png")

    }
  },
  mounted() {
    var self = this;
    var a = this.$route.params.name;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a);
    var strin3 = 'http://localhost:5000/db/view/requests/'.concat(a);
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
         self.checkLeader();})
      .catch(error => {console.log(error)});
    axios
      .get(strin3)
      .then(response => {this.item2 = response.data;
       })
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
    },
    checkLeader()
    {
      if(this.item && this.item[0])
      {
      var self = this;
      var c = 'http://localhost:5000/api/getLeader?name='.concat(this.item[0].name);
        this.$axios
        .get(c)
        .then(response =>{
          //console.log(response.data);
          if(response.data && response.data[0].count >= 1) {
            self.isleader = true;
          }
        })
        .catch(error => {
          console.log(error);
        })
      }
    },
    image()
    {
      var self = this;
      try{
        return require("@/assets/club/"+this.item[0].name+ ".png");
      }
      catch(err)
      {
        self.noImg = true;
        console.log("Club does not have a picture");
      }
      return require("@/assets/noImage.png")
    }
  }

}

</script>

<style>

</style>