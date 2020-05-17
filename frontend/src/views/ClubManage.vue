<template>
  <div v-if="loggedInAsLeader">
    <b-container fluid>
      <h3> Club  {{ name }} </h3>
      <b-table bordered hover :items='events' :fields='fields'></b-table>
    </b-container>
  </div>
  <div v-else>
    <h3> You do not have permission to access this page. </h3>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'ClubManageEvent',
  data() {
    return {
      loggedInAsLeader: false,
      userName: "",
      events: null,
      fields: [
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
    }
  },
  mounted() {
    this.$axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        console.log(response.data);
        if(response.data != "") {
          this.userName = response.data[0];
          let url = 'http://localhost:5000/api/loginLeader?name=' + this.userName + '&clubName=' + this.name;
          this.$axios
            .get(url)
            .then(response => {
              console.log(response.data);
              if(response.data.length == 1) {
                this.loggedInAsLeader = true;
                this.$axios
                  .post('http://localhost:5000/api/getEvents',{'nm': this.name})
                  .then(response => {
                    this.events = response.data;
                    console.log(this.events);
                  })
                  .catch(error => {console.log(error)})
              }
            })
            .catch(error => {console.log(error)})
        }
      })
      .catch(error => {console.log(error)});
  },
  props: ['name']
}

</script>

<style scoped>

</style>
