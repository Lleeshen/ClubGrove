<template>
  <div v-if="loggedInAsLeader">
    <b-container fluid>
      <h3> Club  {{ name }} </h3>
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
      loggedInAsLeader: true,
      userName: false,
    }
  },
  mounted() {
    this.$axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        //console.log(response.data);
        if(response.data != "") {
          this.userName = response.data[0];
        }
      })
      .catch(error => {console.log(error)});
    console.log(this.userName)
    // this.$axios
    //   .get('http://localhost:5000/db/view/club')
    //   .then(response => {
    //     console.log(response.data);
    //     if(this.loggedInAsAdmin) {
    //       if(typeof response.data !== "string"){
    //         this.items = response.data;
    //       }
    //     }
    //   })
    //   .catch(error => {console.log(error)});
  },
  methods: {
    setUpClub() {
      this.clubModal = true;
    }
  },
  props: ['name']
}

</script>

<style scoped>

</style>
