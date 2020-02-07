<template>
  <div>
    <div id="searchBar">
      <b-form inline action="/club">
        <label class="sr-only" for="searchTerm">Event Name</label>
        <b-form-input class="searchFormElt" v-model="eventName" id="searchTerm" placeholder="Event name"></b-form-input>
        <label class="sr-only" for="searchDescription">Event Description</label>
        <b-form-input class="searchFormElt" v-model="eventDesc" id="searchDescription" placeholder="Event description"></b-form-input>
        <label for="sortOption">Sorting Option</label>
        <b-form-select class="searchFormElt" v-model="selectedSortOption" :options="sortOptions" id="sortOption"></b-form-select>
        <b-button class="searchFormElt" variant="secondary">Search</b-button>
      </b-form>
    </div>
    <h2> Event Results </h2>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'eventSearch',
  data() {
    return {
      eventName: null,
      searchDescription: null,
      selectedSortOption: '1',
      sortOptions: [
        { value: '1', text: 'Similarity to Search Term'},
        { value: '2', text: 'Alphabetical ascending'},
        { value: '3', text: 'Alphabetical descending'},
      ],
      items: [
        { Name: 'Food Run', Description: 'Come get food with us at Cupertino, rides provided', startTime: '2/12/20 5:00 PM', endTime: '2/12/20 7:00 PM', location: 'Shappell Center' },
      ]
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

</style>
