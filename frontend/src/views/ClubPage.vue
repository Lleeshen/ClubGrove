<template>
  <div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'ClubPage',
  data() {
    return {
      //Replace this with actual club results
      items: null
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


</style>
