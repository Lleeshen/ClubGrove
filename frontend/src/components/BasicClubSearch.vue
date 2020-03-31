<template>
  <div>
    <div id="searchBar">
      <b-form inline action="/club" @submit.prevent="searchClubs">
        <label class="sr-only" for="searchTerm">Club Name</label>
        <b-form-input class="searchFormElt" v-model="clubName" id="searchTerm" placeholder="Club name"></b-form-input>
        <label class="sr-only" for="clubCategory">Club Category</label>
        <b-form-select class="searchFormElt" v-model="selectedClubCat" :options="clubCatOptions" id="clubCategory"></b-form-select>
        <label for="sortOption">Sorting Option</label>
        <b-form-select class="searchFormElt" v-model="selectedSortOption" :options="sortOptions" id="sortOption"></b-form-select>
        <b-button class="searchFormElt" variant="secondary" type="submit">Search</b-button>
      </b-form>
    </div>
    <h2> Club Results </h2>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'basicSearchClubs',
  props: ['baseClub', 'user'],
  data() {
    return {
      clubName: null,
      selectedClubCat: null,
      clubCatOptions: [
          { value: null, text: 'Select a Club Category' }
      ],
      selectedSortOption: 'ASC',
      sortOptions: [
        //{ value: '1', text: 'Similarity to Search Term'},
        { value: 'ASC', text: 'Alphabetical ascending'},
        { value: 'DESC', text: 'Alphabetical descending'},
      ],
      items: null
    }
  },
  mounted() {
      if(this.user != null)
      {
        this.$axios
            .get('http://localhost:5000/db/view/club?user='.concat(this.user))
            .then(response => {this.items = response.data;})
            .catch(error => {console.log(error)});
      }
      else{
        this.$axios
            .get('http://localhost:5000/db/view/club')
            .then(response => {this.items = response.data;})
            .catch(error => {console.log(error)});
      }
    this.$axios
      .get('http://localhost:5000/api/getClubCategories')
      .then(response => {
        console.log(response.data);
        this.clubCatOptions = this.clubCatOptions.concat(response.data);
       })
      .catch(error => {console.log(error)});

  },
  methods: {
    searchClubs() {
      console.log(this.clubName,this.selectedClubCat,this.selectedSortOption);
      this.$axios
        .post('http://localhost:5000/api/getSearchedClubs',{
          'searchTerm': this.clubName,
          'keyword': this.selectedClubCat,
          'sort': this.selectedSortOption
        })
        .then(response => {
          console.log(response.data);
          this.items = response.data;
        })
        .catch(error => console.log(error))
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