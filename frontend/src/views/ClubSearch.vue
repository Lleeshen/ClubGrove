<template>
  <div>
    <div id="searchBar">
      <b-form inline action="/club">
        <label class="sr-only" for="searchTerm">Club Name</label>
        <b-form-input v-model="text" id="searchTerm" placeholder="Club name"></b-form-input>
        <label class="sr-only" for="clubCategory">Club Category</label>
        <b-form-select v-model="selectedClubCat" :options="clubCatOptions" id="clubCategory"></b-form-select>
        <label for="sortOption">Sorting Option</label>
        <b-form-select v-model="selectedSortOption" :options="sortOptions" id="sortOption"></b-form-select>
        <b-button variant="secondary">Submit</b-button>
      </b-form>
    </div>
    <h2> Club Results </h2>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from 'axios'
export default {
  name: 'searchClubs',
  data() {
    return {
      selectedClubCat: null,
      clubCatOptions: [
          { value: null, text: 'Select a Club Category' },
          { value: '1', text: 'Games' },
          { value: '2', text: 'Science' },
          { value: '3', text: 'Film' },
          { value: '3', text: 'Culture' },
      ],
      selectedSortOption: '1',
      sortOptions: [
        { value: '1', text: 'Similarity to Search Term'},
        { value: '2', text: 'Alphabetical ascending'},
        { value: '3', text: 'Alphabetical descending'},
      ],
      items: [
        { clubName: 'Dickerson', clubDescription: 'Macdonald' },
        { clubName: 'Larsen', clubDescription: 'Shaw' },
        { clubName: 'Geneva', clubDescription: 'Wilson' },
        { clubName: 'Jami', clubDescription: 'Carney' }
      ]
    }
  },
  mounted() {
    axios
      .get('http://localhost:5000/db/view/club')
      .then(response => {this.items = response.data;
       console.log(response) })
      .catch(error => {console.log(error)})
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

</style>
