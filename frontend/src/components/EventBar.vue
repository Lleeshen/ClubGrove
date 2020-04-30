<template>
<b-container fluid style="border: .5px solid grey; margin: 10px" >
    <b-row class = "row align-items-center" style="background: lightblue">
      <b-col>
        <h3> {{ name }} Events </h3>
      </b-col>
      <b-col cols="9">
        <b-card-group v-if="fields" style="margin: 10px">
      <div v-for="item in items" :key="item.name">
        <Baseholder 
            v-bind:items="item" 
            isEvent="true">
        </Baseholder>
      </div>
      </b-card-group>
        <!---
        <b-table bordered hover :items='items' :fields='fields'></b-table>
        --->
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src
import Baseholder from '../components/Baseholder'
export default {
  name: 'EventBar',
  components: {Baseholder},
  data() {
    return {
      validClub: false,
      fields: [
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      items: null,
      clubName: this.name
    }
  },
  mounted() {
    if(this.clubName)
    {
        this.$axios
        .post('http://localhost:5000/api/getEvents',{'nm': this.clubName})
        .then(response => {this.items = response.data;
        console.log(response.data) })
        .catch(error => {console.log(error)})
    }
  },
  props: ['name']
}

</script>

<style scoped>

</style>