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
        <label for="typeCategory" v-if="user">Status in Club</label>
         <b-form-select class="searchFormElt" v-model="selectedUserOption" :options="userOptions" id="typeCategory" 
        v-if="user"></b-form-select>
        <b-button class="searchFormElt" variant="secondary" type="submit">Search</b-button>
      </b-form>
    </div>
    <h2> Club Results </h2>

    <!---<b-table bordered hover :items="items"></b-table>--->
    <BasicholderPage v-if="hasitems()"
    :items="items" :isUser="isUser">
    </BasicholderPage>
    <!---
    <b-card-group deck v-if="items" style="margin: 10px">
      <div v-for="item in items">
        <Baseholder v-bind:items="item" style="margin-bottom: 30px"></Baseholder>
      </div>
    </b-card-group>
    --->
  </div>
</template>

<script>
// @ is an alias to /src
import Baseholder from '../components/Baseholder'
import BasicholderPage from '../components/BasicholderPage'
export default {
  name: 'basicSearchClubs',
  props: ['baseClub', 'user'],
  components : {Baseholder,BasicholderPage},
  data() {
    return {
      clubName: "",
      selectedClubCat: null,
      clubCatOptions: [
          { value: null, text: 'Select a Club Category' }
      ],
      selectedSortOption: '1',
      sortOptions: [
        { value: '1', text: 'Order Created'},
        { value: 'ASC', text: 'Alphabetical ascending'},
        { value: 'DESC', text: 'Alphabetical descending'},
      ],
      userOptions: [
        { value: 'All', text: 'Show All'},
        { value: 'Member', text: 'Show member'}
      ],
      selectedUserOption: 'All',
      items: null,
      isUser: false
    }
  },
  mounted() {
      if(this.user != null)
      {
        this.isUser = true;
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
        //console.log(response.data);
        this.clubCatOptions = this.clubCatOptions.concat(response.data);
       })
      .catch(error => {console.log(error)});

  },
  methods: {
    searchClubs() {
      //console.log(this.clubName,this.selectedClubCat,this.selectedSortOption);
      this.$axios
        .post('http://localhost:5000/api/getSearchedClubs',{
          'searchTerm': this.clubName,
          'keyword': this.selectedClubCat,
          'sort': this.selectedSortOption,
          'user': this.user,
          'type': this.selectedUserOption
        })
        .then(response => {
          //console.log(response.data);
          this.items = response.data;
        })
        .catch(error => console.log(error))
    },
    hasitems()
    {
      if(this.items && Array.isArray(this.items) && this.items.length >=1 )
      {
        return true;
      }
      return false;
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

#searchBar{
  font-family: Helvetica, Arial, sans-serif;
}

label{
  text-shadow: 0px 2px #CCCCCC;
}
</style>