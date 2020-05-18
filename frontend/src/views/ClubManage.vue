<template>
  <div v-if="loggedInAsLeader">
    <b-container fluid>
      <h2> Club  {{ name }} </h2>
      <b-row>
        <b-col v-for="field in fields" :key="field.key">
          <h3>{{field['label']}}</h3>
        </b-col>
        <b-col>
          <h3> Edit </h3>
        </b-col>
      </b-row>
      <b-row v-for="event in events" :key=event.id class="event" v-on:click="editItem(event['id'])">
        <b-col v-for="field in fields" :key=field.key>
          <span>{{event[field['key']]}}</span>
        </b-col>
        <b-col>
          <span> Edit or Delete </span>
        </b-col>
      </b-row>
      <br />
      <b-button variant='info'> Create New Event </b-button>
      <b-modal v-model="editing">
        Edit or Delete Event

      </b-modal>
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
        {key:'id', label: 'ID'},
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      selected: null,
      editing: false,
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
                  .post('http://localhost:5000/api/getEvents3',{'nm': this.name})
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
  methods: {
    editItem: function (eventId) {
      console.log('hello',eventId);
      this.selected = eventId;
      this.editing = true;
      console.log('good bye',this.selected)
    }
  },
  props: ['name']
}

</script>

<style scoped>
.event {
  margin: 2px;
  height: 30px;
  background-color:  aliceblue;
}
</style>
