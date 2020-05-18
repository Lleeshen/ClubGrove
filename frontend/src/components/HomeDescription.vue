<template>
  <b-container fluid>
  <b-row>
  <b-col>
    <img src="@/assets/grove.jpg" style = "max-width: 100%">
  </b-col>
  <b-col cols="7">
  <div class="description">
    <h2>What's Our Goal</h2>
    <div class="decription-content">
    <p>Our goal is to provide a accessible way join an organization.
      Building this website will help club officers, students, and guests
      to see what the clubs a particular school has. At first, this website is 
      only available for SCU, but we hope to expand to other schools.</p>
    </div>
  </div>
  </b-col>
  </b-row>
  <b-row>
  <b-col>
  </b-col>
  <b-col cols="10">
  <div class="description">
  <h2>Searching Clubs and Events</h2>
  <div class="decription-content">
    <p>Near the top of the page, there is a link called "Club Search" where you can search for
    clubs. Clicking it will take you to show the available clubs. In the same general area,
    there is a link called "Event Search". Clicking it will take you will show you all the events.
    Both searches have a search bar and categories. Your search is updated to the last time you search. 
    No worries about deleted clubs existing or newly added clubs not being there
     whenever there is a search.</p>
    </div>
  </div>
  </b-col>
  <b-col>
  </b-col>
  </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'HomeDescription',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.description {
  display: inline-block;
  margin: 10px 0px 0px 0px;
  padding: 10px;
}

 .decription-content {
  background-color: #c7c7c7;
  padding: 10px;
  text-align: left;
  color: black;
}

img {
  padding: 10px;
}

h2,h3 {

}

</style>
