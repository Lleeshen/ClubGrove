<template>
  <div v-if= "item">
    <b-container fluid>
      <b-row class= "club-page text-left">
        <b-col>
          <h2>{{item[0].name}}</h2>
        </b-col>
      </b-row>
      <b-row class= "club-page text-left" style= "height: 100px;">
        <b-col>
          <h3 >Description</h3>
          {{item[0].description}}
        </b-col>
        <b-col class = "text-center float-center">
          picture here
        </b-col>
      </b-row>
      <b-row>
          <b-col>
              <b-button class = "float-left" size="sm" style="margin-bottom: 5px;" v-b-modal.modal-1>Accept Requests</b-button>
          </b-col>
          <b-col cols="5">
        </b-col>
        <b-col>
        </b-col>
      </b-row>
    </b-container>
    <b-modal id="modal-1" title="Request List">
    <p>
        Here are a list of request:
    </p>
    <div v-if= "1==1">
    
    </div>
    <div v-else>

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
      item: null

    }
  },
  mounted() {
    var a = this.$route.params.name;
    var strin2 = 'http://localhost:5000/db/view/club/'.concat(a);
    console.log(strin2);
    axios
      .get(strin2)
      .then(response => {this.item = response.data;
       console.log(response) })
      .catch(error => {console.log(error)});
      
  }
}

</script>

<style>

</style>