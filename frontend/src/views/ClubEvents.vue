<template>
  <div>
    <h3> Club  {{ name }} </h3>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'clubEvent',
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
      items: null
    }
  },
  mounted() {
    axios
      .get('http://localhost:5000/db/view/club')
      .then(response => {this.items = response.data;
       console.log(response) })
      .catch(error => {console.log(error)})
  },
  props: ['name']
}

</script>
