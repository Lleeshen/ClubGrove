<template>
  <div>
    <b-container fluid="sm">
      <b-row class= "club-page text-center">
        <b-col>
          <h2 v-if="item">{{item[0].name}}</h2>
        </b-col>
      </b-row>
    </b-container>
     <b-container fluid>
      <b-row class= "club-page text-center">
        <b-col v-if="item">
          <h3>Description</h3>
          {{item[0].description}}
        </b-col>
        <b-col cols="5">
          picture here
        </b-col>
        <b-col>
        </b-col>
      </b-row>
    </b-container>
  <b-container>
    
  </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'clubPage',
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
