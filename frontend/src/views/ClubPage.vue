<template>
  <div>
    ok
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'clubPage',
  data() {
    return {
      //Replace this with actual club results
      item: null
    }
  },
  mounted() {
    axios
      .get('http://localhost:5000/db/view/club')
      .then(response => {this.item = response.data;
       console.log(response) })
      .catch(error => {console.log(error)})
  }
}

</script>


</style>
