<template>
  <div class="description">
    <h2>What's Our Goal</h2>
    <div class="decription-content">
    <p>Our goal is to provide a accessible way join an organzation.
      Building this website will help club officers, students, and guests
      to see what the clubs a parituclar school has. At first, this website is 
      only avaliable for SCU, but we hope to expand to other schools.
    </p>
    </div>
  </div>
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
  width: 50%;
  margin: 0px 0px 0px 40%;
  padding: 10px;
}
h2 {
  color: darkred;
}

.description .decription-content {
  background-color: #c7c7c7;
  padding: 10px;
}

</style>
