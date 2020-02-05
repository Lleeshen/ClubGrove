<template>
  <div>
    <div id="searchBar">
      <form class="form-inline" action="/club">
        <div class="form-group">
          <label for="searchTerm">Club name:</label>
          <input type="text" class="form-control" id="searchTerm">
        </div>
        <div class="form-group">
          <label for="clubCat">Select Categories</label>
          <select class="form-control" id="clubCat">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <!-- Club Categories from database goes here -->
          </select>
        </div>
        <div class="form-group">
          <label for="clubSort">Sort Option:</label>
          <select class="form-control" id="clubSort">
            <option>Alphabetical ascending</option>
            <option>Alphabetical descending</option>
            <option>Similarity to search term??</option>
          </select>
        </div>
        <button type="submit" class="btn">Submit</button>
      </form>
    </div>
    <h2> Club Results </h2>
    <b-table bordered hover :items="items"></b-table>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Search Clubs',
  data() {
    return {
      //Replace this with actual club results
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

</style>
