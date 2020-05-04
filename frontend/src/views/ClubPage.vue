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
          {{item[0].description}}
        </b-col>
        <b-col cols="5">
          <img src="@/assets/noImage.png" style = "max-width: 100%">
        </b-col>
        <b-col>
        <div v-if="isLeader">
          You are the Leader of this group.
        </div>
        <div v-else-if="user">
          You are logged in.
        </div>
        </b-col>
      </b-row>
      <b-row>
    <EventBar v-bind:name="$route.params.name"></EventBar>
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
      user: null
    }
  },
  methods: {
    isloggedin()
    {
      return axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        console.log(response.data);
        this.user = response.data;
      })
      .catch(error => {console.log(error)});
    },
    hasitem()
    {
      if(this.item && this.item.length > 1)
      {
        return true;
      }
      return false;
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
       console.log(response) })
      .catch(error => {console.log(error)})
    axios
      .get(strin3)
      .then(response => {
        if(response.data.length >=1)
        {
          this.isLeader = response.data[0].count; 
          console.log(response.data[0].count);
          self.isloggedin();
        }})
      .catch(error => {console.log(error)})
  }
}

</script>

<style>

</style>
