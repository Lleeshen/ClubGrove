<template>
  <div>
    <b-container fluid>
      <b-row class= "club-page text-center">
        <b-col>
          <h2 v-if="item">{{item[0].name}}</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-center">
        <b-col v-if="item">
          <h3>Description</h3>
          {{item[0].description}}
        </b-col>
        <b-col cols="5">
          <img src="@/assets/noImage.png" style = "max-width: 100%">
        </b-col>
        <b-col>
        </b-col>
      </b-row>
      <b-row>
    <EventBar v-bind:name="$route.params.name"></EventBar>
      </b-row>
    </b-container>
  <b-container>
  </b-container>
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
      item: null

    }
  },
  mounted() {
    var a = this.$route.params.name;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a)
    console.log(strin2)
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
       console.log(response) })
      .catch(error => {console.log(error)})
  }
}

</script>

<style>

</style>
