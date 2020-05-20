<template>
  <div v-if="hasitem()">
    <b-container fluid >
      <b-row class= "club-page text-center">
        <b-col>
          <h2 v-if="hasitem()">{{item[0].name}}</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-center">
        <b-col v-if="hasitem()">
          <h3>Description</h3>
          <div class ="text-left">
          {{item[0].description}}
          </div>
        </b-col>
        <b-col cols="5">
          <img :src="image()" style = "max-width: 100%">
        </b-col>
        <b-col>
        <div v-if="isLeader">
        <h3>Leadership Responsibilities</h3>
        <b-button 
        variant="custom"
        :to="link"
        >Manage Club</b-button>
        <br /> <br />
        <b-button variant="custom" 
        :to="link2"
        >Manage Club Events</b-button>
        </div>
        <div v-else-if="user">
        <h3>Join Options</h3>
        <b-button 
          variant="customBlack"
          :disabled="isMember" 
          v-on:click="generateJoinRequest()"
          style="margin-right: 5px;">Join Club </b-button>
        <b-button 
          variant="customBlack"
          :disabled="isMemberOrInterested()" 
          v-on:click="generateRequestForInterested()"
          >Follow Club</b-button><br>
        </div>
        </b-col>
      </b-row>
      <b-row>
    <EventBar v-bind:name="$route.params.name"></EventBar>
      </b-row>
      <b-row v-if="item[0].website">
      <b-col>
        <h3>Other Websites</h3>
        <a :href="'//' +item[0].website">{{item[0].website}}</a>
        <br><br>
      </b-col>
      </b-row>
    </b-container>
  <b-container>
  </b-container>
  </div>
  <div v-else>
    This page does not exist.
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import EventBar from '../components/EventBar'

export default {
  name: 'clubPage',
  components: {EventBar},
  data() {
    return {
      //Replace this with actual club results
      item: null,

      isLeader: null,
      user: null,
      isInterested: false,
      isMember: false
    }
  },
  methods: {
    isloggedin()
    {
      var self = this;
      return axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        console.log(response.data[0]);
        this.user = response.data;
        self.isPartOfClub();
      })
      .catch(error => {console.log(error)});
    },
    isPartOfClub(){
      var self = this;
      if(self.user && self.item[0])
      {
        var b = encodeURIComponent(this.item[0].name);
        return axios
          .get('http://localhost:5000/api/isMemberOrRequested/'.concat(this.item[0].name))
          .then(response => {
          console.log(response.data);
          {
              self.isMember = response.data.member;
              self.isInterested= response.data.interested
          }
        })
      .catch(error => {console.log("error")});
      }
    },
    hasitem()
    {
      if(this.item && this.item.length >= 1)
      {
        return true;
      }
      return false;
    },
    isMemberOrInterested()
    {
        if(this.isMember || this.isInterested)
        {
          return true;
        }
        return false;
    },
    generateRequestForInterested()
    {
      var self = this;
      if(this.hasitem() && this.item[0].name)
      {
        this.$axios
          .post('http://localhost:5000/api/interested',{'name': this.item[0].name,
          'email': this.user[0]})
          .then(response => {
          console.log(response.data);
          self.isInterested = true;
          })
          .catch(error => {console.log(error)})
      }
    },
    generateJoinRequest()
    {
      if(this.hasitem() && this.item[0].name)
      {
        if(this.isInterested)
        {
          this.$axios
            .post('http://localhost:5000/api/toRequest',{'name': this.item[0].name, 'email': this.user[0]})
          .then(response =>{
          //console.log(response.data)
          this.isMember = true;
        })
        .catch(error => {
          console.log(error);
        })
        }
        else
        {
          this.$axios
          .post('http://localhost:5000/api/generateClubRequest',{'name': this.item[0].name,
          'email': this.user[0]})
          .then(response => {//this.items = response.data;
          console.log(response.data);
          this.isMember = true;
          self.isInterested = true;
          })
          .catch(error => {console.log(error)})
        }
      }
    },
    greet()
    {
      alert("a");
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
  },
  mounted() {
    var a = this.$route.params.name;
    var self = this;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a)
    var strin3 = 'http://localhost:5000/api/getLeader?name='.concat(a)
    console.log(strin2)
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
       console.log(response);
       self.isloggedin(); })
      .catch(error => {console.log(error)})
    axios
      .get(strin3)
      .then(response => {
        if(response.data.length >=1)
        {
          this.isLeader = response.data[0].count;
          console.log(response.data[0].count);
        }})
      .catch(error => {console.log(error)})
  },
  computed:
  {
      link: function()
      {
        if(this.item){
          return encodeURI(this.item[0].name) + "/manage";
        }
        return "#";
      },
      link2: function()
      {
        if(this.item){
          return encodeURI(this.item[0].name) + "/events/manage";
        }
        return "#";
      }
  }
}

</script>

<style>

</style>
