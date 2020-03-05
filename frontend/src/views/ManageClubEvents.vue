<template>
  <div v-if='loggedInAsClubLeader'>
    <b-container fluid class="mainPage">
      <b-row>
        <b-col>
          <h3> Club  {{ name }} </h3>
        </b-col>
        <b-col cols="9">
          <b-table bordered hover :items='items' :fields='fields'></b-table>
        </b-col>
      </b-row>
    </b-container>
  </div>
  <div v-else>
    <h3> You do not have permission to access this page. </h3>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'clubEvent',
  data() {
    return {
      loggedInAsClubLeader: false,
      validClub: false,
      fields: [
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      items: null
    }
  },
  mounted() {
    this.$axios
      .post('http://localhost:5000/api/getEvents',{'nm': this.name})
      .then(response => {this.items = response.data;
       console.log(response.data) })
      .catch(error => {console.log(error)})
  },
  props: ['name']
}

</script>

<style scoped>
.mainPage {
  margin-top: 20px;
}
</style>
