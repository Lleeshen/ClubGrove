<template>
  <div>
    <h3> Club  {{ name }} </h3>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'clubEvent',
  data() {
    return {
      validClub: false,
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
      items: null
    }
  },
  mounted() {
    this.$axios
      .post('http://localhost:5000/api/getEvents',{'nm': this.name})
      .then(response => {this.items = response.data;
       console.log(response.data) })
      .catch(error => {console.log(error)})
  },
  props: ['name']
}

</script>
