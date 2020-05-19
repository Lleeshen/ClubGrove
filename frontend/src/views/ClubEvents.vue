<template>
  <b-container fluid class="mainPage">
    <b-row>
      <b-col>
        <h3> Club  {{ name }}  Events</h3>
        <b-table bordered hover 
          :items='items' 
          :fields='fields'
          :per-page="perPage"
          :current-page="currentPage"
          id="event-table"></b-table>
        <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="event-table"
        ></b-pagination>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'clubEvent',
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
      perPage: 8,
      currentPage: 1,
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
