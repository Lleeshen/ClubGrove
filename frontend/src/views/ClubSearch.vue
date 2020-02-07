<template>
  <div>
    <div id="searchBar">
      <b-form inline action="/club">
        <label class="sr-only" for="searchTerm">Club Name</label>
        <b-form-input class="searchFormElt" v-model="clubName" id="searchTerm" placeholder="Club name"></b-form-input>
        <label class="sr-only" for="clubCategory">Club Category</label>
        <b-form-select class="searchFormElt" v-model="selectedClubCat" :options="clubCatOptions" id="clubCategory"></b-form-select>
        <label for="sortOption">Sorting Option</label>
        <b-form-select class="searchFormElt" v-model="selectedSortOption" :options="sortOptions" id="sortOption"></b-form-select>
        <b-button class="searchFormElt" variant="secondary">Search</b-button>
      </b-form>
    </div>
    <h2> Club Results </h2>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'searchClubs',
  data() {
    return {
      clubName: null,
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
