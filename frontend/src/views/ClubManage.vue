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
      <b-row v-for="event in events" :key=event.id class="event" v-on:click="editItem(event)">
        <b-col v-for="field in fields" :key=field.key>
          <span>{{event[field['key']]}}</span>
        </b-col>
        <b-col>
          <span> Edit or Delete </span>
        </b-col>
      </b-row>
      <br />
      <b-button variant='info' v-on:click="addItem()"> Create New Event </b-button>
      <b-modal v-model="showModal">
        <h3 v-if="this.editing"> Edit or Delete Event {{(this.selected).id}} </h3>
        <h3 v-else> New Event </h3>
        <b-form>
          <b-form-group
            id='input-group-1'
            label='Event Name:'
            label-for='input-1'
          >
            <b-form-input
              id='input-1'
              v-model='editEvent.name'
              type='text'
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id='input-group-2'
            label='Event Description:'
            label-for='input-2'
          >
            <b-form-input
              id='input-2'
              v-model='editEvent.description'
              type='text'
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id='input-group-3'
            label='Event Place:'
            label-for='input-3'
          >
            <b-form-input
              id='input-3'
              v-model='editEvent.place'
              type='text'
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id='input-group-4'
            label='Event Start Time:'
            label-for='input-4'
          >
            <b-form-input
              id='input-4'
              v-model='editEvent.starttime'
              type='time'
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id='input-group-5'
            label='Event End Time:'
            label-for='input-5'
          >
            <b-form-input
              id='input-5'
              v-model='editEvent.endtime'
              type='time'
            ></b-form-input>
          </b-form-group>
          <b-form-group>
            <b-container>
              <b-row>
                <b-col><b-button type="submit" variant="primary">Edit</b-button></b-col>
                <b-col><b-button type="submit" variant="danger">Delete</b-button></b-col>
              </b-row>
            </b-container>
          </b-form-group>
        </b-form>
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
        {key:'name', label: 'Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      selected: {},
      showModal: false,
      editing: false,
      newItem: false,
      editEvent: {
        name:'',
        place:'',
        description:'',
        starttime:'',
        endtime:'',
      },
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
    editItem: function (event) {
      this.selected = event;
      this.showModal = true;
      this.editing = true;
      this.newItem = false;
      this.editEvent = {
        name: event.name,
        description: event.description,
        place: event.place,
        starttime: event.starttime,
        endtime: event.endtime,
      }
    },
    addItem: function() {
      this.selected = event;
      this.showModal = true;
      this.editing = false;
      this.newItem = true;
      this.editEvent = {
        name: '',
        description: '',
        place: '',
        starttime: '09:00',
        endtime: '10:00',
      }
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
