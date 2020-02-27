<template>
  <div v-if="loggedInAsAdmin">
    <b-list-group class="manage">
      <h3> Events </h3>
      <b-row id="addEvent">
        <b-col> <b-button> Add Event </b-button> </b-col>
     </b-row>
      <b-list-group-item v-for="item in items" key=item.id>
        <b-row>
          <b-col> Name: {{ item.name }} </b-col>
          <b-col> Description: {{ item.description }} </b-col>
          <b-col> <b-button> Delete Event </b-button> </b-col>
       </b-row>
      </b-list-group-item>
    </b-list-group>
  </div>
  <div v-else>
    <h3> You do not have permission to access this page. </h3>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Admin',
  data() {
    return {
      loggedInAsAdmin: false,
      clubName: null,
      items: null
    }
  },
  mounted() {
    this.$axios
      .get('http://localhost:5000/api/loginStatus')
      .then(response => {
        //this.items = response.data;
        //console.log(response.data);
        if(response.data != "") {
          this.loggedInAsAdmin = (response.data[1] === 1) ? true : false;
        }
      })
      .catch(error => {console.log(error)});
    this.$axios
      .get('http://localhost:5000/db/view/events')
      .then(response => {
        //console.log(response.data);
        if(this.loggedInAsAdmin) {
          this.items = response.data;
        }
      })
      .catch(error => {console.log(error)});
  },
  methods: {
    searchClubs() {
    }
  }
}

</script>

<style scoped>
#searchBar {
  height: auto;
  background-color: #AFB781;
}

form {
  margin: 0 auto;
  padding: 15px 15px;
}

h2 {
  text-align: left;
  margin-left: 5%;
  margin-top: 20px;
}

.searchFormElt {
  margin: 0 10px 0 10px;
}

.manage {
  margin: 10px;
}

#addEvent {
  margin-top: 10px;
  margin-bottom: 30px;
}

</style>
