<template>
  <div v-if="loggedInAsAdmin">
    <b-list-group class="manage">
      <h3> Clubs </h3>
      <b-row id="addclub">
        <b-col> <b-button @click="setUpClub"> Add Club </b-button> </b-col>
     </b-row>
      <div v-for="item in items">
        <b-list-group-item  key=item.id>
          <b-row>
            <b-col> Name: {{ item.name }} </b-col>
            <b-col> Description: {{ item.description }} </b-col>
            <b-col> <b-button> Delete club </b-button> </b-col>
         </b-row>
        </b-list-group-item>
      </div>
    </b-list-group>
    <b-modal v-model="clubModal">
      <b-form action="/admin" @submit.prevent="addClub">
        <b-form-group>
          <label for="clubTitle">Title:</label>
          <b-form-input v-model="newClubTitle" id="clubTitle"></b-form-input>
        </b-form-group>
        <b-form-group>
          <label for="clubDescription">Description:</label>
          <b-form-input v-model="newClubDescription" id="clubDescription"></b-form-input>
        </b-form-group>
        <b-form-group>
          <label for="clubWebsite">Website:</label>
          <b-form-input v-model="newClubWebsite" id="clubWebsite"></b-form-input>
        </b-form-group>
        <b-form-group>
          <label for="clubEmail">Description:</label>
          <b-form-input v-model="newClubEmail" id="clubEmail"></b-form-input>
        </b-form-group>
        <b-button variant="secondary" type="submit">Add event</b-button>
      </b-form>
    </b-modal>
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
      items: null,
      clubModal: false,
      newClubId: "",
      newClubTitle: "",
      newClubDescription: "",
      newClubWebsite: "",
      newClubEmail: "",
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
      .get('http://localhost:5000/db/view/club')
      .then(response => {
        console.log(response.data);
        if(this.loggedInAsAdmin) {
          if(typeof response.data !== "string"){
            this.items = response.data;
          }
        }
      })
      .catch(error => {console.log(error)});
  },
  methods: {
    setUpClub() {
      this.clubModal = true;
    },
    addClub() {
      this.clubModal = false;
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

#addclub {
  margin-top: 10px;
  margin-bottom: 30px;
}

</style>
