<template>
  <div>
    <div id="searchBar">
      <b-form inline action="/events">
        <label class="sr-only" for="searchTerm">Event Name</label>
        <b-form-input class="searchFormElt" v-model="eventName" id="searchTerm" placeholder="Event name"></b-form-input>
        <!--<label class="sr-only" for="searchDescription">Event Description</label>
        <b-form-input class="searchFormElt" v-model="searchDescription" id="searchDescription" placeholder="Event description"></b-form-input>
        -->
        <label for="sortOption">Sorting Option</label>
        <b-form-select class="searchFormElt" v-model="selectedSortOption" :options="sortOptions" id="sortOption"></b-form-select>
        <label for="sortOptionT">Type</label>
        <b-form-select class="searchFormElt" v-model="selectedType" :options="sortOptionsType" id="sortOptionT"></b-form-select>
        <b-button class="searchFormElt" variant="secondary" v-on:click="updateEvent">Search</b-button>
      </b-form>
    </div>
    <h2> Event Results </h2>
    <BasicholderPage 
    :items="items"
    :isEvent="isevent">
    </BasicholderPage>
    <!--
    <b-card-group deck v-if="items" style="margin: 10px">
      <div v-for="item in items">
        <Baseholder v-bind:items="item" 
        :isEvent="false"></Baseholder>
      </div>
    </b-card-group>
    -->
  </div>
</template>

<script>
// @ is an alias to /src
import Baseholder from '../components/Baseholder'
import BasicholderPage from '../components/BasicholderPage'

export default {
  name: 'eventSearch',
  components: {Baseholder,BasicholderPage},
  data() {
    return {
      eventName: null,
      //searchDescription: null,
      selectedType: 'name',
      selectedSortOption: 'true',
      sortOptions: [
        { value: 'true', text: 'Alphabetical ascending'},
        { value: 'false', text: 'Alphabetical descending'},
      ],
      sortOptionsType: [
         { value: 'name', text: 'Name'},
        { value: 'starttime', text: 'Start Time'},
        { value: 'place', text: 'Location'}
      ],
      fields: [
        {key:'name', label: 'Event Name'},
        {key:'description', label: 'Description'},
        {key:'place', label: 'Location'},
        {key: 'starttime', label: 'Start Time'},
        {key: 'endtime', label: 'End Time'}
      ],
      items: [
        { Name: 'Food Run', Description: 'Come get food with us at Cupertino, rides provided', startTime: '2/12/20 5:00 PM', endTime: '2/12/20 7:00 PM', location: 'Shappell Center' },
      ],
      isevent: true
    }
  },
  methods:{
    generateParams: function() {
      if(this.name !=null)
        return '?name=' + this.selectedType + '&sort=' + this.selectedSortOption;
      else
        return '?name=' + this.selectedType + '&sort=' + this.selectedSortOption + '&event=' + this.eventName;
    },
    updateEvent: function (){
      var string2 = 'http://localhost:5000/api/getEvents2'.concat(this.generateParams());
      console.log(string2);
      this.$axios
        .get(string2)
        .then(response => {this.items = response.data;
        console.log(response) })
        .catch(error => {console.log(error)})
    }
  },
  mounted() {
    this.updateEvent();
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

</style>
